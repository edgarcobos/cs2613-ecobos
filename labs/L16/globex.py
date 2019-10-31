#!/usr/bin/python3
import glob
import os
from os.path import join
new_dir = os.path.expanduser("~/fcshome/cs2613/labs/test")

python_files_for = []

for file in glob.glob("*.py"):
    python_files_for.append(join(new_dir,file))

python_files_comp = [join(new_dir,file) for file in glob.glob("*.py")]

python_files_map = map(lambda file: join(new_dir,file), glob.glob("*.py"))