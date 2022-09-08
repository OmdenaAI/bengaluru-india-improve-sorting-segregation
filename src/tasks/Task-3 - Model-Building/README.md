# Task 3 
-  **The Task 3 dealts with building models for each dataset and they have been displayed here under respective folders**.

1. [**Dataset 11 Models**](https://github.com/OmdenaAI/bengaluru-india-improve-sorting-segregation/tree/main/src/tasks/Task-3%20-%20Model-Building/Models%20Made%20for%20Dataset%2011)

2. [**Dataset 1 Models**](https://github.com/OmdenaAI/bengaluru-india-improve-sorting-segregation/tree/main/src/tasks/Task-3%20-%20Model-Building/Models%20for%20Dataset%201)

3. [**Final Modified Dataset Models**](https://github.com/OmdenaAI/bengaluru-india-improve-sorting-segregation/tree/main/src/tasks/Task-3%20-%20Model-Building/Final%20Datasets%20and%20Models)

- **Each Folder Contains the Models made by all the contributors and also contains the final model file that can be used for deployment**

## SUMMARY OF TASK 3

### **Aim** :
 - To create various models for the finalised dataset using various computer vision algorithms  and finally find a proper model for real world usage. 

### **Work Done** :
- Initially 4 various datasets were made to be tested so around 10 different architectures and algorithms were tested on each of them.
- Through continuous meetings top 5 models based on testing accuracies were carried forward to the Task 4 team  for further  deployment.
- Subsequent debugging and code were optimised for easy deployment.
- All the models tested were recorded with their computational time and accuracy.

### **Challenges Faced** :
- Due to the high no.of algorithms present in working it was a time consuming task to create around 10 models for each of the 4 datasets.
- Newer algorithms like VGG16 were modified by prior references from blogposts and research papers which took some time to get running.


## Model Performance Comparison


SI No.		| Model Architecture | Dataset Used | Training Accuracy | Testing Accuracy | No.of Epochs(Early Stopping)
--- | --- | --- | --- |  --- | --- |
1	| Custom CNN V1 | Dataset 1 | 55%| 53% | 20 Epochs
2	| Custom CNN V2 | Dataset 11 | 86%| 76% | 20 Epochs
3	| Custom CNN V3 | Dataset 11 | 73%| 70% | 10 Epochs
4	| MobileNet v2 | Dataset 11 | 96%| 91% | 20 Epochs (15)
5	| XceptionNet | Dataset 11 | 97%| 93% | 100 Epochs (16)
6	| VGG19 | Dataset 11 | 94%| 91% | 20 Epochs (15)
7	| VGG16 + SVM| Dataset 11 | 97%| 93% | 20 Epochs (16)
