from os import listdir
from os.path import isfile, join
import pathlib

#mypath = pathlib.Path().resolve()
mypath="H:\Django\miEntorno\dashboard\media\myfolder"

print(mypath)


onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)