import re
import pickle
import requests
from lxml import etree
from pathlib import Path


class AV:
    pattern = {'number': re.compile(r'[a-zA-Z]{2,4}-\d{3,4}'),
               'extension': re.compile(r'.(mp4|avi|mkv|wmv)')}

    def __init__(self, path):
        self.av_number = self.pattern['number'].match(path.stem).group()
        self.av_extension = self.pattern['extension'].match(path.suffix).group()
        print(self.av_number)
        print(self.av_extension)

a = AV(Path('./Done/AQJ-901.mp4'))
a.actress_name = 123
print(a.actress_name)
a.av_number = 1
