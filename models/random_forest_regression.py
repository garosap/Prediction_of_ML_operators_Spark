from pyspark.ml import Pipeline
from pyspark.ml.regression import RandomForestRegressor

def rf_model():
    rf = RandomForestRegressor()
    return rf
    