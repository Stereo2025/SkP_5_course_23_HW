from typing import Iterator

from config import DATA_DIR


def read_file():
    with open(DATA_DIR, 'r') as f:
        return [i.strip() for i in f.readlines()]


class Search:
    def filter_foo(self: Iterator, param: str):
        if not isinstance(param, str):
            raise TypeError
        return filter(lambda row: param in row, self)

    def map_foo(self: Iterator, num_column: [int, str]):
        if not isinstance(num_column, int):
            raise TypeError
        return map(lambda row: row.strip().split(' ')[:num_column - 1], self)

    def sort_foo(self: Iterator, param: str):
        return sorted(self, reverse=True) if param == 'asc' else sorted(self, reverse=False)

    def limit_foo(self: Iterator, param: int):
        return list(self)[:int(param)]

    def unique_foo(self: Iterator):
        return set(self)
