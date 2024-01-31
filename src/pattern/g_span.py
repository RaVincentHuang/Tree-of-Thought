from graph import Task24PointGraph
import os
from gspan_mining.config import parser
from gspan_mining.main import gSpan

def save_data(graphs: list[Task24PointGraph]):
    with open('.graph.data', 'w') as file:
        for i in range(len(graphs)):
            print("t # {}".format(i), file=file)
            
            graph = graphs[i]
            for node in graph.node:
                print("v {} 1".format(node.id), file=file)
            for edge in graph.edge:
                print("e {} {} 1".format(edge.src, edge.dst), file=file)
        print("t # -1", file=file)
    
def run_gSpan():
    # args_str = '-s 5000 -d True -l 3 -u 8 -p True -w True .graph.data'
    # # flags, _ = parser.parse_known_args(args=args_str.split())
    
    
    gs = gSpan(".graph.data", 10, 3, 10, visualize=False, where=True, is_undirected=False, verbose=True)
    gs.run()
    gs.time_stats()
    
    # for g in gs.graphs.values():
    #     g.plot()
    
    