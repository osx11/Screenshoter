import os
from time import sleep

modules = ['Pillow', 'Plyer', 'keyboard', 'pywin32', 'pywinauto']

print('''
|||||||||||||
Upgrading pip
|||||||||||||
''')

os.system('python -m pip install --upgrade pip')

for module in modules:
    print('''
||||||||||||||||||||||
Installing %s
||||||||||||||||||||||
    ''' % module)
    os.system('pip install %s' % module)

print('''
|||||||||||||||||||||||||||||||||||
Installing completed. Waiting 3 sec
|||||||||||||||||||||||||||||||||||
''')

sleep(3)
os.system('cls')
os.system('python Screenshoter.py')
exit(0)
