<!--[![arXiv](https://img.shields.io/badge/arXiv-2502.07190-b31b1b.svg?style=plastic)](https://arxiv.org/abs/2502.07190) [![Web](https://img.shields.io/badge/Web-ARAOC-blue.svg?style=plastic)](https://wujunjie1998.github.io/araoc-benchmark.github.io/)-->

This repository contains the code and data of the paper:

> Ref-Long: Benchmarking the Long-context Referencing Capability of Long-context Language Models
> 
> [Junjie Wu](https://wujunjie1998.github.io/), [Gefei Gu](https://frankgu3528.github.io/), [Yanan Zheng](https://scholar.google.com/citations?hl=zh-CN&user=0DqJ8eIAAAAJ&view_op=list_works&sortby=pubdate), [Dit-Yan Yeung](https://sites.google.com/view/dyyeung), [Arman Cohan](https://armancohan.com/)



## Data
The `data` folder contains the four Ref-Long subsets used in our paper. Each subset includes two prompt formats—**"ori"** and **"before"**—as described in Appendix B. 

Since different LCLMs may perform better with different input formats, we recommend that users try both formats when first evaluating a model, and then select the one that yields better results for subsequent experiments.


## Run the Experiments

### Obtain LCLMs' results.

We provide an example of evaluating the GPT-4o model on the Ref-Long benchmark. Users can configure the following parameters in `gpt4.sh` to evaluate the LCLM on different subsets and settings:

- `datasets`
- `prompt_types`
- `task_types`
- `document_numbers`

After setting the parameters, run:


```
./gpt4.sh
```
to obtain GPT-4o's results on the specified files.

### Evaluation
After generating results with the previous files, you can run
```
Python evaluate.py 
```

This script calculates the Exact Accuracy (Ex Acc) and F1 scores for different model outputs. You can customize the evaluation by modifying the following parameters:

- `evaluate_model`
- `dataset`
- `prompt_types`
- `task_types`
- `document_numbers`


## Citation

```bibtex
@article{wu2025understanding,
  title={Understanding LLMs' Fluid Intelligence Deficiency: An Analysis of the ARC Task},
  author={Wu, Junjie and Yu, Mo and Liu, Lemao and Yeung, Dit-Yan and Zhou, Jie},
  journal={arXiv preprint arXiv:2502.07190},
  year={2025}
}
```



