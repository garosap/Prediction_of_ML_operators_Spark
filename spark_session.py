from pyspark.sql import SparkSession

def create_spark_session():
    """Create a spark session"""
    spark = SparkSession.builder.master("spark://192.168.0.2:7077").config("spark.executor.memory", "2000m")\
        .config("spark.executor.cores", "2")\
        .config("spark.driver.memory", "3g")\
        .config("spark.cleaner.periodicGC.interval", "1min")\
        .appName("K-Means").getOrCreate()
    return spark
