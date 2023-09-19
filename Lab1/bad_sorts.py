"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import time


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


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# Bubble sort 2
def bubble_sort2(L):
    n = len(L)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                swap(L, j, j+1)
                swapped = True
        if not swapped:
            break

# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index


#******************TESTING**********************************
#******************TESTING**********************************
#******************TESTING**********************************
#******************TESTING**********************************


def measure_runtime(sorting_algorithm, L):
    start_time = time.time()
    sorting_algorithm(L)
    end_time = time.time()
    return end_time - start_time

list_lengths = [100,500,1000,2000,5000,10000]
num_runs = 10
num_runs = 10
max_value = 50000
results = {algo.__name__: [] for algo in [insertion_sort, bubble_sort, selection_sort]}

# for length in list_lengths:
#     for algorithm in [insertion_sort, bubble_sort, selection_sort]:
#         runtimes = [] #empty list for storing runtimes
#         for _ in range(num_runs):
#             L = create_random_list(length, max_value)
#             runtime = measure_runtime(algorithm, L.copy())
#             runtimes.append(runtime)  #adding to runtime list
#         results[algorithm.__name__].append(runtimes)


# print("List Length\tInsertion Sort\tBubble Sort\tSelection Sort")
# for i, length in enumerate(list_lengths):
#     insertion_mean = sum(results["insertion_sort"][i]) / num_runs
#     bubble_mean = sum(results["bubble_sort"][i]) / num_runs
#     selection_mean = sum(results["selection_sort"][i]) / num_runs
#     print(f"{length}\t\t{insertion_mean:.6f}\t\t{bubble_mean:.6f}\t\t{selection_mean:.6f}")