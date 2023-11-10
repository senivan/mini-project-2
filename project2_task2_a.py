"""Mini-project 2 task 2 subtask a by Sen Ivan"""
import os
import queue

def tree(st_dir:str, recursion_call:bool = False, call_root:str="",stick_dict:dict = {}) -> str:
    """
        >>> print(tree('test_folder'))
        test_folder
        |  ├──File1.txt
        ├──Folder2
        |  ├──File2.txt
        ├─────Folder3
        |     ├──File3.txt
        ├──Folder1
        |  ├──File2.txt
        <BLANKLINE>
    """
    if not os.path.isdir(st_dir):
        raise ValueError('Starting directory does not exist or is file')
    result = {}
    q = queue.Queue()
    q.put(st_dir)
    while True:
        if q.empty():
            break
        item = q.get()
        if os.path.isdir(item):
            result[item] = [i for i in os.listdir(item) if os.path.isfile(os.path.join(item, i))]
            result[item].extend([i for i in os.listdir(item) if os.path.isdir(os.path.join(item, i))])
            for i in os.listdir(item):
                q.put(os.path.join(item, i))
    if recursion_call:
        string_result = st_dir.split('/')[-1] + '\n' 
    else:
        string_result = st_dir + '\n'
    res_q = queue.Queue()
    res_q.put(st_dir)
    while True:
        if res_q.empty():
            break
        item = res_q.get()
        flag = True
        for value in result[item]:
            if call_root == "":
                call_root = st_dir
                level = item.count('/') - st_dir.count('/')
                print(level)
            else:
                level = item.count('/') - call_root.count('/')
            if level not in stick_dict:
                stick_dict[level] = True
            start_symbol = ('├──' if result[item].index(value) < len(result[item])-1 else "└──")
            if start_symbol == "└──":
                flag = False
                stick_dict[level] = False
            if os.path.isdir('/'.join([item, value])) and not recursion_call:
                string_result +=  start_symbol + "───"*level + tree('/'.join([item,value]), True, call_root=st_dir)
            elif os.path.isdir('/'.join([item, value])) and recursion_call:
                if start_symbol == '└──':
                    # string_result += ''.join(['|  ' if stick_dict[key] == True else '   ' for key in stick_dict])[1::]
                    string_result += '|  '*(level) + start_symbol  + tree('/'.join([item,value]), True, call_root=call_root, stick_dict=stick_dict)
                else:
                    string_result += '|  '*(level) + start_symbol  + tree('/'.join([item,value]), True, call_root=call_root, stick_dict=stick_dict)
            else:
                if start_symbol == '└──':
                    string_result += '|  '*(level) + start_symbol + value + '\n'
                else:
                    string_result += '|  '*(level) + start_symbol + value + '\n'
    return string_result

if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    import argparse
    parser = argparse.ArgumentParser(
        prog='task 2 subtask a',
        description='print directory tree'
    )    
    parser.add_argument('st_dir', type=str, help='starting directory')
    args = parser.parse_args()
    try:
        print(tree(args.st_dir))
    except ValueError as e:
        print(e)