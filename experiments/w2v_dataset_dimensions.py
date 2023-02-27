import sys
import numpy as np

def w2v_dataset_dimensions():
    num_samples = np.random.randint(10**2,5*(10**6),size=1)
    num_features = np.random.randint(3,50,size=1)
    return {"num_samples": int(num_samples), "num_features": int(num_features)}

sys.modules[__name__] = w2v_dataset_dimensions