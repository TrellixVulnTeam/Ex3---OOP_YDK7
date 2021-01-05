class NodeData:

    def __init__(self, key: int, location: None):
        self.key = key
        self.location = location
        self.weight = 0.0
        self.info = ""
        self.tag = 0

    def __str__(self):
        return '(' + str(self.key) + ')'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.key == other.key and self.location == other.location

    def __lt__(self, other):
        t = other.tag - self.tag
        return self.tag < other.tag

    def __hash__(self):
        return self.key


    def get_key(self) -> int:
        return self.key

    def set_weight(self, w: double) -> None:
        self.weight = s

    def get_weight(self) -> double:
        return self.weight

