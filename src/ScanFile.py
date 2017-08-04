import os
from os import listdir
from os.path import isfile, join

def scan():
    url = '/Users/yszsyf/Desktop'


    onlyfiles = [f for f in listdir(url) if isfile(join(url, f))]

    return onlyfiles

print scan()