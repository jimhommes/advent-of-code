import re


class PuzzleRange:

    def __init__(self, dest, src, rng):
        self.dest_start = dest
        self.src_start = src
        self.dest_stop = dest + rng - 1
        self.src_stop = src + rng - 1
        self.offset = dest - src
        self.range_length = rng
        self.si = 0

    def update_back(self, item):
        if item.src_start == 25 and self.src_stop == 97:
            pass  # Debug break

        if item.src_start <= self.dest_start and item.src_stop >= self.dest_stop:
            # Update Type 1
            return [[], [PuzzleRange(item.translate_value(self.dest_start), self.src_start, self.range_length)]]

        elif item.src_start < self.dest_start and self.dest_start <= item.src_stop <= self.dest_stop:
            # Update Type 2
            res = []

            if self.dest_stop - item.src_stop > 0:
                res.append(PuzzleRange(item.src_stop, self.src_start + item.src_stop - self.dest_start + 1,
                                       self.dest_stop - item.src_stop))

            return [res,
                    [PuzzleRange(item.translate_value(self.dest_start), self.src_start,
                                 item.src_stop - self.dest_start + 1)]]

        elif self.dest_start <= item.src_start <= self.dest_stop and item.src_stop > self.dest_stop:
            # Update Type 3
            res = []
            if item.src_start - self.dest_start > 0:
                res += [PuzzleRange(self.dest_start, self.src_start, item.src_start - self.dest_start)]

            return [res, [PuzzleRange(item.dest_start, self.src_stop - (self.dest_stop - item.src_start),
                                      self.dest_stop - item.src_start + 1)]]

        elif item.src_start >= self.dest_start and item.src_stop <= self.dest_stop:
            # Update Type 4
            res = []
            if item.src_start - self.dest_start > 0:
                res += [PuzzleRange(self.dest_start, self.src_start, item.src_start - self.dest_start)]

            if self.range_length - (item.src_start - self.dest_start) - item.range_length > 0:
                res += [PuzzleRange(self.dest_start + (item.src_start - self.dest_start) + item.range_length,
                                    item.src_stop + 1 - self.offset,
                                    self.range_length - (item.src_start - self.dest_start) - item.range_length)]

            return [res, [
                PuzzleRange(item.dest_start, self.src_start + (item.src_start - self.dest_start), item.range_length)]]

        else:
            # No touch
            return [[self], []]

    def update(self, item):
        rest_parts = []
        mapped_parts = []

        # Determine rest parts
        if self.dest_start < item.src_start:
            # There is a left part
            rest_parts += [
                PuzzleRange(self.dest_start, self.src_start, min(self.range_length, item.src_start - self.dest_start))]

        if self.dest_stop > item.src_stop:
            # There is a right part
            src_start = max(self.src_start, item.src_stop + 1 - self.offset)
            range_length = min(self.range_length, self.src_stop - (item.src_stop + 1 - self.offset) + 1)
            rest_parts += [PuzzleRange(self.translate_value(src_start),
                                       src_start,
                                       range_length)]

        # Determine mapped parts
        # if self.dest_start <= item.src_start <= self.dest_stop or self.dest_start <= item.src_stop <= self.dest_stop or (item.src_start <= self.dest_stop and item.src_stop >= self.dest_start):
        if item.src_start <= self.dest_stop and item.src_stop >= self.dest_start:
            src_start = max(self.src_start, item.src_start - self.offset)
            src_stop = min(self.src_stop, item.src_stop - self.offset)
            dest_start = item.translate_value(self.translate_value(src_start))
            range_length = min(self.range_length, src_stop - src_start + 1)
            mapped_parts.append(PuzzleRange(dest_start, src_start, range_length))

        return [rest_parts, mapped_parts]

    def calc_stops(self):
        self.dest_stop = self.dest_start + self.range_length - 1
        self.src_stop = self.src_start + self.range_length - 1

    def translate_value(self, value):
        return value + self.offset

    def __contains__(self, item):
        return self.src_start <= item <= self.src_stop

    def __repr__(self):
        return 'Range(src:' + str(self.src_start) + ':' + str(self.src_stop) + ',dest:' \
            + str(self.dest_start) + ':' + str(self.dest_stop) + ')'


class PuzzleMap:

    def __init__(self):
        self.ranges = []

    def update(self, input_map):
        for rng in self.ranges:
            rng.si = rng.dest_start
        for rng in input_map.ranges:
            rng.si = rng.src_start

        self.ranges = sorted(self.ranges, key=lambda x: x.si)
        input_map.ranges = sorted(input_map.ranges, key=lambda x: x.si)
        res_ranges = []
        own_ranges = self.ranges[:]
        while len(own_ranges) > 0:
            own_rng = own_ranges.pop(0)
            for other_rng in input_map.ranges:
                updated = own_rng.update(other_rng)
                res_ranges += updated[1]
                if len(updated[0]) == 0:
                    own_rng = None
                    break
                own_rng = updated[0][0]
                if len(updated[0]) > 1:
                    own_ranges.append(updated[0][1])
            if own_rng is not None:
                res_ranges.append(own_rng)
        self.ranges = res_ranges

    def add_range(self, input_range):
        self.ranges.append(input_range)

    def translate_value(self, value):
        for puzzle_range in self.ranges:
            if value in puzzle_range:
                return puzzle_range.translate_value(value)
        return value

    def __repr__(self):
        return str(sorted(self.ranges, key=lambda x: x.src_start))


with open('input/5.txt') as f:
    lines = f.readlines()

# Load all maps
puzzlemaps = []
curr_map = None
for line in lines[2:]:
    if line.strip() == '':
        pass
    elif not line[0].isnumeric():
        curr_map = PuzzleMap()
        puzzlemaps.append(curr_map)
    else:
        spl = line.strip().split(' ')
        curr_map.add_range(PuzzleRange(int(spl[0]), int(spl[1]), int(spl[2])))

# Reduce to 1 map
master_map = PuzzleMap()
master_map.add_range(PuzzleRange(0, 0, float('inf')))
starting_seeds = [int(el) for el in re.findall(r'\d+', lines[0])]
print('Exercise 1')
print('Starting seeds: ' + str(starting_seeds))

for pmp in puzzlemaps:
    master_map.update(pmp)

end_locations = [master_map.translate_value(x) for x in starting_seeds]
print('Translated seeds: ' + str(end_locations))
print('Exercise 1 Final Answer: ' + str(min(end_locations)))

end_locations = []
ex2_map = PuzzleMap()
for i in range(0, len(starting_seeds), 2):
    ex2_map.add_range(PuzzleRange(int(starting_seeds[i]), int(starting_seeds[i]), int(starting_seeds[i+1])))


print('Exercise 2')
print('Starting map: ' + str(ex2_map))
ex2_map.update(master_map)
print('Translated seeds: ' + str(ex2_map))

print('Exercise 2 Final Answer: ' + str(min([x.dest_start for x in ex2_map.ranges])))