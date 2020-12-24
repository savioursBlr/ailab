
#from queuelib import FifoDiskQueue
#qfactory = lambda priority: FifoDiskQueue('queue-dir-%s' % priority)
import colorama
from colorama import Fore, Back, Style

# A simple implementation of Priority Queue 
# using Queue.
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[float, tuple]] = []

    def __str__(self): 
        return self.elements

    def empty(self) -> bool:
        return len(self.elements) == 0
    
    def put(self, item: tuple, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self) -> tuple:
        return heapq.heappop(self.elements)[1]
''' 
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self,i): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == 0
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i] > self.queue[max]: 
                    max = i 
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            print() 
            exit()
    
'''

# HELPER
def visualize(frontier):
    colorama.init()
    for i in range(len(frontier.elements)):
        text = str(frontier.elements[i])
        if i == 0:
            print(Back.RED + Fore.WHITE + text + Style.RESET_ALL)
        else:
            print(text)
    print()

def build_graph_weighted(file):
    """Builds a weighted, undirected graph"""
    graph = {}
    for line in file:
        v1, v2, w = line.split(',')
        v1, v2 = v1.strip(), v2.strip()
        w = int(w.strip())
        if v1 not in graph:
            graph[v1] = []
        if v2 not in graph:
            graph[v2] = []
        graph[v1].append((v2,w))
        graph[v2].append((v1,w))
    return graph

# Helper methods for A*
def build_heuristic_dict():
    h = {}
    with open("sld_to_bucharest.txt", 'r') as file:
        for line in file:
            line = line.strip().split(",")
            node = line[0].strip()
            sld = int(line[1].strip())
            h[node] = sld
    return h

def heuristic(node, values):
    return values[node]

# A* search
def a_star(graph, start, dest, visualization=False):
    """Performs a* search on graph 'graph' with
        'start' as the beginning node and 'dest' as the goal.
        Returns shortest path from 'start' to 'dest'.
        If 'visualization' is set to True, then progress of
        algorithm is shown."""

    frontier = PriorityQueue()

    # uses helper function for heuristics
    h = build_heuristic_dict()

    # path is a list of tuples of the form ('node', 'cost')
    frontier.put([(start, 0)], 0)
    explored = set()

    while not frontier.empty():

        # show progress of algorithm
        if visualization:
            visualize(frontier)

        # shortest available path
        path = frontier.get()

        # frontier contains paths with final node unexplored
        node = path[-1][0]
        g_cost = path[-1][1]
        explored.add(node)

        # goal test:
        if node == dest:
            # return only path without cost
            return [x for x, y in path]

        for neighbor, distance in graph[node]:
            cumulative_cost = g_cost + distance
            f_cost = cumulative_cost + heuristic(neighbor, h)
            new_path = path + [(neighbor, cumulative_cost)]

            # add new_path to frontier
            if neighbor not in explored:
                frontier.put(new_path, f_cost)

            # update cost of path in frontier
            elif neighbor in frontier.elements:
                frontier.put(new_path, f_cost)
                print(path)
    return False

with open('Graph.txt', 'r') as file:
    lines = file.readlines()

start = lines[1].strip()
dest = lines[2].strip()
graph = build_graph_weighted(lines[4:])
print(a_star(graph, start, dest, True), "\n\n")