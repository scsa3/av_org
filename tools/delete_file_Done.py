from pathlib import Path

p = Path('../Done')
l = [x for x in p.iterdir() if x.is_dir()]
for f in p.iterdir():
    if f.is_file():
        f.unlink()
