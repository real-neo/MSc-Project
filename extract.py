import csv
import glob
import os
from typing import List


def convert_bytes(size: int) -> str:
    for x in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size < 1024.0:
            return '%3.1f %s' % (size, x)
        size /= 1024.0


def file_size_in_byte(path: str) -> int:
    return os.stat(path).st_size


def file_size(path: str) -> str:
    return convert_bytes(file_size_in_byte(path))


def file_line(file: str) -> int:
    with open(file) as _f:
        return len(_f.readlines())


def dir_detail(directory: str, suffix: str) -> List:
    _list = glob.glob(os.path.join(directory, '**/*.' + suffix), recursive=True)
    print(suffix + ' file numbers:', len(_list))
    _detail = []
    for _f in _list:
        _detail.append([_f.replace(directory, '.'), file_size(_f), file_size_in_byte(_f), file_line(_f)])
    return _detail


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
