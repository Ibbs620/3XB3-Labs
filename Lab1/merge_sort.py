
import time
import random

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

# *************************************

#******************TESTING**********************************
#******************TESTING**********************************
#******************TESTING**********************************
#******************TESTING**********************************


def measure_runtime(sorting_algorithm, L):
    start_time = time.time()
    sorting_algorithm(L)
    end_time = time.time()
    return end_time - start_time

list_lengths = [500, 1000, 2000, 5000, 10000, 50000]
num_runs = 10
max_value = 50000
results = {algo.__name__: [] for algo in [ mergesort]}

for length in list_lengths:
    for algorithm in [ mergesort]:
        runtimes = [] #empty list for storing runtimes
        for _ in range(num_runs):
            L = create_random_list(length, max_value)
            runtime = measure_runtime(algorithm, L.copy())
            runtimes.append(runtime)  #adding to runtime list
        results[algorithm.__name__].append(runtimes)


print("List Length merge Sort")
for i, length in enumerate(list_lengths):
    selection = results["mergesort"][i]
    print(f"{length}\t\t{selection}")
