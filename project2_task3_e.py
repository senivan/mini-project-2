"""Mini-project 2 task 3 subtask e"""

def compose_archives(zip_one:str, zip_two:str, zip_result:str) -> None:
    """compose two archives into one
    >>> compose_archives("test_folder.zip", "just_folder.zip", "test_folder_result.zip")
    """
    import zipfile
    with zipfile.ZipFile(zip_one, 'r') as zip_file_one, zipfile.ZipFile(zip_two, 'r') as zip_file_two, zipfile.ZipFile(zip_result, 'w') as zip_file_result:
        for file in zip_file_one.namelist():
            zip_file_result.write(file)
        for file in zip_file_two.namelist():
            zip_file_result.write(file)

if __name__ == '__main__':
    # import doctest
    # print(doctest.testmod())
    import argparse
    parser = argparse.ArgumentParser(description="Program that makes zip file from 2 zip files")
    parser.add_argument('zip_one', help='First zip file')
    parser.add_argument('zip_two', help='Second zip file')
    parser.add_argument('zip_result', help='Resulting zip file')
    args = parser.parse_args()
    compose_archives(args.zip_one, args.zip_two, args.zip_result)