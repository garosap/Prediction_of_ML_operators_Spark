import sys
import numpy as np

def clustering_dataset_dimensions():
    rows = np.random.randint(10**2,10**7,size=1)
    cols = np.random.randint(2,100,size=1)
    centers = np.random.randint(2,20,size=1)
    return {"num_samples": int(rows), "num_features": int(cols), "num_centers": int(centers)}

sys.modules[__name__] = clustering_dataset_dimensions