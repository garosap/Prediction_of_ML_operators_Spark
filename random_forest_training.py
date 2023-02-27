from data_generators import regression_data_generator as rdg
import measure_performance as mp
from experiments import random_forest_dataset_dimensions as random_forest_dimensions
from pyspark.storagelevel import StorageLevel
from spark_session import create_spark_session
from models import random_forest_regression as rfr

spark = create_spark_session()

# define the experiments
random_forest_dimensions = random_forest_dimensions()

# generate the data
num_features, num_samples = rdg.regression_generate_data(random_forest_dimensions['num_samples'], random_forest_dimensions['num_features'])

# Load the dataset
dataset = spark.read.format("libsvm").option("numFeatures", str(num_features)).load("data.libsvm")
dataset.persist(StorageLevel.MEMORY_AND_DISK)

# Define the k-means clustering model
random_forest = rfr.rf_model()

try:
    mp.measure_performance(random_forest, dataset, "./results/random_forest.csv")
    print("DONE")
    
    with open("exec_log_random_forest.txt", "a") as file:
        output = "DONE: num_features: {}, num_samples: {}\n".format(num_features, num_samples)
        file.write(output)
        file.close()
          

except Exception as e:
    print(e)
    with open("exec_log_random_forest.txt", "a") as file:
        output = "ERROR: num_features: {}, num_samples: {}\n".format(num_features, num_samples)
        file.write(output)
        file.close()



dataset.unpersist()
# free the memory
del random_forest
del num_features
del dataset
del random_forest_dimensions




