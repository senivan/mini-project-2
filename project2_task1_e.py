"""Mini-project 2 task 1 subtask e by Sen Ivan"""
import os
def find_same(path1:str, path2:str, res_path:str) -> None:
    """
    Find same lines in two files and write them to result file.
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
    ...    _ = f.write('a\\nb\\na\\n')
    >>> with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f2:
    ...    _ = f2.write('a\\nb\\n')
    >>> with tempfile.NamedTemporaryFile(mode='w+', delete=False) as res:
    ...    find_same(f.name, f2.name, res.name)
    >>> with open(res.name, 'r') as res:
    ...    print(res.read())
    a
    b
    """
    if not os.path.isfile(res_path):
        raise ValueError('Result file does not exist or is directory')
    if not (os.path.isfile(path1) and os.path.isfile(path2)):
        raise ValueError('One of the files does not exist or is directory')
    with open(path1, 'r', encoding='utf-8') as file1, open(path2, 'r', encoding="utf-8")\
 as file2, open(res_path, 'w+', encoding="utf-8") as res_file:
        lines1 = file1.readlines()
        lines2 = file2.readlines()
        for line1 in lines1:
            if line1 in lines2 and line1 not in res_file:
                res_file.write(line1)
if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    import argparse
    parser = argparse.ArgumentParser(
        prog='task 1 subtask e',
        description='find same lines in files'
    )

    parser.add_argument('path1', type=str, help='first file to compare')
    parser.add_argument('path2', type=str, help='second file to compare')
    parser.add_argument('dst', type=str, help='file to write results to')

    args = parser.parse_args()
    find_same(args.path1, args.path2, args.dst)
