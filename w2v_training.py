from data_generators import w2v_data_generator as w2v_gen
import measure_performance as mp
from experiments import w2v_dataset_dimensions as w2v_dataset_dimensions
from pyspark.storagelevel import StorageLevel
from spark_session import create_spark_session
from models import w2v as w2v

spark = create_spark_session()

# define the experiments
word2vec_dimensions = w2v_dataset_dimensions()

# generate the data
num_features,num_samples = w2v_gen.w2v_generate_data(word2vec_dimensions['num_samples'], word2vec_dimensions['num_features'])

# Load the dataset from w2v_dataset.csv
dataset = spark.read.csv("w2v_dataset.csv", header=False, inferSchema=True)

dataset.persist(StorageLevel.MEMORY_AND_DISK)

rdd = dataset.rdd

# Convert each row of the DataFrame to a list of strings
rdd = rdd.map(lambda x: [str(i) for i in x])


# Define the word2vec clustering model
word2vec = w2v.word2vec_model()

try:
    mp.measure_performance(word2vec, rdd, "./results/word2vec.csv")
    print("DONE")
    
    with open("exec_log_word2vec.txt", "a") as file:
        output = "DONE: num_features: {}, num_samples: {}\n".format(num_features,num_samples)
        file.write(output)
        file.close()
          

except Exception as e:
    print(e)
    with open("exec_log_word2vec.txt", "a") as file:
        output = "ERROR: num_features: {}, num_samples: {}\n".format(num_features,num_samples)
        file.write(output)
        file.close()



dataset.unpersist()
# free the memory
del word2vec
del num_features
del dataset
del word2vec_dimensions




