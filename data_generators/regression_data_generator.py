from sklearn.datasets import make_regression
from sklearn.datasets import dump_svmlight_file
import os

def regression_generate_data(num_samples, num_features):
    
    # check if data_temp exists and if so delete it
    if os.path.exists('data_temp.libsvm'):
        os.remove('data_temp.libsvm')
    open('data_temp.libsvm', 'a').close()

    # empty the file before the new experiment
    if os.path.exists('data.libsvm'):
        os.remove('data.libsvm')
    open('data.libsvm', 'a').close()

    
    chunk_size = 3*(10**5)

     # check if num_samples is greater than 10**6 and if so create the dataset in chunks
    if num_samples > chunk_size:
        num_chunks = num_samples // chunk_size
        for i in range(num_chunks):
            print("creating chunk {} of {}".format(i+1,num_chunks))
            X, y = make_regression(n_samples=chunk_size, n_features=num_features)
            # overrides the existing data in the temp file
            dump_svmlight_file(X, y, 'data_temp.libsvm', zero_based=False)
            # concatenate the files 
            if i == 0:
                os.system("cat data_temp.libsvm >> data.libsvm")
            else:
                os.system("cat data_temp.libsvm >> data.libsvm")
                os.system("rm data_temp.libsvm")

        remainder = num_samples % chunk_size
        if remainder != 0:
            print("creating chunk {} of {}".format(num_chunks+1,num_chunks+1))
            X, y = make_regression(n_samples=remainder, n_features=num_features)
            dump_svmlight_file(X, y, 'data_temp.libsvm', zero_based=False)
            os.system("cat data_temp.libsvm >> data.libsvm")
            os.system("rm data_temp.libsvm")
        

        # write num_samples, num_features, num_labels and dataset_size to a file
        with open('data.libsvm.meta', 'w') as f:
            f.write('num_samples,{}\n'.format(num_samples))
            f.write('num_features,{}\n'.format(num_features))
            f.write('dataset_size,{}'.format(os.path.getsize('data.libsvm')/10**6))
            print("dataset size is: {} MB".format(os.path.getsize('data.libsvm')/10**6))
            f.close()
        return num_features, num_samples

    else:
        X, y = make_regression(n_samples=num_samples, n_features=num_features)
        dump_svmlight_file(X, y, 'data.libsvm', zero_based=False)
        # write num_samples, num_features, num_labels and dataset_size to a file
        with open('data.libsvm.meta', 'w') as f:
            f.write('num_samples,{}\n'.format(num_samples))
            f.write('num_features,{}\n'.format(num_features))
            f.write('dataset_size,{}'.format(os.path.getsize('data.libsvm')/10**6))
            print("dataset size is: {} MB".format(os.path.getsize('data.libsvm')/10**6))
            f.close()
            
        return num_features, num_samples

    
