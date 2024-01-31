from typing import List, TypeVar, Generic
import numpy
from enum import Enum

class Label:
    def __init__(self) -> None:
        self.embedding = numpy.array([])
        
    def getEmbedding():
        pass
    
    def __repr__(self) -> str:
        return "Label:"

class Operator(Enum):
    Add = 1
    Sub = 2
    Mul = 3
    Div = 4

class Task24PointEdgeLabel(Label):
    def __init__(self, last_formula: list[int], operator: Operator) -> None:
        super().__init__()
        self.last_formula: list[int] = last_formula
        self.operator: Operator = operator
        
    def __repr__(self) -> str:
        return super().__repr__() + "last_formula: {}, operator: {}".format(self.last_formula, self.operator)

class Task24PointNodeLabel(Label):
    def __init__(self, calc_expr: str, step: int) -> None:
        super().__init__()
        self.calc_expr: str = calc_expr
        self.step: int = step
        # self.value: float = value
    
    def __repr__(self) -> str:
        return super().__repr__() + "calc_expr: {}, step: {}".format(self.calc_expr, self.step)
   
class ThoughtEdge:
    def __init__(self, src: int, dst: int, label: Label = None) -> None:
        self.src: int = src
        self.dst: int = dst
        self.label: Label = label
    
    def __repr__(self) -> str:
        return "{} -> {} ({})".format(self.src, self.dst, self.label)

class ThoughtNode:
    def __init__(self, id, label: Label = None) -> None:
        self.id: int = id
        self.label: Label = label
    
    def __repr__(self) -> str:
        return "{} ({})".format(self.id, self.label)
        
class Task24PointEdge(ThoughtEdge):
    def __init__(self, src: int, dst: int, label: Task24PointEdgeLabel) -> None:
        super().__init__(src, dst, label)
        
    def __repr__(self) -> str:
        return super().__repr__()
        
class Task24PointNode(ThoughtNode):
    def __init__(self, id, value: float, label: Task24PointNodeLabel = None) -> None:
        super().__init__(id, label)
        self.value: float = value
        
    def __repr__(self) -> str:
        return super().__repr__() + " := {}".format(self.value)

NodeType = TypeVar('NodeType')
EdgeType = TypeVar('EdgeType')

# class Graph(Generic[NodeType], Generic[EdgeType]):
#     def __init__(self) -> None:
#         self.node: List[NodeType] = []
#         self.edge: List[EdgeType] = []
    
#     def add_node(self, node: NodeType):
#         self.node.append(node)
    
#     def add_edge(self, edge: EdgeType):
#         self.edge.append(edge)

class Task24PointGraph:
    def __init__(self) -> None:
        self.node: list[Task24PointNode] = []
        self.edge: list[Task24PointEdge] = []
    
    def add_node(self, node: Task24PointNode):
        self.node.append(node)
    
    def add_edge(self, edge: Task24PointEdge):
        self.edge.append(edge)

    def display(self):
        for node in self.node:
            print(node)
        
        for edge in self.edge:
            print(edge)