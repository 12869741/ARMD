Below are the English translations of your eight Chinese rebuttals to Reviewer 3 (R3) for your academic paper, "SeedBench: A Multi-task Benchmark for Evaluating Large Language Models in Seed Science." Each response is paired with its original Chinese version for reference, ensuring precise terminology and alignment with the paper’s formal tone and context.

---

### Rebuttal to Reviewer 3 (R3)

We thank the reviewer for the valuable feedback and suggestions. We have developed a revision plan and respond to the questions as follows:

---

#### Q1: Data Utilization Issue  
**中文:** 在 3.3.1 节中，作者提到收集了 308k 篇文章，其中 86% 通过数据清理过滤掉，剩下大约 40k 篇文章。然而，只使用了 113 个文档，这意味着浪费了大量高质量的数据。作者应该解释为什么没有利用更多这些清理后的数据，并考虑扩展数据集以评估模型的训练和泛化能力。  
**英文:** In Section 3.3.1, the author mentions collecting 308k articles, with 86% filtered out through data cleaning, leaving around 40k articles. However, only 113 documents were used, which means a significant amount of high-quality data was wasted. The author should explain why more of this cleaned data was not utilized, and consider expanding the dataset to evaluate the model’s training and generalization capabilities.  

**A1:**  
We appreciate the opportunity to clarify this point.  
Breeding experts first predefined the three key steps and ten subcategories of real-world breeding (lines 197–241), which represent common challenges in the field. From the 40k articles, 113 documents were selected as the most representative coreset by these experts. They deemed this subset sufficient in terms of breeding strategies and scientific value. The remaining high-quality 40k articles were not wasted; we collected this extensive dataset with the intent of using it for continual pre-training and fine-tuning of large models, which is beyond the scope of this work and thus not detailed in the main text.  
We commit to maintaining and expanding SeedBench in the future, incorporating additional crops and modalities to comprehensively evaluate LLM capabilities.  

---

#### Q2: Clarification on the Proportion of English and Chinese Data  
**中文:** 在提交页面中，作者仅提到了数据集中的英文数据，而提供的数据表明存在大量的中文数据。为确保透明度，作者应澄清数据集中英文和中文数据的比例，并讨论这种语言分布对模型性能的潜在影响。  
**英文:** In the submission page, the author mentions only the English data in the dataset, while data provided indicates that there is a significant amount of Chinese data. To ensure transparency, the author should clarify the proportion of English and Chinese data in the dataset and discuss the potential impact of this language distribution on the model’s performance.  

**A2:**  
We appreciate the reviewer’s note on this point.  
Here, we provide the proportions to address the reviewer’s concerns:  
(1) The initial corpus of 308,727 articles comprises 63% English and 37% Chinese, reflecting the greater availability of English publications;  
(2) After cleaning, the 1.1 billion-token corpus consists of 75% English and 25% Chinese, with this shift due to MinerU’s higher accuracy in processing English texts;  
(3) The final 279 segments used in SeedBench include 49% English and 51% Chinese, achieving balance through manual selection by breeding experts;  
(4) The 2,264 questions in SeedBench include 45% English and 55% Chinese.  
LLMs exhibit strong cross-lingual capabilities, and the linguistic distinction in breeding questions does not alter the underlying scientific logic. We tested this by posing the same question in English and Chinese (with cleared histories) to LLMs, yielding consistent answers:  
- "Question1-EN": "What effect did the overexpression of OsDREB1C have on the levels of photosynthetic pigments in the leaves of the plants? A. Increased pigment levels B. Decreased pigment levels C. Pigment levels fluctuated unpredictably D. No significant change in pigment levels"  
- "Question2-EN": "The expression profile of OsDT11 in different rice tissues was analyzed by ________."  
- "Question1-CN": "OsDREB1C 的过表达对植物叶片中光合色素水平有何影响？A. 增加色素水平 B. 减少色素水平 C. 色素水平不可预测地波动 D. 色素水平没有显著变化"  
- "Question2-CN": "OsDT11 在不同水稻组织中的表达谱通过________分析。"  

| Model             | Ans1-EN | Ans1-CN | Ans2-EN                  | Ans2-CN          |  
|-------------------|---------|---------|--------------------------|------------------|  
| DeepSeek-V3-671B  | A       | A       | quantitative real-time PCR | 实时荧光定量PCR |  
| GPT-4             | A       | A       | quantitative real-time PCR | 实时荧光定量PCR |  

