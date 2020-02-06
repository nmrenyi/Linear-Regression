# class c(object):
#     def __init__(self):
#         self.name = 'ry'

# def t(x):
#     x.name = 'I'

# x = c()
# print(x.name)
# t(x)
# print(x.name)

# def getNumber(f):
#     s = f.readline()
#     s = s.split(' ')
#     s[-1] = s[-1].replace('\n', '')
#     return [float(x) for x in s]
# with open('data.txt', 'r') as f:
#     coef, bias = getNumber(f)
#     data_x = getNumber(f)
#     data_y = getNumber(f)

from sklearn import datasets
import numpy as np
bias = np.random.randint(-10, 11)

data_x, data_y, coef = datasets.make_regression(n_samples = 500,n_features = 1,n_targets = 1, bias = bias,noise = 3, coef=True) # TODO checkout parametres of the dataset
data_x = [x[0] for x in data_x]

with open('data.txt', 'w') as f:
    f.write(str(coef) + ' ' + str(bias) + '\n')
    f.write(' '.join([str(x) for x in data_x]) + '\n')
    f.write(' '.join([str(y) for y in data_y]) + '\n')