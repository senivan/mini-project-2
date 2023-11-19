"""Mini-project 2 task 2 subtask a by Sen Ivan"""
import os

def tree(directory, prefix="") -> str:
    """
        >>> print(tree('test_folder'))
        ├── File1.txt
        ├── Folder1
        |   └── File2.txt
        └── Folder2
            ├── File2.txt
            └── Folder3
                └── File3.txt
    """
    if not os.path.isdir(directory):
        raise ValueError('Starting directory does not exist or is file')
    result = []
    entries = sorted(os.listdir(directory))
    for i, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        new_prefix = prefix + ('└── ' if i == len(entries)-1 else '├── ')
        if os.path.isdir(path):
            result.append(f"{new_prefix}{entry}")
            result.extend(tree(path, prefix + ('    ' if i == len(entries)-1 else '|   ')))
        else:
            result.append(f"{new_prefix}{entry}")
    if prefix == "":
        return '\n'.join(result)
    return result

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    # import argparse
    # parser = argparse.ArgumentParser(
    #     prog='task 2 subtask a',
    #     description='print directory tree'
    # )    
    # parser.add_argument('st_dir', type=str, help='starting directory')
    # args = parser.parse_args()
    # try:
    #     print(tree(args.st_dir))
    # except ValueError as e:
    #     print(e)