We plan to include these details in Section 3.3.1 (Data Collection, lines 248–282) and Appendix H (line 923) to clarify the language composition and its impact.  

---

#### Q3: Data Quality Issues  
**中文:** 在查看数据集时，很明显基准测试中的一些数据与种子育种没有直接关系。例如，像“水稻灌溉管理的原则是什么？”和“稻瘟病的发病部位包括________、叶片、穗、节”这样的问题似乎与特定品种的特定育种知识无关。这些不相关的数据点可能会对评估结果产生负面影响。  
**英文:** Upon reviewing the dataset, it is apparent that some data in the benchmark is not directly related to seed breeding. For example, questions like “水稻灌溉管理的原则是什么？” and “稻瘟病的发病部位包括________、叶片、穗、节” do not seem to relate to specific breeding knowledge for particular varieties. These irrelevant data points could negatively impact the evaluation results.  

**A3:**  
We thank the reviewer for their thorough examination of the dataset.  
Each question in SeedBench is assigned a precise, expert-validated label tied to the seed science domain, as shown in Figure 2 (encompassing three steps and ten subcategories). The two cited questions directly relate to the third step of the breeding process—“Variety Breeding and Agronomic Traits” (lines 230–241). Specifically, “What are the principles of rice irrigation management?” and “The onset parts of rice blast include ________, leaves, panicles, nodes” fall under (C9) Variety Cultivation and Technical Key Points Query.  
These questions are critical to breeding, as they address downstream agronomic considerations essential for variety success, despite not focusing on early-stage genetics or gene selection. They are integral to SeedBench’s goal of mimicking the expert breeding workflow and evaluating LLMs’ comprehensive breeding knowledge.  

---

#### Q4: Averaging Zero-shot and One-shot Results  
**中文:** 在表 2 中，作者提到了“零发和单发配置的平均值”。如果这是指对单独的 zero-shot 和 one-shot 实验的结果进行平均，建议单独报告结果。对它们进行平均使得很难研究 zero-shot 与 one-shot 配置的具体影响。  
**英文:** In Table 2, the author mentions “averaged across both zero-shot and one-shot configurations.” If this refers to averaging the results from separate zero-shot and one-shot experiments, it is recommended to report the results separately. Averaging them makes it difficult to investigate the specific impact of zero-shot versus one-shot configurations.  

**A4:**  
We agree on the importance of reporting results separately.  
Due to the eight-page limit in the main text, we provided separate zero-shot and one-shot scores in Appendix H.1.9 (Tables 8 and 9). We will enhance the caption of Table 2 in the main text to strengthen guidance, facilitating easier navigation for readers.  

---

#### Q5: Evaluation of Sub-category Tasks  
**中文:** 在表 5（附录 C.2）中，作者表明不同的子类别（C1、C2）包含不同的任务类型，例如多项选择题和生成题，它们具有不同的评估指标。作者需要澄清表 2 中不同子类别的结果是如何计算的。  
**英文:** In Table 5 (Appendix C.2), the author shows that different sub-categories (C1, C2) contain different task types, such as multi-choice and generation questions, which have distinct evaluation metrics. The author needs to clarify how the results of different subcategories in Table 2 are calculated.  

**A5:**  
We thank the reviewer for the opportunity to clarify.  
We reported the three evaluation metrics (Accuracy, Macro-F1, ROUGE-L) for the 11 task types in line 283, and the caption of Table 2 specifies that the scores represent averages across these metrics for the 11 task types.  
The specific calculation involves iterating through each subcategory, computing the metrics for the 11 task types individually, and then averaging these 11 values to derive the subcategory score.  

---

#### Q6: Small Sample Size in Sub-categories  
**中文:** 表 5（附录 C.2）显示子类别 C3 和 C5 分别只有 73 个和 38 个数据点。小样本量可能导致实验偏差，并导致难以准确评估模型在这些子类别中的性能。建议作者增加这些子类目的数据量，以保证评估结果的可靠和稳定。  
**英文:** Table 5 (Appendix C.2) shows that sub-categories C3 and C5 have only 73 and 38 data points, respectively. The small sample size could lead to experimental bias and make it difficult to assess the model’s performance in these sub-categories accurately. It is recommended that the author increase the data volume for these sub-categories to ensure reliable and stable evaluation results.  

