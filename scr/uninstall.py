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
|||||||||||||||||||||||||||
Uninstalling %s
|||||||||||||||||||||||||||
    ''' % module)
    os.system('pip uninstall %s -y' % module)

print('''
|||||||||||||||||||||||||||||||||||||
Uninstalling completed. Waiting 3 sec
|||||||||||||||||||||||||||||||||||||
''')

sleep(3)
exit(0)
