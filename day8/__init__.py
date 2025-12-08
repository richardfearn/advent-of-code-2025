import collections
from itertools import combinations
import math
from heapq import heappush, heappop

JunctionBox = collections.namedtuple("JunctionBox", ["x", "y", "z"])


def part_1_answer(lines, connections_to_make):
    connector = JunctionBoxConnector(lines)

    for _ in range(connections_to_make):
        connector.connect()

    sizes = connector.circuit_sizes()
    return math.prod(sizes[:3])


def part_2_answer(lines):
    connector = JunctionBoxConnector(lines)

    while True:
        box1, box2 = connector.connect()
        if connector.num_circuits() == 1:
            return box1.x * box2.x


class JunctionBoxConnector:

    def __init__(self, lines):
        self.junction_boxes = self._parse(lines)
        self.circuits = [{i} for i in range(len(self.junction_boxes))]
        self.distances = self._calculate_distances()

    @staticmethod
    def _parse(lines):
        boxes = [line.split(",") for line in lines]
        boxes = [(int(n) for n in box) for box in boxes]
        boxes = [JunctionBox(*box) for box in boxes]
        return boxes

    def _calculate_distances(self):
        distances = []
        for (i, box1), (j, box2) in combinations(enumerate(self.junction_boxes), 2):
            dist = self._distance(box1, box2)
            heappush(distances, (dist, (i, j)))
        return distances

    def connect(self):
        _, (i, j) = heappop(self.distances)
        c1, c2 = [self.which_circuit(n) for n in [i, j]]
        if c1 != c2:
            self.circuits[c1] |= self.circuits[c2]
            self.circuits.pop(c2)
        return [self.junction_boxes[n] for n in [i, j]]

    @staticmethod
    def _distance(a, b):
        return int(math.sqrt(((b.x - a.x) ** 2) + ((b.y - a.y) ** 2) + ((b.z - a.z) ** 2)))

    def which_circuit(self, box_num):
        return next(i for i, c in enumerate(self.circuits) if box_num in c)

    def circuit_sizes(self):
        return sorted([len(circuit) for circuit in self.circuits], reverse=True)

    def num_circuits(self):
        return len(self.circuits)