**A6:**  
We appreciate the reviewer’s concern regarding the stability of evaluation results.  
In H.1.9, Table 7, we provided standard deviations of scores across C1–C10. The standard deviations for C3 and C5 are not higher than those of other subcategories, indicating reliable and stable results despite the smaller sample sizes.  
Additionally, we commit to continuously maintaining and expanding SeedBench in future work, increasing data points to further enhance evaluation reliability.  

---

#### Q7: Expert Benchmark Performance  
**中文:** 为了更好地评估模型与实际应用之间的差距，建议作者提供育种专家在基准测试中的表现。这种与专家级性能的比较将为如何进一步优化模型提供有价值的见解。  
**英文:** To better evaluate the gap between the model and real-world applications, it is recommended that the author provide the performance of breeding experts on the benchmark. This comparison with expert-level performance would offer valuable insights into how the model can be further optimized.  

**A7:**  
We appreciate the reviewer’s focus on real-world applications.  
As discussed in line 505, LLMs currently fall short of meeting breeding experts’ practical expectations. Our rationale for not conducting expert benchmark testing is as follows:  
(1) All 2,264 questions were validated by six Ph.D.-level experts, requiring significant time and resources. We believe expert judgment is already embedded in the dataset, and recruiting additional experts for benchmark testing would be redundant and of limited value.  
(2) In Section 5 (Discussion, line 513), we elaborated on feedback from experts using LLMs as breeding assistants, enriching our understanding of LLM deficiencies. This approach directly highlights optimization priorities, which we believe more efficiently aligns with the reviewer’s intent to guide LLMs toward real-world breeding applications.  
(3) SeedBench’s data generation process leverages LLMs under expert guidance to save time.  
Your suggestion is valuable, and we will consider establishing a performance standard in the benchmark, indicating that an LLM reaching this threshold qualifies as a competent intelligent breeding assistant.  

---

#### Q8: Crop Proportions in SeedBench  
**中文:** 在第 280-282 行中，作者提到了不同的作物，但没有阐明每种作物在 SeedBench 数据集中的比例。  
**英文:** In lines 280-282, the author mentions different crops, but does not clarify the proportion of each crop in the SeedBench dataset.  

