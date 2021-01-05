class NodeData:

    def __init__(self, key: int, location: None):
        self.key = key
        self.location = location
        self.weight = 0.0
        self.info = ""
        self.tag = 0

    def get_key(self) -> int:
        return self.key

    def set_weight(self, w: double) -> None:
        self.weight = s

    def get_weight(self) -> double:
        return self.weight

