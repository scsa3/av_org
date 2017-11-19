import re
from pathlib import Path

pattern = re.compile(r'^[a-zA-Z]{2,4}-?[0-9]{3}\.')


def av_filter(path=Path()):
    for p in path.iterdir():
        if p.is_file() and pattern.search(p.name):
            print(pattern.search(p.name).group())
            print(p.name)
    pass


if __name__ == '__main__':
    av_filter(Path('../!Test'))
