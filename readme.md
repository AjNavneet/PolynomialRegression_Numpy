## Overview

In this project, we aim to build a polynomial regression model for predicting the points scored by a sports team.

### Objective
- To predict points scored by a sports team using polynomial regression.

  ### Data Description
  The dataset contains information about the points scored by sports teams based on various attributes.

  ### Tech Stack
  - Language: Python
  - Libraries: pandas, numpy, scipy, matplotlib, seaborn, sklearn, statsmodel

---

### Approach

 1. **Data Preprocessing:**
         - Outlier removal
         - Imputing null values
         - One-hot encoding

  2. **Model Building:**
     - Linear regression model building

         Polynomial regression is a form of regression analysis that maps the relationship between the dependent variable and independent variable using an nth-degree polynomial. While linear regression works well for linear datasets, it may yield drastic results when applied to non-linear data. In such cases, polynomial regression is essential to capture the non-linear relationships in the data. Polynomial regression transforms the original features into polynomial features of the required degree and models them using a linear model.

      - Polynomial regression model building

  3. **Model Evaluation:**
         - Evaluating the model on test data
         - Discussion of various regression metrics like R-squared, AIC, AICC, F-statistics

      ---

      ### Modular Code Overview
      After unzipping the 'polynomial_regression.zip' file, you'll find the following folders:

      1. **Input**: Contains the data for analysis, in our case, the NBA dataset.
      2. **ML_Pipeline**: Includes all the functions organized in different Python files, appropriately named. These functions are called inside the `Engine.py` file.
      3. **Notebook**: Contains the Jupyter notebook file of the project.
      4. **Engine.py**: The script to run the code.
      5. **Readme.md**: Instructions for running the code.
      6. **requirements.txt**: Lists all the required libraries with their respective versions. Install them using `pip install -r requirements.txt`.

---
### Project Structure

      - Root
         - Input
            - NBA dataset csv.csv
         - MLPipeline
            - I_kuma_utils
            - I_Model.py
            - __Preprocessing.py
         - Notebook
            - Regression_Splines.ipynb
            - Engine.py
            - Readme.md
            - requirements.txt


---
   

      ### Takeaways
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
