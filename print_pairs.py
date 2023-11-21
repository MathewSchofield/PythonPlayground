import numpy as np

'''Write a program to check and return the pairs of a given array A whose sum value is equal to a target value N.'''

def matching_pairs(arr, N):
    pairs = np.empty(shape = (len(arr), 2), dtype = int)
    hash_set = set()
    num_pairs = 0

    for idx in range(0, len(arr)):
        target = N - arr[idx]
  
        if (target in hash_set):
            print("Pairs " + str(arr[idx]) + ", " + str(target))
            pairs[num_pairs] = [arr[idx], target]
            num_pairs+=1

        hash_set.add(arr[idx])

    return pairs[0:num_pairs]

arr = [1, 4, 2, 0, 40, 3, 9, 4, 4]
N = 3

result = matching_pairs(arr, N)
print("result: ", result)

