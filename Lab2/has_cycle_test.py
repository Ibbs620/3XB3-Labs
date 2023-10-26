from graph import *

# A simple graph with a cycle
def test_case_1():
    G = Graph(4)
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 0)
    
    assert has_cycle(G) == True, "Test Case 1 Failed"

# A tree structure (acyclic graph)
def test_case_2():
    G = Graph(4)
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    
    assert has_cycle(G) == False, "Test Case 2 Failed"

# A disconnected graph with one component having a cycle
def test_case_3():
    G = Graph(5)
    G.add_edge(0, 1)
    G.add_edge(1, 2)
    G.add_edge(2, 0)
    # The graph has another component with nodes 3 and 4 which are disconnected from the main graph and from each other
    
    assert has_cycle(G) == True, "Test Case 3 Failed"

def run_tests():
    test_case_1()
    test_case_2()
    test_case_3()
    print("All Test Cases Passed!")

run_tests()
