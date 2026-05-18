import os

def get_size(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for file in os.listdir(path):
            child = os.path.join(path, file)
            total += get_size(child)
    print(f"{total} path: {path}")
    return total