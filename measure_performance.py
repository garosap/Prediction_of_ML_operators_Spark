
import gc
import time
import psutil
import csv
from pyspark.storagelevel import StorageLevel
from sparkmeasure import StageMetrics

import requests
import json

# Get the Spark application ID
def get_app_id():
    response = requests.get("http://83.212.81.54:4040/api/v1/applications")
    applications = json.loads(response.text)
    app_id = applications[0]["id"]
    return app_id

# Get the executor summary
def get_executor_summary(app_id):
    response = requests.get(f"http://83.212.81.54:4040/api/v1/applications/{app_id}/executors")
    executors = json.loads(response.text)
    return executors

# Calculate the average CPU usage
def get_average_cpu_usage(executors):
    total_cpu = 0
    for executor in executors:
        print
        total_cpu += executor["totalCores"]
    average_cpu = total_cpu / len(executors)
    return average_cpu

# Calculate the total memory usage
def get_total_memory_usage(executors):
    total_memory = 0
    for executor in executors:
        total_memory += executor["memoryUsed"]
    return total_memory

# get the total time
def get_total_time(executors):
    total_time = 0
    for executor in executors:
        total_time += executor["totalDuration"]
    return total_time


def measure_performance(model, dataset, file):
    # Start a process to measure the CPU and memory usage
    process = psutil.Process()

    start_time = time.time()

    # Fit the model to the dataset
    model.fit(dataset)

    end_time = time.time()
    total_time = end_time - start_time


    app_id = get_app_id()
    executors = get_executor_summary(app_id)

    # Get the total memory from all the executors
    memory_usage = get_total_memory_usage(executors)

    # Read the values from the data.libsvm.meta file
    with open("data.libsvm.meta", "r") as meta_file:
        reader = csv.DictReader(meta_file, fieldnames=["key", "value"], delimiter=",")
        meta_values = {}
        for row in reader:
            meta_values[row["key"]] = row["value"]

    # Write the performance statistics to the file
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        # Write the headers if the file is empty
        if f.tell() == 0:
            writer.writerow(["Total Time","Memory Usage"] + list(meta_values.keys()))
        writer.writerow([total_time, memory_usage] + list(meta_values.values()))

    # free up memory
    del model
    del dataset
    del process
    del meta_values
    

    
    