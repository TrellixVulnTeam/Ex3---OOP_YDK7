from dataclasses import dataclass, field
from src.node import NodeData


@dataclass(order=True)
class PriorityNode:
    priority: float
    item: NodeData = field(compare=False)

    def __init__(self, weight: float, node: NodeData):
        self.priority = weight
        self.item = node

    def get_item(self) -> NodeData:
        return self.item