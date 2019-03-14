#!/usr/bin/python3
import glob
import os
from typing import List, Set


def convert_bytes(size: int) -> str:
    for x in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size < 1024.0:
            return '%3.1f %s' % (size, x)
        size /= 1024.0


def file_size(path: str) -> str:
    return convert_bytes(os.stat(path).st_size)


def file_list(directory: str) -> List[str]:
    _list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_abs_path = os.path.join(os.path.abspath(root), file)
            _list.append(file_abs_path)
    return _list


def file_line(file: str) -> int:
    with open(file) as f:
        return len(f.readlines())


def suffix_list(directory: str) -> Set:
    suffix = set()
    for f in file_list(directory):
        suffix.add(os.path.splitext(f)[1])
    return suffix


def dir_detail_java(directory: str):
    _list = glob.glob(os.path.join(directory, '**/*.java'), recursive=True)
    print('Java file numbers:', len(_list))
    for f in _list:
        print(f, file_size(f), file_line(f))


def dir_detail_text(directory: str):
    _list = file_list(directory)
    print('Text file numbers:', len(_list))
    for f in _list:
        if ('.git' not in f) and ('.idea' not in f) and ('.DS_Store' not in f) and (not f.endswith('.zip')) and \
                (not f.endswith('.gif')) and (not f.endswith('.png')) and (not f.endswith('.jar')):
            print(f, file_size(f), file_line(f))


def list_all_file(directory: str):
    _list = glob.glob(os.path.join(directory, '**/*'), recursive=True)
    for f in _list:
        if os.path.isfile(f):
            print(f)


if __name__ == '__main__':
    gson_dir = '/Users/neo/IdeaProjects/gson'
    # print(suffix_list(gson_dir))
    # list_all_file(gson_dir)
    dir_detail_text(gson_dir)
    # dir_detail_java(gson_dir)
