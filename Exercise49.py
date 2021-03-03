from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/Users/Argir') if isfile(join('/Users/Argir', f))]
print(files_list);
