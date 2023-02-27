from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from data_generators import clustering_data_generator as cdg
import measure_performance as mp
from experiments import clustering_dataset_dimensions as clustering_dataset_dimensions 
from models import kmeans as km
import os
import logging
import gc
import psutil
from pyspark.storagelevel import StorageLevel
import sys
from spark_session import create_spark_session
import time

# define the clustering dimensions
clustering_dimensions = clustering_dataset_dimensions()

spark = create_spark_session()


# generate the data
num_features,num_centers,num_samples = cdg.clustering_generate_data(clustering_dimensions['num_samples'], clustering_dimensions['num_features'], clustering_dimensions['num_centers'])

# Load the dataset
dataset = spark.read.format("libsvm").option("numFeatures", str(num_features)).load("data.libsvm")
dataset.persist(StorageLevel.MEMORY_AND_DISK)

# create the model
kmeans = km.kmeans_model(num_centers)

try:
    mp.measure_performance(kmeans, dataset, "./results/kmeans.csv")
    
    with open("exec_log_kmeans.txt", "a") as file:
        output = "DONE: samples: {}, features: {}, centers: {}\n".format(num_samples, num_features, num_centers)
        file.write(output)
        file.close()
          

except Exception as e:
    with open("exec_log_kmeans.txt", "a") as file:
        output = "ERROR: samples: {}, features: {}, centers: {}\n".format(num_samples, num_features, num_centers)
        file.write(output)
        file.close()

dataset.unpersist()
# free the memory
del kmeans
del num_features
del num_centers
del dataset


