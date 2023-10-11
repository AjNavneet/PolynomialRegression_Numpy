# Polynomial Regression Model for Predicting Sports Team Points

## Overview

In this project, we aim to build a polynomial regression model for predicting the points scored by a sports team.

### Objective

- To predict points scored by a sports team using polynomial regression.

## Data Description

The dataset contains information about the points scored by sports teams based on various attributes.

## Tech Stack

- Language: Python
- Libraries: `pandas`, `numpy`, `scipy`, `matplotlib`, `seaborn`, `scikit-learn`, `statsmodels`

## Approach

1. **Data Preprocessing:**
    - Outlier removal
    - Imputing null values
    - One-hot encoding

2. **Model Building:**
    - Linear regression model building
    - Polynomial regression model building

3. **Model Evaluation:**
    - Evaluating the model on test data
    - Discussion of various regression metrics like R-squared, AIC, AICC, F-statistics

## Project Structure
```
- Root
  - Input
    - `NBA_dataset.csv`
  - MLPipeline
    - I_kuma_utils
    - I_Model.py
    - __Preprocessing.py
  - Notebook
    - `Regression_Splines.ipynb`
    - `Engine.py`
    - `Readme.md`
    - `requirements.txt`
 ```

## Takeaways

1. Understanding distribution plots.
2. Knowing how to create box plots.
3. Understanding violin plots.
4. Detecting outliers in data.
5. Methods to treat outliers.
6. Familiarity with pandas imputer.
7. Understanding iterative imputer.
8. Knowledge of KNN imputer.
9. Exploring LGBM imputer.
10. Univariate analysis.
11. Chatterjee correlation.
12. Understanding ANOVA.
13. Implementation of ANOVA.
14. Data preprocessing techniques.
15. Awareness of AIC (Akaike Information Criterion).
16. Understanding likelihood in statistical modeling.
