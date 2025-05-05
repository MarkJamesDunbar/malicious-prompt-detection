# malicious-prompt-detection

Quick project to analyze various techniques for detecting malicious LLM prompting activity.

## Features

- **DataLoader**: A utility class for batching data during model training or analysis.
- **Notebook Examples**: Demonstrates data loading and basic exploration.

## Project Structure

```
malicious-prompt-detection/
├── README.md
├── pyproject.toml
├── data/
├── notebooks/
├── src/
│   ├── dataloader.py
│   ├── models/
│   ├── utils/
│   └── database/
├── tests/
└── docs/
```

## Usage

1. Install dependencies using Conda:
    ```bash
    conda create -n malicious-prompt-detection python=3.8 -y
    conda activate malicious-prompt-detection
    conda install pandas numpy scikit-learn duckdb jupyter -y
    ```

2. Use the `DataLoader` class to batch your dataset:
    ```python
    from src.dataloader import DataLoader

    data_loader = DataLoader(df, batch_size=32)
    for batch in data_loader:
        print(batch.head())
    ```

3. Explore the dataset using the provided Jupyter notebooks:
    ```bash
    jupyter notebook
    ```

https://huggingface.co/datasets/ahsanayub/malicious-prompts/viewer/default/train?f%5Bid%5D%5Bmin%5D=373650&f%5Bid%5D%5Bmax%5D=420356
