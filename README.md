# SemEval-2014-Task-1
In this project, I will focus on building a model for multi-output learning using the SemEval 2014 Task 1 dataset. This dataset contains text samples, each associated with multiple labels, reflecting complex relationships inherent in real-world data. 

The competition aims to evaluate computational models that measure the similarity between pairs of sentences. Given two text fragments, the goal is to assign a similarity score that reflects their meaning closeness, which is useful in applications such as machine translation, information retrieval, and text summarization.

This project will provide valuable insights into how machine learning can effectively deal with multi-label classification challenges.

## SemEval 2014 Task 1 dataset
Task Description: Evaluation of compositional distributional semantic models on full sentences through semantic relatedness and textual entailment.

This challenge involves two sub-tasks:

- sub-task1: predicting the degree of relatedness between two sentences (eg. **regression**)

- sub-task2: detecting the entailment relation holding between them (eg. **3-class classification**)

Dataset describtion: 

- Train split: 4500 pieces

- Validation split: 500 pieces

- Test split: 4927 pieces

- Each data piece: 
    - premise

    - hypothesis
        
    - relatedness_score: A numerical score (e.g., from 0 to 5) that indicates the semantic similarity between the premise and the hypothesis.
        
    - entailment_judgement: A categorical label that classifies the relationship between the premise and the hypothesis. (including 3: Contradiction, 2: Entailment, 0: Neutral)

![image](https://github.com/user-attachments/assets/07d226d2-99ab-4874-a3fb-b7a1ef38c0f4)

## Data Preprocessing

This pipeline processes the data to use with a BERT-based model. 

1. Define `SemevalDataset` class

    - Loads and processes the SemEval 2014 Task 1 dataset.

    - Maps entailment_judgment to numeric labels and returns cleaned records.

2. Define bert base tokenizer: Uses `BertTokenizer` to convert sentences into BERT-compatible tokens.

3. Define `collate_fn()` function: Prepares batches by tokenizing sentences and converting data into tensors.

    - Handling Variable-Length Sequences: Ensures consistent input length by padding or truncating sentences.

    - Converting to Tensors: Converts tokenized text into tensors, which models require for training.

    - Attention Masks and Token Type IDs: Provides extra information like which tokens to attend to and which sentence they belong to.

4. Build own DataLoader : Creates training and validation DataLoaders, shuffling data for training.

