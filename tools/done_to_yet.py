from pathlib import Path

file_list = [x for x in Path('../!Done/').iterdir() if x.is_file()]
for i in file_list:
    i.rename(Path('../!Yet/') / i.name)
