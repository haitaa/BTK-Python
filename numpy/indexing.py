import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[::-1]

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numbers2[0,2]
result = numbers2[:,2]


print(result)