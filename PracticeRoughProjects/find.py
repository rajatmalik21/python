import PracticeRoughProjects.file_operations

def find_in(iterable, finder, expected):
    for i in iterable:
        if finder[i] == expected:
            return i
    raise NotFoundError(f'{expected} not found in the provided iterable')


class NotFoundError(Exception):
    pass


print(__name__)
