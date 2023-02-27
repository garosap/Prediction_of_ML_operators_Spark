from pyspark.ml.clustering import KMeans

def kmeans_model(num_centers):
    # Define the k-means clustering model
    kmeans = KMeans().setK(num_centers).setSeed(1).setInitMode("k-means||").setMaxIter(10)
    return kmeans