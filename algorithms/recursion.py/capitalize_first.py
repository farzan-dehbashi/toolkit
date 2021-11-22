##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################

import numpy as np


def capitalize_first(string):
    parts = string.split(' ')
    first_word = parts[0]
    if len(parts) <= 1:
        if len(first_word) > 1:
            return str(first_word[0].capitalize()+first_word[1:])
        else:
            return str(first_word[0].capitalize())
    else:
        if len(first_word) > 1:

            parts.remove(first_word)
            string = ' '.join(map(str, parts))
            return str(first_word[0].capitalize()+first_word[1:]) +' '+ capitalize_first(string)
        else:
            return str(first_word[0].capitalize()) + ' '+capitalize_first(string)
if __name__ == '__main__':
    string = 'Alafetam balas hazinasha yakuza namusan'
    print(capitalize_first(string))
