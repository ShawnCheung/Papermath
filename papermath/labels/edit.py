import sys, os
for root, dirs, names in os.walk("./train"):
    for name in names:
        path = os.path.join(root, name)
        with open(path, 'r') as f:
            lines = f.readlines()
            lines = ["0 "+" ".join((line.split(' ')[1:])) for line in lines]
            with open(path, 'w') as f:
                for line in lines:
                    f.write(line)
