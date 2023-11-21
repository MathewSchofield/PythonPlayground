import numpy as np

list = [[35, 53, 63], [72, 12, 22], [43, 84, 56]]
array = np.array(list)
new_col = [20, 30, 40]


print("before:\n", array)

print("\n",array[1])

array[1] = new_col


print("\nafter:\n", array)
