##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Description: employ polymorphism to read files
##################################################

import json
import pandas as pd
import os
import sys

class File():
    def __init__(self, name, extention, size, path):
        self.name = name
        self.extention = extention
        self.size = size
        self.path = path

    def read(self):
        f_content = None
        with open(self.path, encoding = 'utf-8') as f:
            f_content = f.read()
        return f_content


class JsonFile(File):
    def __init__(self, name, extention, size, path):
        super().__init__(name, extention, size, path)

    def read(self):
        f_content = None
        try:
            with open(self.path, encoding='utf-8') as f:
                f_content = json.load(f)
        except:
            print(f'{self.path} not found')
        return f_content


class TextFile(File):
    def __init__(self, name, extention, size, path):
        super().__init__(name, extention, size, path)


class CsvFile(File):
    def __init__(self, name, extention, size, path):
        super().__init__(name, extention, size, path)

    def read(self):
        f_content = None
        try:
            f_content = pd.read_csv(self.path)
        except:
            print(f'{self.path} not found')
        return f_content.to_string()


#####################

text_file_obj = TextFile('text', 'txt', os.path.getsize('./text.txt'), './text.txt')
csv_file_obj = CsvFile('csv', 'csv', os.path.getsize('./csv.csv'), './csv.csv')
json_file_obj = JsonFile('json', 'JSON', os.path.getsize('./json.JSON'), './json.JSON')
print(json_file_obj.read())