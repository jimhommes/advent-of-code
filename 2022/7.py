class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.total_size = 0
        self.folders = {}
        self.files = {}

    def add_folder(self, foldername):
        if foldername not in self.folders.keys():
            self.folders[foldername] = Folder(foldername, self)

    def add_file(self, filename, filesize):
        if filename not in self.files.keys():
            self.files[filename] = File(filename, int(filesize))
            self.add_size(int(filesize))

    def add_size(self, size):
        self.total_size += int(size)
        if self.parent is not None:
            self.parent.add_size(size)

    def to_console(self, prefix=None):
        if prefix is None:
            prefix = ' - '
        print(prefix + self.name + ' (dir, total_size=' + str(self.total_size) + ')')
        for folder in self.folders.values():
            folder.to_console(' |' + prefix)
        for file in self.files.values():
            file.to_console(' |' + prefix)

    def get_list_of_all_dirs(self):
        res = list(self.folders.values())
        for direl in self.folders.values():
            res += direl.get_list_of_all_dirs()
        return res

    def __str__(self):
        return str({'folders': str(self.folders), 'files': str(self.files)})

    def __repr__(self):
        return str({'folders': str(self.folders), 'files': str(self.files)})


class File:

    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def to_console(self, prefix=None):
        print(prefix + self.name + ' (file, size=' + str(self.size) + ')')


with open('input/7.txt') as f:
    lines = f.readlines()

root = Folder('/', None)
curr_dir = None
last_command = None

# Preprocessing directory
for line in lines:
    spl = line.strip().split(' ')
    if spl[0] == '$':
        # Command
        last_command = spl[1]
        if spl[1] == 'cd':
            # change directory
            if spl[2] == '/':
                curr_dir = root
            elif spl[2] == '..':
                curr_dir = curr_dir.parent
            else:
                curr_dir = curr_dir.folders[spl[2]]
        elif spl[1] == 'ls':
            # list files
            pass
    elif spl[0] == 'dir':
        # Dir
        if last_command == 'ls':
            curr_dir.add_folder(spl[1])
    elif spl[0].isnumeric():
        # File
        if last_command == 'ls':
            curr_dir.add_file(spl[1], spl[0])


# print(root.folders)
# print(root.files)


def get_total_size_under_threshold(direc, thresh):
    res = 0
    for direl in direc.folders.values():
        res += get_total_size_under_threshold(direl, thresh)

    if direc.total_size <= thresh:
        res += direc.total_size
    return res


print(get_total_size_under_threshold(root, 100000))

# Part 2

total_disk_space = 70000000
unused_space_required = 30000000

all_dirs = root.get_list_of_all_dirs()
all_dirs.sort(key=lambda i: i.total_size)
for direl in all_dirs:
    if total_disk_space - root.total_size + direl.total_size >= unused_space_required:
        print(direl.total_size)
        break
