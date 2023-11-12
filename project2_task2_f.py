"""Mini-project 2 task 2 subtask f"""
import re
import os
import queue

def grep(re_to_find: str, re_for_file:str, st_dict:str, show_lines:bool, only_show_count:bool):
    """find all files in a directory that match a regular expression 
    and print lines that match a regular expression
    if show_lines is True, print lines that match a regular expression in format count:line
    if only_show_count is True, print only count of lines that match a regular expression
    >>> grep("ello$", "txt$", "test_folder", show_lines=True, only_show_count=False)
    """
    q = queue.Queue()
    q.put(st_dict)
    result = {}
    while True:
        if q.empty():
            break
        item = q.get()
        if os.path.isdir(item):
            for file in os.listdir(item):
                q.put(os.path.join(item, file))
        else:
            if re.search(re_for_file, item.split('/')[-1]):
                result[item.split('/')[-1]] = []
                with open(item, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if re.search(re_to_find, line):
                            result[item.split('/')[-1]].append(line)
    if only_show_count:
        for key in result:
            print(f"{key}\nMatches:{len(result[key])}")
            print()
    elif show_lines:
        for key in result:
            print(f"{key}")
            count = 1
            for value in result[key]:
                print(f"{count}:{value}")
                count += 1
            print()
    else:
        for key in result:
            print(f"{key}")
            for value in result[key]:
                print(f"{value}")
            print()
            
if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    import argparse
    parser = argparse.ArgumentParser(description='grep')
    parser.add_argument('re_to_find', help='regular expression to find')
    parser.add_argument('re_for_file', help='regular expression for file')
    parser.add_argument('st_dict', help='directory to search')
    parser.add_argument('-l', '--show_lines', action='store_true', help='show lines')
    parser.add_argument('-c', '--only_show_count', action='store_true', help='only show count')
    args = parser.parse_args()
    grep(args.re_to_find, args.re_for_file, args.st_dict, args.show_lines, args.only_show_count)