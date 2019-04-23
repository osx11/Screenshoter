import os

print('''
|||||||||||||
Upgrading pip
|||||||||||||
''')

os.system('python -m pip install --upgrade pip')

print('''
|||||||||||||||||||
Uninstalling Pillow
|||||||||||||||||||
''')

os.system('pip uninstall Pillow -y')

print('''
||||||||||||||||||
Uninstalling Plyer
||||||||||||||||||
''')

os.system('pip uninstall Plyer -y')

print('''
|||||||||||||||||||||
Uninstalling keyboard
|||||||||||||||||||||
''')

os.system('pip uninstall keyboard -y')

print('''
||||||||||||||||||||
Uninstalling pywin32
||||||||||||||||||||
''')

os.system('pip uninstall pywin32 -y')

print('''
||||||||||||||||||||||
Uninstalling pywinauto
||||||||||||||||||||||
''')

os.system('pip uninstall pywinauto -y')
