# Creates a dictionary for storing results
def initialize_results(x_axis):
    return {x: [] for x in x_axis}


# Prints results of a test
def print_results(title, results, axis_title):
    print("-" * 20, title, "-" * 20)
    print(f"{axis_title}\t\tResult")
    for value, data in results.items():
        data = [round(x, 6) for x in data]
        print(f"{value}\t\t{data}")
    print()