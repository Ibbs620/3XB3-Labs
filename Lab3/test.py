from knapsack import *

kps = [ {'items': [(4,5),(3,4),(5,8),(2,3)], 'cap': 9, 'sol': 13},
        {'items': [(1,2),(3,5),(4,7),(7,8),(8,10)], 'cap': 10, 'sol': 14},
        {'items': [(1,1)], 'cap': 20, 'sol': 1},
        {'items': [(5, 10) ,(6, 12), (10, 20)], 'cap': 4, 'sol': 0},
        {'items': [(5, 10) ,(6, 12), (10, 20)], 'cap': 5, 'sol': 10} ]

# Add your function in here once its complete to test it
completed = [ks_rec]

for func in completed: 
    for i in range(len(kps)): 
        try:
            assert func(kps[i]['items'], kps[i]['cap']) == kps[i]['sol']
        except:
            print(func.__name__, "failed test case", i)
            break


