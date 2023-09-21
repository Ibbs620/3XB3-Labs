import bad_sorts as bs

swaps = [10, 50, 100, 500, 1000, 5000]
list_length = 1000
max_value = 50000
results = {algo.__name__: [] for algo in [ bs.bubble_sort2]}
num_runs = 10

# for swap in swaps:
#     for algorithm in [ bs.bubble_sort2]:
#         runtimes = [] #empty list for storing runtimes
#         for _ in range(num_runs):
#             L = bs.create_near_sorted_list(list_length,max_value,swap)
#             runtime = bs.measure_runtime(algorithm, L.copy())
#             runtimes.append(runtime)  #adding to runtime list
#         results[algorithm.__name__].append(runtimes)


# print("Swaps Bubble Sort 2")
# for i, swap in enumerate(swaps):
#     selection = results["bubble_sort2"][i]
#     print(f"{swap}\t\t{selection}")

mylist = [0.03799843788146973, 0.03500175476074219, 0.02299642562866211, 0.022001266479492188, 0.016999006271362305, 0.025000810623168945, 0.021001815795898438, 0.022999048233032227, 0.02400064468383789, 0.030998706817626953]
for l in mylist:
    print(l)

# 10              [0.03799843788146973, 0.03500175476074219, 0.02299642562866211, 0.022001266479492188, 0.016999006271362305, 0.025000810623168945, 0.021001815795898438, 0.022999048233032227, 0.02400064468383789, 0.030998706817626953]
# 50              [0.027997970581054688, 0.03800010681152344, 0.02909564971923828, 0.022086381912231445, 0.024007797241210938, 0.025989770889282227, 0.027981996536254883, 0.025966405868530273, 0.02707839012145996, 0.02800130844116211]
# 100             [0.025997161865234375, 0.024019479751586914, 0.023086071014404297, 0.02691197395324707, 0.02791571617126465, 0.026923179626464844, 0.03008890151977539, 0.029910564422607422, 0.025056123733520508, 0.02899909019470215]
# 500             [0.04699826240539551, 0.049001216888427734, 0.04799938201904297, 0.04799675941467285, 0.04904890060424805, 0.041933298110961914, 0.04199862480163574, 0.03800058364868164, 0.04099893569946289, 0.044069528579711914]
# 1000            [0.04801654815673828, 0.04492831230163574, 0.04300093650817871, 0.04400277137756348, 0.04599428176879883, 0.04708051681518555, 0.04901576042175293, 0.04190492630004883, 0.042957305908203125, 0.04499459266662598]