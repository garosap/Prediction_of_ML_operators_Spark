# import word2vec from pyspark and create a word2vec model
from pyspark.mllib.feature import Word2Vec

def word2vec_model():
    word2vec = Word2Vec()
    return word2vec
