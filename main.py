# 导入必要的库
import os  # 用于操作系统接口，例如文件和目录操作
import torch  # PyTorch深度学习框架
import numpy as np  # 用于数值计算的库
import random  # 用于生成随机数的模块
import argparse  # 用于解析命令行参数

import warnings  # 用于管理警告信息
warnings.filterwarnings("ignore")  # 忽略所有警告信息，避免干扰输出

# 导入自定义模块和函数
from engine.solver import Trainer  # 自定义的训练器类，用于模型训练
from sklearn.metrics import mean_squared_error  # 计算均方误差（MSE）
from sklearn.metrics import mean_absolute_error  # 计算平均绝对误差（MAE）
from torch.utils.data import Dataset, DataLoader  # PyTorch的数据集和数据加载器
from gluonts.dataset.repository.datasets import get_dataset  # 从GluonTS获取数据集
from gluonts.dataset.multivariate_grouper import MultivariateGrouper  # 用于多变量数据处理
from Utils.io_utils import load_yaml_config, instantiate_from_config  # 加载YAML配置和实例化模型
from Models.autoregressive_diffusion.model_utils import normalize_to_neg_one_to_one, unnormalize_to_zero_to_one  # 数据归一化与反归一化工具
from Data.build_dataloader import build_dataloader, build_dataloader_cond  # 构建训练和测试数据加载器

def set_seed(seed):
    """
    设置随机种子以确保实验的可重复性。
    
    参数:
    - seed (int): 种子值，用于初始化随机数生成器。
    """
    # 设置Python内置random模块的种子
    random.seed(seed)
    
    # 设置NumPy的随机种子
    np.random.seed(seed)
    
    # 设置PyTorch的随机种子
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)  # 为所有GPU设置种子
    torch.backends.cudnn.deterministic = True  # 确保CuDNN使用确定性算法
    torch.backends.cudnn.benchmark = False  # 禁用基准测试以确保可重复性
    
    # 为CuDNN后端设置额外的种子
    os.environ['PYTHONHASHSEED'] = str(seed)

# 示例用法：设置随机种子为2023
set_seed(2023)

class Args_Example:
    def __init__(self, config_path, save_dir, gpu):
        """
        定义命令行参数示例类，用于存储配置路径、保存目录和GPU编号。
        
        参数:
        - config_path (str): 配置文件路径。
        - save_dir (str): 保存实验结果的目录。
        - gpu (int): 指定使用的GPU编号。
        """
        self.config_path = config_path  # 配置文件路径
        self.save_dir = save_dir  # 保存实验结果的目录
        self.gpu = gpu  # GPU编号
        os.makedirs(self.save_dir, exist_ok=True)  # 创建保存目录，如果已存在则不报错

def parse_arguments():
    """
    解析命令行参数。
    
    返回:
    - args: 包含解析后的参数对象。
    """
    parser = argparse.ArgumentParser(description="处理配置和目录。")
    parser.add_argument('--config_path', type=str, required=True,
                        help='配置文件路径。')
    parser.add_argument('--save_dir', type=str, default='./forecasting_exp',
                        help='保存实验结果的目录，默认为./forecasting_exp。')
    parser.add_argument('--gpu', type=int, default=0,
                        help='指定使用哪个GPU，默认为0。')
    
    args = parser.parse_args()  # 解析命令行参数
    return args

if __name__ == "__main__":
    # 解析命令行参数
    args_parsed = parse_arguments()
    # 创建Args_Example实例，存储配置路径、保存目录和GPU编号
    args = Args_Example(args_parsed.config_path, args_parsed.save_dir, args_parsed.gpu)
    
    # 设置时间序列长度
    seq_len = 96
    
    # 从YAML配置文件加载配置信息
    configs = load_yaml_config(args.config_path)
    
    # 设置设备：如果GPU可用则使用指定的GPU，否则使用CPU
    device = torch.device(f'cuda:{args.gpu}' if torch.cuda.is_available() else 'cpu')
    
    # 根据配置文件中的模型配置实例化模型，并将其移动到指定设备上
    model = instantiate_from_config(configs['model']).to(device)
    
    # 设置模型的fast_sampling属性为True，启用快速采样模式
    model.fast_sampling = True
    
    # 构建训练数据加载器
    dataloader_info = build_dataloader(configs, args)
    dataloader = dataloader_info['dataloader']  # 获取数据加载器
    
    # 创建训练器实例，传入配置、参数、模型和数据加载器
    trainer = Trainer(config=configs, args=args, model=model, dataloader={'dataloader':dataloader})
    
    # 开始训练模型
    trainer.train()
    
    # 设置模式为预测模式
    args.mode = 'predict'
    
    # 设置预测长度为序列长度
    args.pred_len = seq_len
    
    # 构建测试数据加载器（可能带有条件）
    test_dataloader_info = build_dataloader_cond(configs, args)
    
    # 获取测试数据集的样本（已缩放）
    test_scaled = test_dataloader_info['dataset'].samples
    
    # 获取数据集的缩放器，用于数据缩放和反缩放
    scaler = test_dataloader_info['dataset'].scaler
    
    # 设置序列长度（训练序列长度*2）和特征数量
    seq_length, feat_num = seq_len*2, test_scaled.shape[-1]
    
    # 设置预测长度
    pred_length = seq_len
    
    # 真实的测试数据（已缩放）
    real = test_scaled
    
    # 获取测试数据集和数据加载器
    test_dataset = test_dataloader_info['dataset']
    test_dataloader = test_dataloader_info['dataloader']
    
    # 使用训练器进行预测，生成预测样本
    sample, real_ = trainer.sample_forecast(test_dataloader, shape=[seq_len, feat_num])
    
    # 获取测试数据集的掩码，用于标识缺失值或需要预测的部分
    mask = test_dataset.masking
    
    # 计算预测样本与真实值之间的均方误差（MSE）
    mse = mean_squared_error(sample.reshape(-1), real_.reshape(-1))
    
    # 计算预测样本与真实值之间的平均绝对误差（MAE）
    mae = mean_absolute_error(sample.reshape(-1), real_.reshape(-1))
    
    # 打印MSE和MAE
    print(mse, mae)
