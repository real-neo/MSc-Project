import csv
import glob
import os
from typing import List, Set


def convert_bytes(size: int) -> str:
    for x in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size < 1024.0:
            return '%3.1f %s' % (size, x)
        size /= 1024.0


def file_size_in_byte(path: str) -> int:
    return os.stat(path).st_size


def file_size(path: str) -> str:
    return convert_bytes(file_size_in_byte(path))


def file_list(directory: str) -> List[str]:
    _list = []
    for root, dirs, files in os.walk(directory):
        for _f in files:
            file_abs_path = os.path.join(os.path.abspath(root), _f)
            _list.append(file_abs_path)
    return _list


def file_line(file: str) -> int:
    with open(file) as _f:
        return len(_f.readlines())


def suffix_list(directory: str) -> Set:
    _suffix = set()
    for _f in file_list(directory):
        _suffix.add(os.path.splitext(_f)[1])
    return _suffix


def dir_detail(directory: str, suffix: str) -> List:
    _list = glob.glob(os.path.join(directory, '**/*.' + suffix), recursive=True)
    print(suffix + ' file numbers:', len(_list))
    _detail = []
    for _f in _list:
        _detail.append([_f.replace(directory, '.'), file_size(_f), file_size_in_byte(_f), file_line(_f)])
    return _detail


def dir_detail_text(directory: str) -> List:
    _list = file_list(directory)
    print('Text file numbers:', len(_list))
    _detail = []
    for _f in _list:
        if ('.git' not in _f) and ('.idea' not in _f) and ('.DS_Store' not in _f) and (not _f.endswith('.zip')) and \
                (not _f.endswith('.gif')) and (not _f.endswith('.png')) and (not _f.endswith('.jar')):
            _detail.append([_f.replace(directory, '.'), file_size(_f), file_size_in_byte(_f), file_line(_f)])
    return _detail


def list_all_file(directory: str):
    _list = glob.glob(os.path.join(directory, '**/*'), recursive=True)
    for _f in _list:
        if os.path.isfile(_f):
            print(_f)


def export_detail_to_csv(export: List, filename: str):
    with open(filename, mode='w') as csv_file:
        csv_file.write("File,Size,Size(bytes),LOC\r\n")
        _w = csv.writer(csv_file)
        for _e in export:
            _w.writerow(_e)


if __name__ == '__main__':
    gson_dir = '/Users/neo/IdeaProjects/gson'
    # print(suffix_list(gson_dir))
    # list_all_file(gson_dir)
    # detail = dir_detail_text(gson_dir)
    detail = dir_detail(gson_dir, 'java')
    export_detail_to_csv(detail, 'data/software-detail.csv')
