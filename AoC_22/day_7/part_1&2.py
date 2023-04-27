class Directory:
    def __init__(self, name, files, parent):
        self.name = name
        self.files = files
        self.parent = parent

    def __repr__(self):
        return self.name
    
    @property
    def size(self):
        size = 0
        if not self.files:
            return 0
        for file in self.files:
            num_str = '0'
            i=0
            while file[i].isdigit():
                num_str += file[i]
                i += 1
            num = int(num_str)
            size += num
        return size


lines = []
with open('/Users/oliverjordan/AoC_22/day_7/input_7.txt') as input:
    for line in input:
        line = line.rstrip("\n")
        lines.append(line)
lines.append('$')

directories = []
parent = None
for i in range(len(lines)):
    line = lines[i]
    if line[:4] == '$ cd' and '..' not in line:
        name = line[5:]
        files = []
        j = 2
        while lines[i+j][0] != '$':
            if lines[i+j][:3] != 'dir':
                files.append(lines[i+j])
            j+=1
        current = Directory(name, files, parent)
        directories.append(current)
        parent = current
    if line == '$ cd ..':
        parent = parent.parent

def calculate_size(dir):
    size = dir.size
    for directory in directories:
        if directory.parent == dir:
            size += calculate_size(directory)
    return size

sizes = []
for directory in directories:
    sizes.append(calculate_size(directory))


target = 30000000 - (70000000 - 42476859)
result = sorted(list(filter(lambda x: x>=target, sizes)))[0]
print(result)


total = 0
for size in sizes:
    if size <= 100000:
        total += size

print(total)

