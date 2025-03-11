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

