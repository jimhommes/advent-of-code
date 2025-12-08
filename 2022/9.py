class Coordinates:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direc):
        self.last_move = direc
        if direc == 'R':
            self.x += 1
        elif direc == 'L':
            self.x -= 1
        elif direc == 'U':
            self.y += 1
        elif direc == 'D':
            self.y -= 1

    def follow(self, to_follow):
        dist = self.get_distance(to_follow)
        if dist >= 2:
            if abs(to_follow.x - self.x) == abs(to_follow.y - self.y):
                # Move diagonally
                if to_follow.x > self.x:
                    self.x += 1
                else:
                    self.x -= 1
                if to_follow.y > self.y:
                    self.y += 1
                else:
                    self.y -= 1
            elif abs(to_follow.x - self.x) > abs(to_follow.y - self.y):
                # Horizontal movement
                self.y = to_follow.y
                if to_follow.x > self.x:
                    # Move right
                    self.x = to_follow.x - 1
                else:
                    # Move Left
                    self.x = to_follow.x + 1
            else:
                # Vertical movement
                self.x = to_follow.x
                if to_follow.y > self.y:
                    # Move Up
                    self.y = to_follow.y - 1
                else:
                    self.y = to_follow.y + 1

    def get_distance(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

    def __repr__(self):
        return str((self.x, self.y))


with open('input/9.txt') as f:
    lines = f.readlines()

rope = [Coordinates() for i in range(10)]
tail = rope[-1]
tail_prev_coords = set()

print('Starting: ' + str(rope))

for line in lines:
    spl = line.strip().split(' ')
    direction = spl[0]
    amount = int(spl[1])

    print('Executing instruction: ' + direction + ' ' + str(amount))
    for i in range(amount):
        # Move the head
        rope[0].move(direction)
        # Update all tails
        for j in range(1, 10):
            rope[j].follow(rope[j-1])

        tail_prev_coords.add((tail.x, tail.y))
        print('Rope: ' + str(rope))

print(len(tail_prev_coords))
