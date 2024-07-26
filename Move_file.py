import os 
import shutil

from_dir = "C:/Users/BHUVNESH/Downloads"
to_dir = "E:"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for files in list_of_files:
    name,extension = os.path.splitext(files)
    print(f"Name:{name},Extension:{extension}")
    