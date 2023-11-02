# My approach and insights for the project

## Approach and Insights

As the data is about bank marketing, out of all the features, these caught my attention the most:

- job
- balance
- loan
- duration

I think these features will be the most important ones for the bank to consider when deciding whether to call a customer or not. For example, if a customer has a high balance, then the bank should definitely call them. On the other hand, if a customer has a loan, then the bank should not call them. Keeping these in mind, I started the data analysis.

First of all I saw that there were no missing data. So I did not have
to deal with them. The data was highly imbalanced though.

After that I separated the attributes into binary types, categorial types and numeric types as I would have to handle them differently. For the binary types, I converted the "yes" and "no" to 1 and 0 for simplicity. For the numerical types, I plotted histogram to see the distribution of data. From what I saw is that columns like `balance`, `previous`, `duration`, `pdays`, `campaign` were higly skewed toward left. I had to deal with them during the modeling phase. For the categorial types, I plotted box plots to see how they are distributed across the dataset.

After going through the data exploration steps, I started doing specific analysis. First, I started with monthwise analysis. How many records do I have for each month and how many of them were converted to long term deposit. I saw that the month of may had the most amount of records, but the convertion rate was very low, where instead the month of december had the most convertion rate. After some exploration online, I found some possible reason for those. The reasons are explained in the `EDA.ipynb` notebook.

Then I thought about the marital status, having a larger family can have heavy impact on ones financials. And I found that customers with marital status of divorced and single were converted more.

I had a column age, and profession which could segmeent the customer base in a pretty good way and got some insight from there that students and retired people can be good targeted customers.

Also as said before, having a loan in pending, customers would be less interested in deposits and more interested in repaying the debts, which I also saw from the data.

As a telemarketing approach, duration of how long a sales representative talks to a customer is very important. I saw that the longer the duration, the more likely the customer is to convert. But longer than some point, the duration does not matter anymore. So the bank should keep the call running for too long as it might annoy them.

During a marketing campaing, the bank might call the same customer multiple times. I found some ideal number of times to call a customer, after which the bank should stop calling them.

I also found out that customers who were never contacted before a campaign has lesser chance of getting converted. So if the bank can not convert a customer during one campaing, they still have a chance to convert them in the next campaign.

Staying in touch with a customer can provide some more benefits. I found out some ideal time period after which contacting the same customer might not be beneficial anymore. Also, after successful campaings for customers, the probability was higher for convertion, so campaigns are useful but they should check this rate between successive campaings to see the effectiveness of the campaign.

## Approach for modeling

Given the attributes, my goal was to predict whether a customer would convert or not. A correct and strong model could reduce the work load of sales representatives, resulting in more accurate and efficient marketing campaigns. I tried to use the following models:

- Decision Tree
- Naive Bayes

For training and testing, I separted the dataset into 80%, 20% portions.

For decision tree, I used `GridSearchCV` to search for the best hyperparameters. After the model training I Used the test data for the final evaluation. Here is the result:

|   | Precision | Recall | F1-Score | Support |
|---|-----------|--------|----------|---------|
| 0 | 0.92      | 0.97   | 0.94     | 801     |
| 1 | 0.56      | 0.31   | 0.40     | 104     |
|   | Accuracy  |         | 0.89     | 905     |
|   | Macro Avg | 0.74   | 0.64     | 0.67    | 905     |
|   | Weighted Avg | 0.87 | 0.89  | 0.88    | 905     |

As the data is highly imbalanced, the model is biased towards the negative class which is in majority. After training the model I wanted to see the features that got the most importance. Top 2 were:

1. duration - 0.516
2. other outcomes - 0.225

For the naive bayes model, I used the Gaussian Naive Bayes, and also saw very close results:

|   | Precision | Recall | F1-Score | Support |
|---|-----------|--------|----------|---------|
| 0 | 0.92      | 0.89   | 0.90     | 801     |
| 1 | 0.31      | 0.38   | 0.34     | 104     |
|   | Accuracy  |         | 0.83     | 905     |
|   | Macro Avg | 0.62   | 0.64     | 0.62    | 905     |
|   | Weighted Avg | 0.85 | 0.83     | 0.84    | 905     |

As the data was highly imbalanced, I tried oversampling techniques to balance the classes. I tried **SMOTE** and **ADASYN** for this purpose. After oversampling, I got the following results using decision tree classifier:

1. SMOTE

    |   | Precision | Recall | F1-Score | Support |
    |---|-----------|--------|----------|---------|
    | 0 | 0.93      | 0.89   | 0.91     | 801     |
    | 1 | 0.36      | 0.48   | 0.41     | 104     |
    |   | Accuracy  |         | 0.84     | 905     |
    |   | Macro Avg | 0.64   | 0.68     | 0.66    | 905     |
    |   | Weighted Avg | 0.86 | 0.84  | 0.85    | 905     |

2. ADASYN

    |   | Precision | Recall | F1-Score | Support |
    |---|-----------|--------|----------|---------|
    | 0 | 0.94      | 0.91   | 0.92     | 801     |
    | 1 | 0.43      | 0.55   | 0.48     | 104     |
    |   | Accuracy  |         | 0.86     | 905     |
    |   | Macro Avg | 0.68   | 0.73     | 0.70    | 905     |
    |   | Weighted Avg | 0.88 | 0.86    | 0.87    | 905     |

I still saw the same problem of the model being biased towards the negative class. In my future works I listed some approach to deal with this problem:

1. Use a different data genearation technique. Possibly GAN based techniques for tabular data generation

2. Use a different model, like Random Forest classifier or Boosting methods like XGBoost or LightGBM

3. Use a different evaluation metric like AUC-ROC.

## Conclusion and Recommendations

From the analysis, I found out that the bank should focus on the following points:

- The bank should focus more on the month of May, november as they have lower convertion rate, raising them can increase the overall convertion rate, but also be active during the month of december

- The bank should focus on customers with marital status of divorced and single. The ideal customers are also students and retired people.

- The bank should not provide addtional effort on people who have personal loans.

- During cellular or telephone contact, the ideal duration of the call should be around 20-40 minutes.

- During a campaign, the ideal number of contacts made should be around 1 to 10.

- People who were contacted before a campaign has higher chance of getting converted.

- People who were contacted within a range of 3-6 mothns before a campaign has higher chance of getting converted.

- A successful campaing has a 64% chance of converting the customer according to the current data.
