# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:59:49 2019

@author: Thangarajan
"""
import os
import sys
from glob import glob
import platform
import zipfile
#1
base_path = 'E:\\learnings\\python\\temp\\'
os.makedirs(os.path.join(base_path,'1\\1\\1\\1'))
os.mkdir(os.path.join(base_path,'thanga'))

#2
base_path = 'E:\\learnings\\python\\hackers_rank\\'
X = []
for path in  os.walk(base_path,topdown=False):
    for p in path:
       print(p)

#3
code_path = os.path.dirname()
os.chdir(code_path)

#4
os.link(os.path.basename(__file__),os.path.join(base_path,'sample.txt'))

#5
os.rename(os.path.join(base_path,'sample.txt'),os.path.join(base_path,'sample.py'))

#6
os.remove(os.path.join(base_path,'sample.py'))

#7
with open(os.path.join(base_path,'sample.txt'),'r') as f:
#    print(sys.getsizeof(f.read()))
    content = f.read()
    if len(content.strip()) == 0:
        print('empty')
    else:
        with open(os.path.join(base_path,'sanjay.txt'),'w') as f1:
            f1.write(content)

        print('Non-Empty')
        
#8
new_file_name = os.path.join(base_path,'sanjay.txt')
if os.path.exists(new_file_name):
    print('already exists')


#9
try:
    os.mkdir(os.path.join(base_path,'thanga\thanga\thanga'))
except OSError:
    raise

#10
os.environ
os.system('chrome.exe')


#11
os.pipe()

#12
zip_path = r'E:\learnings\python\temp'
with zipfile.ZipFile('sample.zip','w') as z:
    for files in os.listdir():
        z.write(files)
        
#13
x = os.popen('python.exe')
x._stream
x.__doc__
x._proc


#14
os.lstat(base_path+'sample.txt')

#15
os.cpu_count()

#16
os.environ
os.getenv('USERNAME')
platform.architecture()
platform.dist()
platform.java_ver()
platform.machine()
platform.mac_ver()
platform.os
platform.python_build()
platform.release()
