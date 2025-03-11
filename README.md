# SemEval-2014-Task-1
In this project, I will focus on building a model for multi-output learning using the SemEval 2014 Task 1 dataset. This dataset contains text samples, each associated with multiple labels, reflecting complex relationships inherent in real-world data. Given two text fragments, the goal is to assign a similarity score that reflects their meaning closeness, which is useful in applications such as machine translation, information retrieval, and text summarization.

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

## Data Explore
This dataset distribution table shows the class breakdown for the SICK (Sentences Involving Compositional Knowledge) dataset, which is used for semantic relatedness and textual entailment tasks. It consists of a training set (4,934 samples) and a test set (4,906 samples).

1. Higher Relatedness Correlates with Entailment:

    - The majority of ENTAIL cases appear in the 4-5 relatedness range, meaning highly similar sentences often entail each other.

2. Contradictions Are More Common in the 3-4 Range:

    - Many CONTRADICT cases are in the 3-4 relatedness range, suggesting that moderate similarity often leads to contradictions.

3. Training vs. Test Set:

    - The distribution is similar between training and test sets, ensuring consistency in model evaluation.

![image](https://github.com/user-attachments/assets/ae0fe04e-6a50-4d50-8139-ea690f47e512)

## Construct Model

My model achiteture: 

<img width="891" alt="image" src="https://github.com/user-attachments/assets/265767d9-df66-4f4b-b8d4-f2e8acbf8832" />


(1) Pre-trained Model Selection: I chose **bert-base-uncased** from Hugging Face for the following reasons:

- Case-Insensitivity:  Since SemEval 2014 Task 1 focuses on semantic similarity, case differences are unnecessary, and an uncased model simplifies the vocabulary.

- Pre-training Benefits: The model is trained on a large English corpus, saving computation and training time.

- Versatility: BERT excels in NLP tasks like classification and entailment prediction, making it ideal for this task.

- Generalization: The uncased version reduces vocabulary size and improves performance on tasks not reliant on capitalization.


(2) Multi-Output Learning: I find that multi-output learning improves the performance. Comparing separately trained models with a multi-task learning (MTL) approach, we find MTL performs slightly better. Possible reasons:

- Shared Knowledge: MTL enables a single model to learn multiple related tasks, capturing common features and improving efficiency, especially with limited data.

- Enhanced Generalization: MTL can reduce overfitting by leveraging more data from other tasks, helping the model generalize better in low-resource situations.

- Model Consistency: MTL maintains overall model consistency and prevents excessive focus on a single task, improving performance across tasks.

(3) Aggregation of the losses from two sub-tasks: 

- Mean Squared Error Loss (MSE Loss): Measures the average squared difference between predicted and true numeric values, useful for regression tasks. It’s computed as 
```python
self.mse_loss(pred_numeric, true_numeric).
```

- Cross-Entropy Loss (CE Loss): Quantifies the difference between predicted probabilities and actual classes, commonly used for classification tasks. It’s calculated with
```python
self.ce_loss(pred_category, true_category).
```

- Both losses are combined into a total loss using:
```python
total_loss = alpha * loss_numeric + (1 - alpha) * loss_category
```

The parameter alpha controls the weight of each loss, allowing you to balance the focus between regression and classification tasks. For instance, alpha = 0.5 gives equal weight to both losses. This enables the model to learn from both numeric and categorical outputs effectively.

## Test
The output you've provided includes some evaluation metrics commonly used to assess the performance of a machine learning model. Here’s a brief explanation of each metric:
- Spearman Correlation Coefficient (Spearman): 0.8134
- Accuracy: 0.8563
- F1 Score: 0.8525

