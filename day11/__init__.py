OUT = "out"


def part_1_answer(lines):
    rack = ServerRack(lines)
    return rack.paths_between("you", OUT)


def part_2_answer(lines):
    rack = ServerRack(lines)

    svr, dac, fft = "svr", "dac", "fft"

    svr_dac = rack.paths_between(svr, dac)
    svr_fft = rack.paths_between(svr, fft)
    dac_fft = rack.paths_between(dac, fft)
    fft_dac = rack.paths_between(fft, dac)
    dac_out = rack.paths_between(dac, OUT)
    fft_out = rack.paths_between(fft, OUT)

    return (svr_dac * dac_fft * fft_out) + (svr_fft * fft_dac * dac_out)


class ServerRack:

    def __init__(self, lines):
        self.connections = self.parse(lines)
        self.num_paths_cache = {}

    @staticmethod
    def parse(lines):
        connections = {}
        for line in lines:
            device, outputs = line.split(": ")
            connections[device] = outputs.split(" ")
        return connections

    def paths_between(self, source, dest):
        key = (source, dest)

        if key not in self.num_paths_cache:
            self.num_paths_cache[key] = self.calculate_paths_between(source, dest)

        return self.num_paths_cache[key]

    def calculate_paths_between(self, source, dest):
        if source == OUT:
            return 0

        children = self.connections[source]

        if dest in children:
            return 1

        return sum(self.paths_between(child, dest) for child in children)
