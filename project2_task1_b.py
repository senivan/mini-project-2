def replace_substring(substring:str, repl:str, filename:str, inplace:int) -> None:
    pass

if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    import argparse
    parser = argparse.ArgumentParser(
        prog='task 1 subtask b',
        description='replace substring in file'
    )    
    parser.add_argument('substring', type=str, help='substring to replace')
    parser.add_argument('repl', type=str, help='replacement string')
    parser.add_argument('filename', type=str, help='file to modify')
    parser.add_argument('--inplace',action='store_const', const=1, help='modify file in place')
    args = parser.parse_args()
    # print(args)
    replace_substring(args.substring, args.repl, args.filename, args.inplace)