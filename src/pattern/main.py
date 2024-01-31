import argparse
import os
import csv

from graph import Operator, Task24PointEdge, Task24PointEdgeLabel, Task24PointGraph, Task24PointNode, Task24PointNodeLabel
import g_span

parser = argparse.ArgumentParser(description='Get graph inputs.')

parser.add_argument('--path')
parser.add_argument("--filename")

args = parser.parse_args()
graphs_file = []
if args.path:
    files = os.listdir(args.path)
    for path in files:
        node_path, edge_path = os.path.join(args.path, path, "node.csv"), os.path.join(args.path, path, "edge.csv")
        graphs_file.append((node_path, edge_path))

graphs = []
for node_path, edge_path in graphs_file:
    graph = Task24PointGraph()
    node_check = {}
    print(node_path)
    with open(file=node_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        node_cnt = 0
        for row in reader:
            expr, step, value = row["id"], int(row["step"]), float(row["value"]) if row["value"] else -1
            label = Task24PointNodeLabel(expr, step)
            node = Task24PointNode(node_cnt, value, label)
            node_check[expr] = node_cnt
            graph.add_node(node)
            node_cnt += 1
    
    print(edge_path)
    with open(file=edge_path, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row["Source"] == "null":
                continue
            src_str, dst_str = row["Source"], row["Target"]
            src, dst = node_check[src_str], node_check[dst_str]
            formula = row["last_formula"]
            op = None
            match row["operator"]:
                case '+':
                    op = Operator.Add
                case '-':
                    op = Operator.Sub
                case '*':
                    op = Operator.Mul
                case '/':
                    op = Operator.Div
            label = Task24PointEdgeLabel(formula, op)
            edge = Task24PointEdge(src, dst, label)
            graph.add_edge(edge)
    
    graph.display()
    graphs.append(graph)
    
g_span.save_data(graphs)
g_span.run_gSpan()
