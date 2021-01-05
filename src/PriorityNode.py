from dataclasses import dataclass, field
from typing import Any
from src.node import NodeData


@dataclass(order=True)
class PriorityNode:
    priority: double
    item: NodeData = field(compare=False)

    def __init__(self, weight: double, node: NodeData):
        self.priority = weight
        self.item = node

    def get_item(self) -> NodeData:
        return self.item
