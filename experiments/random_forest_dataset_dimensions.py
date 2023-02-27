import sys
import numpy as np

def random_forest_dimensions():
    num_samples = np.random.randint(10**2,10**6,size=1)
    num_features = np.random.randint(10**1,10**2,size=1)
    return {"num_samples": int(num_samples), "num_features": int(num_features)}

sys.modules[__name__] = random_forest_dimensions