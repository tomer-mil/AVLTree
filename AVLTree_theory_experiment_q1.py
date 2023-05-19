from AVLTree_theory import AVLTree, AVLNode
import random

# create descending order array
def create_desc_arr(i):
    arr = []
    n = 1500*(2**i)
    print(n)
    for i in range(n, 0, -1):
        arr.append(i)
    return arr

# shuffle array
def shuffle_array(arr):
    random.shuffle(arr)
    return arr

# create an almost-descending order array
def create_almost_desc_arr(i):
    arr = []
    sub_array = []
    n = 1500*(2**i)
    print(n)
    for i in range(1, n):
        if i <= 300:
            arr.append(i)
            if i == 300:
                arr.reverse()
        else:
            sub_array.append(i)
        if len(sub_array) == 300:
            sub_array.reverse()
            arr += sub_array
            sub_array = []
    sub_array.reverse()
    arr += sub_array
    return arr

# THEORY QUESTION NUMBER 1
print("i=", 3)
print("descending order for i=1")
arr = create_desc_arr(5)
#arr=[9,8,7,6,5,4,3,2,1]
#arr = create_almost_desc_arr(5)
#arr = shuffle_array(arr)
print("################################")
print("not sorted array:")
print(arr)
print("################################")
tree = AVLTree()
# arr=[9,8,7,6,5,4,3,2,1]
sorting_cost, swap_operations_counter, search_operations_counter, balancing_counter = 0, 0, 0, 0
for key in arr:
    key_balance_actions, key_swap_operations_counter, key_search_operations_counter = tree.insert(key=key, val="")
    sorting_cost += (key_balance_actions + key_search_operations_counter)
    swap_operations_counter += key_swap_operations_counter
    search_operations_counter += key_search_operations_counter
    balancing_counter += key_balance_actions

print(f"swaps number: {swap_operations_counter}")
print(f"sorting cost: {sorting_cost}")
print(f"* for my personal info: searches number: {search_operations_counter}")
print(f"balancing operations: {balancing_counter}")
print("################################")

  


