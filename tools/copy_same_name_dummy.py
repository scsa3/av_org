from pathlib import Path


def print_file(p=Path()):
    for x in p.rglob('*'):
        if x.is_file():
            print('file:\t', x.name)
        if x.is_dir():
            print('dir:\t', x.name)


def copy_dummy(from_path=Path(), target_path=Path()):
    paths = from_path.rglob('*')


if __name__ == '__main__':
    p = Path('../!Test')
    nd = Path('../!Dummy')
    nd.mkdir(exist_ok=True)
    for x in p.rglob('*'):
        np = nd
        for mp in x.parts[2:]:
            np = np.joinpath(mp)
        print(np)



