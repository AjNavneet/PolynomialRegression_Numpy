import pandas as pd
import projectpro
import warnings
from ML_Pipeline.Preprocessing import Preprocessing
from ML_Pipeline.Model import Regression
from ML_Pipeline.kuma_utils.preprocessing.imputer import LGBMImputer

# Ignore warnings
warnings.filterwarnings("ignore")

# Load the dataset
data = pd.read_csv('Input/NBA_Dataset_csv.csv')

# Remove outliers
target_col = 'Points_Scored'  # Target column name
df = Preprocessing(data).remove_outlier(target_col)

# Train-test split of data
target_col = 'Points_Scored'  # Target column name
X_train, X_test, y_train, y_test = Preprocessing(df).split_data(target_col)

# One-hot encoding of train and test data
X_train, X_test = Preprocessing(df).onehot_encode(X_train, X_test)

# LGBM imputer for missing value imputation
X_train, X_test = Preprocessing(df).lgbm_imputer(X_train, X_test)

# Polynomial regression model building
degree_of_poly = 1  # Degree of polynomial
y_pred = Regression().polynomial_regression(X_train, X_test, y_train, y_test, degree_of_poly)

# Save checkpoint
projectpro.checkpoint('78ae27')

# Calculate and display metrics
Regression().metrics(y_test, y_pred)
