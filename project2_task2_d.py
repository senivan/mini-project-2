"""Mini-project 2 task 2 subtask d by Sen Ivan"""
import os
import queue

def copy_file(src:str, dst:str) -> None:
    """Function that copies file from src to dst"""
    with open(src, 'rb') as f:
        with open(dst, 'wb') as f1:
            f1.write(f.read())
def copy_tree(src:str, dst:str) -> None:
    if not os.path.isdir(src):
        raise ValueError('Starting directory does not exist or is file')
    if not os.path.isdir(dst):
        os.mkdir(dst)
    structure = {}
    q = queue.Queue()
    q.put(src)
    while True:
        if q.empty():
            break
        item = q.get()
        if os.path.isdir(item):
            structure[item] = [i for i in os.listdir(item) if os.path.isfile(os.path.join(item, i))]
            structure[item].extend([i for i in os.listdir(item) if os.path.isdir(os.path.join(item, i))])
            for i in os.listdir(item):
                q.put(os.path.join(item, i))
    print(structure)
    for key in structure:
        for val in structure[key]:
            if os.path.isfile(os.path.join(key, val)):
                copy_file(os.path.join(key, val), os.path.join(key.replace(src, dst), val))
            else:
                os.mkdir(os.path.join(key.replace(src, dst), val))

if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    import argparse
    parser = argparse.ArgumentParser(
        prog='task 2 subtask d',
        description='copy directory tree'
    )
    parser.add_argument('src', type=str, help='source directory')
    parser.add_argument('dst', type=str, help='destination directory')
    args = parser.parse_args()
    copy_tree(args.src, args.dst)