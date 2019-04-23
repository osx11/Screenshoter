import os
from time import sleep

print('''
|||||||||||||
Upgrading pip
|||||||||||||
''')

os.system('python -m pip install --upgrade pip')

print('''
|||||||||||||||||||
Installing Pillow
|||||||||||||||||||
''')

os.system('pip install Pillow')

print('''
||||||||||||||||||
Installing Plyer
||||||||||||||||||
''')

os.system('pip install Plyer')

print('''
|||||||||||||||||||||
Installing keyboard
|||||||||||||||||||||
''')

os.system('pip install keyboard')

print('''
||||||||||||||||||||
Installing pywin32
||||||||||||||||||||
''')

os.system('pip install pywin32')

print('''
||||||||||||||||||||||
Installing pywinauto
||||||||||||||||||||||
''')

os.system('pip install pywinauto')

print('''
|||||||||||||||||||||||||||||||||||
Installing completed. Waiting 3 sec
|||||||||||||||||||||||||||||||||||
''')

sleep(3)
os.system('cls')
os.system('python Screenshoter.py')
exit(0)