**A8:**  
We value the opportunity to address this point.  
In this paper, to eliminate variability from different species, we selected rice as a representative case for technical demonstration. Rice, the most widely consumed crop globally, feeds over 3.5 billion people (per FAO and World Bank data), particularly in developing countries where hunger is most severe. Thus, this version of SeedBench focuses exclusively on rice, as we believe its insights can generalize across species.  
We are actively expanding SeedBench to include additional species and will continue to do so, providing further support to the research community (https://anonymous.4open.science/r/SeedBench).  

---

We would appreciate it if reviewers could confirm that their concerns have been addressed and, if so, reconsider their assessment. We are happy to engage in further discussions.

---

### Notes on Translation
- **Tone and Style:** The translations maintain a formal, academic tone consistent with the rebuttals to other reviewers, using phrases like “we appreciate,” “we commit to,” and “to address the reviewer’s concerns” to reflect professionalism and responsiveness.
- **Paper-Specific References:** Line numbers (e.g., 197–241, 248–282) and section references (e.g., Section 3.3.1) are retained to align with the LaTeX document structure. Placeholder terms like “TBD” are avoided since specific lines were provided.
- **Technical Accuracy:** Terms such as “coreset,” “subcategories,” “cross-lingual capabilities,” and “breeding workflow” are used to ensure precision and relevance to the paper’s focus on LLMs and seed science.

Let me know if you need further adjustments or additional details!



---
We would appreciate it if reviewers could confirm that their concerns have been addressed and, if so, reconsider their assessment. We are happy to engage in further discussions.
| Task   | Pearson Correlation (BERTScore vs. RougeL) |
|--------|:------------------------------------------:|
| QA-4   |                 0.7937                    |
| SUM-1  |                 0.6770                    |
| SUM-2  |                 0.5811                    |
| RC-3   |                 0.7515                    |
| RC-4   |                 0.7338                    |

| Model             | Ans1-EN | Ans1-CN | Ans2-EN                  | Ans2-CN          |
|:-----------------:|:-------:|:-------:|:------------------------:|:----------------:|
| DeepSeek-V3-671B  |    A    |    A    | qRT-PCR | 实时荧光定量PCR |
| GPT-4             |    A    |    A    | qRT-PCR | 转录组学 |
| OpenAI o1-mini    |    A    |    A    | qRT-PCR | Northern blot分析 |
| gemini-1.5-pro    |    A    |    A    | qRT-PCR | qRT-PCR |

| Models            | QA-4  | SUM-1 | SUM-2 | RC-3  | RC-4  |
|:-----------------:|:-----:|:-----:|:-----:|:-----:|:-----:|
| Claude-3.5-Sonnet | 48.43 | 50.74 | 51.83 | 43.28 | 48.47 |
| Gemini-1.5-Pro    | 72.39 | 74.89 | 73.89 | 95.59 | 79.48 |
| Gemini-2.0-Flash  | 64.6  | 74.84 | 70.85 | 61.71 | 72    |
| GLM-4-Plus        | 79.7  | 83.42 | 80.19 | 95.03 | 84.34 |
| GPT-4o mini       | 81.1  | 83.5  | 82.79 | 93.98 | 86.01 |
| GPT-4             | 79.66 | 87.45 | 85.95 | 96.02 | 88.27 |
| OpenAI o1-mini    | 77.36 | 75.18 | 69.91 | 94.61 | 81.97 |
| DeepSeek-V3       | 81.22 | 83.04 | 81.55 | 94.25 | 85.89 |
| GLM-4-Chat-9B     | 56.1  | 69.45 | 74.72 | 51.17 | 60.93 |
| InternLM2-7B      | 57.49 | 72.76 | 74.04 | 53.83 | 61.34 |
| InternLM2.5-7B    | 76.97 | 84.07 | 81.63 | 91.01 | 85.72 |
| Llama3.1-8B       | 74.91 | 82.11 | 77.87 | 83.28 | 81.18 |
| Llama3.1-70B      | 77.97 | 83.84 | 82.62 | 91.12 | 82.98 |
| Llama3.3-70B      | 76.35 | 81.89 | 79.08 | 87.91 | 82.52 |
| Mistral-v0.3-7B   | 75.13 | 81.98 | 84.54 | 75.94 | 83.66 |
| Qwen2-0.5B        | 75.27 | 78.37 | 76.46 | 64.88 | 79.64 |
| Qwen2-7B          | 77.21 | 78.71 | 78.85 | 84.85 | 82.6  |
| Qwen2-57B         | 80.31 | 82.82 | 83.93 | 92    | 85.83 |
| Qwen2-72B         | 78.75 | 80.23 | 85.11 | 94.51 | 84.53 |
| Qwen2.5-7B        | 77.66 | 81.19 | 82.19 | 82.82 | 83.35 |
| Qwen2.5-14B       | 75.3  | 75.38 | 62.66 | 83.46 | 82.8  |
| Qwen2.5-72B       | 79.5  | 84.38 | 83.5  | 93.16 | 83.14 |
| QwQ-32B           | 70.16 | 70.43 | 69.57 | 65.62 | 73.06 |
| Aksara-v1-7B      | 71.48 | 77.6  | 80.33 | 70.86 | 79.36 |
| PLLaMa-7B         | 69.53 | 64.44 | 63.62 | 62.41 | 69.6  |
| PLLaMa-13B        | 61.73 | 62.46 | 59.66 | 56.95 | 66.64 |

R1 正式版
We thank the reviewer for the valuable feedback and suggestions. We have developed a revision plan and respond to the questions as follows:
Q1: Lack of transparency about the expert correction process or how disagreements were resolved. This is addressed in Appendix very shallowly.
We appreciate the reviewer for this concern. 
To address this, we provide additional clarification regarding the transparency of the expert correction process:
 (1) Composition of the expert panel, which includes six Ph.D.-level experts in seed breeding;
 (2) An iterative review process, in which each question is independently evaluated by at least two experts;
 (3) A disagreement resolution mechanism that accounts for subjectivity in expert assessments, resolved by taking the intersection of differing expert corrections.
We have also open-sourced additional samples that were discarded during the expert correction process as “bad cases” on GitHub (https://anonymous.4open.science/r/SeedBench), providing readers with further insight and reference. Furthermore, we will expand Appendix C (line 805-813) to include the above details to enhance transparency.

---
Q2: The evaluation lacks error analysis, especially of the models' domain-specific failures. Besides, the discussions seem too repetitive, with only the results in one table. It would be better to include other dimensions of the evaluation in the main section. The appendix is full of additional data and results.
We thank the reviewer for highlighting the importance of error analysis.
Due to the 8-page limit, we briefly mentioned the error analysis in the main section (line 417–420). A more comprehensive error analysis is provided in Appendix E (line 863–910), where we summarize eight major causes of domain-specific failures, such as Gene Name Confusion.
To ensure readers do not overlook these important findings, we will enhance the main text by adding explicit references and guidance directing readers to the corresponding appendix sections. Additionally, we will include a table of contents for the appendix to improve navigability and overall readability.

---
Q3: It is not clear how the authors handled and evaluated the texts. Is the final corpus in Chinese or English?
We appreciate the reviewer’s note on this point. 
Here, we provide the proportions to address the reviewer’s concerns: 
(1) The initial corpus of 308,727 articles comprises 63% English and 37% Chinese, with this imbalance reflecting the greater availability of English publications;
(2) After cleaning, the 1.1 billion-token corpus consists of 75% English and 25% Chinese, with this shift due to the higher accuracy of the MinerU (https://github.com/opendatalab/MinerU) in processing English texts;
(3) The final 279 segments used in SeedBench include 49% English and 51% Chinese, achieving balance through manual selection by breeding experts,
(4) The 2,264 questions in SeedBench include 45% English and 55% Chinese.
We plan to include these details in Section 3.3.1 (Data Collection, lines 248–282) to clarify the language composition.

---
Q4: The authors provided an anonymous repo, but it seems that the corpus is not there. It is not well documented.
We apologize for the lack of guidance in the repository. 
We have updated the anonymous repository (https://anonymous.4open.science/r/SeedBench) with the following additions: 
(1) A detailed README file outlining the benchmark structure,
(2) Samples discarded during the expert correction process, 
(3) Expert selection of 279 high-quality text segments.
The directory structure is as follows: 
- base_model_eval/: Used to test base models without dialogue capabilities, i.e., evaluating performance after pretraining. 
- sft_model_eval/: Used to test SFT (Supervised Fine-Tuning) models, with a total of 2,264 questions covering 10 subcategories (see Fig 2). 
  - one-shot/: Organized by 11 task types (see Tab 1). 
  - zero-shot/: Organized by 11 task types (see Tab 1). 
- corpus/: 279 high-quality text segments and low-quality questions discarded after expert validation. 
This ensures the corpus is accessible and well-documented, and we hope it addresses the reviewer’s concerns.

---
We would appreciate it if reviewers can confirm that their concerns had been addressed, if so, reconsider their assessment. We’d be happy to engage in further discussions.

R2 正式版
We thank the reviewer for the valuable feedback and suggestions. We have developed a revision plan and respond to the questions as follows:
Q1: The finding that domain-specific fine-tuned models performed worse than general-purpose models could suggest a limitation in the immediate applicability of current LLMs to seed science, even with fine-tuning. However, if these models were trained on narrowly defined tasks or with data not validated by experts, their lower performance might not be entirely conclusive.
We appreciate the reviewer’s insight. 
We believe this clarification will benefit future research on fine-tuning LLMs for seed science. Similarly, we have noted that some existing benchmarks exhibit comparable shortcomings, such as reliance on unvalidated data (line 165–169) and a focus on overly narrow task domains (line 175–178).
We will revise the discussion in Section 4.3.2 (line 457-487) to elaborate on potential reasons for the reduced performance of fine-tuned models, such as "training on narrowly defined tasks" and "using data not validated by experts". 

---
Q2: While a rigorous validation process was implemented, a significant portion of the benchmark’s questions were automatically generated using GPT-4. This could introduce biases and limit SeedBench's ability to serve as a truly independent and objective measure of LLM performance in seed science.
We are glad to clarify this important concern.
In fact, to ensure the quality of the generated content, we  leverage the involvement of domain experts to ensure that SeedBench aligns with the genuine needs in seed science to the greatest extent possible. SeedBench incorporates extensive expert participation, including:
 (1) Expert selection of 279 high-quality text segments (line 267),
 (2) Expert-crafted 293 example questions (line 275),
 (3) Expert-predefined three breeding steps and ten subcategories (line 197–241), 
 (4) Expert review that removed 20% of biased or irrelevant questions (line 333).
Overall, SeedBench is designed, curated, and validated by experts, and is therefore aligned with expert experience. GPT-4 serves merely as a tool to automate processes and execute expert-designed plans. This automation enhances SeedBench’s scalability for future expansions (e.g., additional crops or modalities), as manually crafting thousands of questions would be neither replicable nor sustainable.

---
Q3: The study acknowledges the importance of multimodal information in seed genetic improvement, yet SeedBench primarily focuses on text-based tasks. Since seed science relies heavily on sensory evaluations and environmental data, the lack of multimodal integration in the benchmark could restrict its ability to fully capture real-world challenges.
Thanks for the constructive suggestion.
SeedBench currently focuses on text and gene-based tasks, aligned with the capabilities of mainstream LLMs that are purely text-based. 
As multimodal LLMs continue to advance, we will expand SeedBench by incorporating multimodal questions involving images and environmental data, thereby addressing this gap in the field.

---
Q4: To evaluate generative text tasks, SeedBench uses RougeL, which, as has been shown in a large number of studies, does not adapt well to the variety of our language when it comes to expressing itself. So from my point of view it would be more correct to use automatic metrics such as BERTScore or MoverScore that take into account the semantic similarities of the generated texts and not only that the generated text is as it appears in the reference text.
We thank the reviewer for this suggestion. 
We have conducted a new reassessment of the generative tasks (QA-4, SUM-1, SUM-2, RC-3, RC-4) using BERTScore, and calculated the Pearson correlation coefficient between BERTScore and RougeL. The results are as follows:
| Task   | Pearson Correlation (BERTScore vs. RougeL) |
|--------|:------------------------------------------:|
| QA-4   |                 0.7937                    |
| SUM-1  |                 0.6770                    |
| SUM-2  |                 0.5811                    |
| RC-3   |                 0.7515                    |
| RC-4   |                 0.7338                    |
We will incorporate this into Appendix H1.9 (line 1004) to provide a more comprehensive evaluation perspective. 
Models
QA-4
SUM-1
SUM-2
RC-3
RC-4
Claude-3.5-Sonnet
48.43
50.74
51.83
43.28
48.47
Gemini-1.5-Pro
72.39
74.89
73.89
95.59
79.48
Gemini-2.0-Flash
64.6
74.84
70.85
61.71
72
GLM-4-Plus
79.7
83.42
80.19
95.03
84.34
GPT-4o mini
81.1
83.5
82.79
93.98
86.01
GPT-4
79.66
87.45
85.95
96.02
88.27
OpenAI o1-mini
77.36
75.18
69.91
94.61
81.97
DeepSeek-V3
81.22
83.04
81.55
94.25
85.89
GLM-4-Chat-9B
56.1
69.45
74.72
51.17
60.93
InternLM2-7B
57.49
72.76
74.04
53.83
61.34
InternLM2.5-7B
76.97
84.07
81.63
91.01
85.72
Llama3.1-8B
74.91
82.11
77.87
83.28
81.18
Llama3.1-70B
77.97
83.84
82.62
91.12
82.98
Llama3.3-70B
76.35
81.89
79.08
87.91
82.52
Mistral-v0.3-7B
75.13
81.98
84.54
75.94
83.66
Qwen2-0.5B
75.27
78.37
76.46
64.88
79.64
Qwen2-7B
77.21
78.71
78.85
84.85
82.6
Qwen2-57B
80.31
82.82
83.93
92
85.83
Qwen2-72B
78.75
80.23
85.11
94.51
84.53
Qwen2.5-7B
77.66
81.19
82.19
82.82
83.35
Qwen2.5-14B
75.3
75.38
62.66
83.46
82.8
Qwen2.5-72B
79.5
84.38
83.5
93.16
83.14
QwQ-32B
70.16
70.43
69.57
65.62
73.06
Aksara-v1-7B
71.48
77.6
80.33
70.86
79.36
PLLaMa-7B
69.53
64.44
63.62
62.41
69.6
PLLaMa-13B
61.73
62.46
59.66
56.95
66.64

---
Q5: The paper includes an extremely extensive appendix (over 40 pages) which, while providing valuable details on the experiments, is almost a separate article, making it somewhat difficult to navigate.
Thanks for pointing this out.
The appendix is over 40 pages, because we believe this is a novel and underexplored topic with promising scientific value. We aim to share our insights and findings as comprehensively as possible with the research community.
To mitigate this issue, we promise to enhance guidance within the main text by referencing key appendix content more explicitly, thereby improving reader accessibility. Additionally, we will add a table of contents for the appendices. 

---
Q6: In some parts of the article, different points are distinguished using bolded keywords followed by explanatory text (e.g., Section 4.1, line 359 and 375). In these cases, I suggest adding a period between the bolded word and the explanatory text to improve readability.
Thank you! 
We will implement this suggestion to enhance readability. 

---
Q7: In Section 4.1 (Implementation Details), it is stated that models are evaluated using two different strategies: zero-shot learning and one-shot learning. Is there a specific reason for selecting one-shot learning rather than including or testing with a larger number of examples?
We thank the reviewer for this comment. 
Our current setup follows LawBench [1], an influential domain-specific benchmark. 
Additionally, SeedBench aims to evaluate LLMs as intelligent assistants for breeding experts, expecting LLMs achieving strong performance with minimal examples. This minimizes the burden on users to provide extensive examples for improved performance, aligning with practical usability in seed science workflows.
We will explore few-shot strategies in future work. 
[1] LawBench: Benchmarking Legal Knowledge of Large Language Models (Fei et al., EMNLP 2024)

---
**Q8: Section 4.2 mentions that Appendix H provides a detailed analysis of the performance differences between models of varying sizes and series. In my opinion, this is an important aspect of the paper and should not be placed in an appendix. Appendices are typically used for additional data, but analytical discussions should be included in the main text.**
Thanks for this comment.
Due to the 8-page limit of the main text, we included a condensed version of the analysis in Section 4.3.3 (line 448–503), while the detailed experimental results and tables were placed in Appendix H1.5.
We will enhance Section 4.3.3 by adding explicit guidance that highlights the significance of the in-depth analysis in Appendix H1.5, thereby improving clarity and accessibility for readers.

---
**Q9: In line 535, there is a grammatical mistake: "Pproducers" should be corrected to "Producers."**
Thanks for your careful review and valuable suggestions. 
We will correct this typo. 

---
We would appreciate it if reviewers can confirm that their concerns had been addressed, if so, reconsider their assessment. We’d be happy to engage in further discussions.

R3 正式版

We thank the reviewer for the valuable feedback and suggestions. We have developed a revision plan and respond to the questions as follows:
**Q1: Data Utilization Issue**
We appreciate the opportunity to clarify this point.
Breeding experts first predefined the three key steps and ten subcategories of real-world breeding (line 197–241), which represent common challenges in the field. From the 40k articles, 113 documents were selected as the most representative coreset by these experts. They deemed this subset sufficient in terms of breeding strategies and scientific value. The remaining high-quality 40k articles were not wasted; we collected this extensive dataset with the intent of using it for continual pre-training and fine-tuning, which is beyond the scope of this work and thus not detailed in the main text.
And we promise to maintain and expand SeedBench in the future, incorporating additional crops and modalities to comprehensively evaluate LLM capabilities.

---
**Q2: Clarification on the Proportion of English and Chinese Data**
We appreciate the reviewer’s note on this point.  
Here, we provide the proportions to address the reviewer’s concerns:  
(1) The initial corpus of 308,727 articles comprises 63% English and 37% Chinese, reflecting the greater availability of English publications;  
(2) After cleaning, the 1.1 billion-token corpus consists of 75% English and 25% Chinese, with this shift due to the higher accuracy of the MinerU (https://github.com/opendatalab/MinerU)  in processing English texts;  
(3) The final 279 segments used in SeedBench include 49% English and 51% Chinese, achieving balance through manual selection by breeding experts;  
(4) The 2,264 questions in SeedBench include 45% English and 55% Chinese.  
Although LLMs exhibit strong cross-lingual capabilities and the linguistic differences in breeding questions do not alter the underlying scientific logic, we observed response drift when posing the same question in English and Chinese (with cleared histories). This phenomenon suggests potential issues in cross-lingual consistency, which deserves further research—especially when applying LLMs in specific domain where alignment across languages is critical:
- "Question1-EN": "What effect did the overexpression of OsDREB1C have on the levels of photosynthetic pigments in the leaves of the plants? A. Increased pigment levels B. Decreased pigment levels C. Pigment levels fluctuated unpredictably D. No significant change in pigment levels"  
- "Question2-EN": "The expression profile of OsDT11 in different rice tissues was analyzed by ________."  
- "Question1-CN": "OsDREB1C 的过表达对植物叶片中光合色素水平有何影响？A. 增加色素水平 B. 减少色素水平 C. 色素水平不可预测地波动 D. 色素水平没有显著变化"  
- "Question2-CN": "OsDT11 在不同水稻组织中的表达谱通过________分析。"  

We plan to include these details in Section 3.3.1 (Data Collection, line 248–282) and Appendix H (line 923) to clarify the language composition and its impact.  

---
**Q3: Data Quality Issues**
We thank the reviewer for the thorough examination of the dataset.  
Each question in SeedBench is assigned a precise, expert-validated subcategory label tied to the seed science domain, as shown in Figure 2 (encompassing three essential seed breeding stages and ten subcategories). The two cited questions directly relate to the third stage of the breeding process—“Variety Breeding and Agronomic Traits” (lines 230–241). Specifically, “水稻灌溉管理的原则是什么？” and “稻瘟病的发病部位包括________、叶片、穗、节”  are labeled (C9) Variety Cultivation and Technical Key Points Query (line 239).  
These questions are critical to breeding, as they address downstream agronomic considerations essential for variety success, despite not focusing on early-stage genetics or gene selection. They are integral to SeedBench’s goal of simulating the breeding process and evaluating LLMs’ comprehensive breeding knowledge.  

---
**Q4: Averaging Zero-shot and One-shot Results**
We agree on the importance of reporting results separately.  
Due to the eight-page limit in the main text, we provided separate zero-shot and one-shot scores in Appendix H.1.9 (Tables 8 and 9). We mentioned these results in the caption of Table 2 in the main text to strengthen guidance, facilitating easier navigation for readers.  

---
**Q5: Evaluation of Sub-category Tasks**
We thank the reviewer for the opportunity to clarify.  
We reported the three evaluation metrics (Accuracy, Macro-F1, ROUGE-L) for the 11 task types in line 283, and the caption of Table 2 specifies that the scores represent averages across these three metrics for the 11 task types. Specifically, the calculation involves iterating through each subcategory, computing the three metrics for each of the 11 task types, and then averaging the results to obtain a single score per subcategory.
We will add this calculation procedure clearer in Appendix D.2 (line 824) to avoid any potential confusion.

---
**Q6: Small Sample Size in Sub-categories**
We appreciate the reviewer’s concern regarding the stability of evaluation results.  
In Table 7 (Appendix H.1.9, line 1004), we provided standard deviations of scores across C1–C10. The standard deviations for C3 and C5 are not higher than those of other subcategories, indicating reliable and stable results despite the smaller sample sizes.  
Additionally, we commit to continuously maintaining and expanding SeedBench in the future, increasing data points to further enhance evaluation reliability.  

---
**Q7: Expert Benchmark Performance**
We appreciate the reviewer’s focus on real-world applications.  
As discussed in line 505, LLMs currently fall short of meeting breeding experts’ practical expectations. Our rationale for not conducting expert benchmark testing is as follows:  
- All 2,264 questions were validated by six Ph.D.-level experts, requiring significant time and resources. We believe expert judgment is already embedded in the dataset, and recruiting additional experts for benchmark testing would be redundant and of limited value.  
- In Section 5 (Discussion, line 513), we elaborated on feedback from experts using LLMs as breeding assistants, enriching our understanding of LLM deficiencies. This approach directly highlights optimization priorities, which we believe more efficiently aligns with the reviewer’s intent to guide LLMs toward real-world breeding applications.  
- SeedBench’s data generation process leverages LLMs under expert guidance to save time.  
Your suggestion is valuable, and we will consider establishing a expert performance standard in the benchmark, indicating that an LLM reaching this threshold qualifies as a competent smart breeding assistant.  

---
**Q8: Crop Proportions in SeedBench**
We value the opportunity to address this point.  
In this paper, to eliminate variability from different species, we selected rice as a representative case for technical demonstration. Rice, the most widely consumed crop globally, feeds over 3.5 billion people (per FAO and World Bank data), particularly in developing countries where hunger is most severe. Thus, this version of SeedBench focuses exclusively on rice, as we believe its insights can generalize across species.  
We are actively expanding SeedBench to include additional species and will continue to do so, providing further support to the research community.(https://anonymous.4open.science/r/SeedBench)  

---
We would appreciate it if reviewers could confirm that their concerns have been addressed and, if so, reconsider their assessment. We are happy to engage in further discussions.




