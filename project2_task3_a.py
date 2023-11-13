"""Mini project 2 task 3 subtask a"""
import re
import zipfile
import queue
import os

def copy_files_with_re_from_zip(regular_exp:str, archive_path:str, new_archive_path:str) -> None:
    """copy files with regular expression from zip
    >>> copy_files_with_re_from_zip("ello$", "test_folder.zip", "test_folder_copy.zip")
    """

    with zipfile.ZipFile(archive_path, 'r') as zip_file, zipfile.ZipFile(new_archive_path, 'w') as zip_file_copy:
        for file in zip_file.namelist():
            if os.path.isdir(file):
                continue
            with open(file, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if re.search(regular_exp, line):
                        zip_file_copy.write(file)
                        break
    

if __name__ == "__main__":
    # import doctest
    # print(doctest.testmod())
    import argparse
    parser = argparse.ArgumentParser(description='copy files with regular expression from zip')
    parser.add_argument('regular_exp', help='regular expression')
    parser.add_argument('archive_path', help='archive path')
    parser.add_argument('new_archive_path', help='new archive path')
    args = parser.parse_args()
    copy_files_with_re_from_zip(args.regular_exp, args.archive_path, args.new_archive_path)