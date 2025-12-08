import re


class PuzzleObject:

    def __init__(self, tp, vl):
        self.type_obj = tp
        self.value = vl

    def __repr__(self):
        return '(' + self.type_obj + ', ' + str(self.value) + ')'


class PuzzelRange:

    def __init__(self, stt, stp):
        self.start = stt
        self.stop = stp

    def __contains__(self, item):
        return self.start <= item <= self.stop

    def get_offset(self, item):
        return item - self.start

    def __repr__(self):
        return 'Range(' + str(self.start) + ',' + str(self.stop) + ')'


class PuzzleMap:

    def __init__(self, fr, to):
        self.from_type = fr
        self.to_type = to
        self.number_map = {}

    def add_range_to_map(self, destination_range_start, source_range_start, range_length):
        self.number_map[PuzzelRange(source_range_start, source_range_start + range_length)] = \
            PuzzelRange(destination_range_start, destination_range_start + range_length)

    def translate_object(self, puzobj):
        if self.from_type == puzobj.type_obj:
            return PuzzleObject(self.to_type, self.translate_value(puzobj.value))

    def translate_value(self, vl):
        for rng in self.number_map.keys():
            if vl in rng:
                return self.number_map[rng].start + rng.get_offset(vl)
        return vl


with open('input/5.txt') as f:
    lines = f.readlines()


# Read starting seeds
# Exercise 1
print('Ex1')
starting_seeds = [PuzzleObject('seed', int(el)) for el in re.findall(r'\d+', lines[0])]
print(starting_seeds)

# Read all Puzzle Maps
puzzlemaps = {}
curr_map = None
for line in lines[2:]:
    if line.strip() == '':
        pass
    elif not line[0].isnumeric():
        from_type = line.split('-to-')[0]
        to_type = line.split('-to-')[1].split(' ')[0]
        curr_map = PuzzleMap(from_type, to_type)
        if from_type not in puzzlemaps.keys():
            puzzlemaps[from_type] = [curr_map]
        else:
            puzzlemaps[from_type].append(curr_map)
    else:
        spl = line.strip().split(' ')
        curr_map.add_range_to_map(int(spl[0]), int(spl[1]), int(spl[2]))


# Translate seeds to locations
end_locations = []
for starting_seed in starting_seeds:
    curr_puzobj = starting_seed
    while curr_puzobj.type_obj != 'location':
        # print(curr_puzobj)
        for puzzlemap in puzzlemaps[curr_puzobj.type_obj]:
            curr_puzobj = puzzlemap.translate_object(curr_puzobj)
    end_locations.append(curr_puzobj)

print(end_locations)
print(min([end_location.value for end_location in end_locations]))

print('Ex2')


