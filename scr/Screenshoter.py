import os
from datetime import datetime
from time import sleep
from io import BytesIO

try:
    import keyboard
    from PIL import ImageGrab
    from plyer import notification
    import win32gui
    import win32clipboard
    import pywinauto  # без этой строки разрешение экрана и координаты определяются неверно
except ModuleNotFoundError:
    print('''
|||||||||||||||||||||||||| Ошибка ||||||||||||||||||||||||||

Один из модулей отсутствует. Запуск установщика через 3 сек.

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    ''')
    sleep(3)
    os.system('cls')
    os.system('python installer.py')
    exit(0)

date = datetime.now().strftime('%d.%m.%Y')
root_path = os.path.expanduser('~/Documents/Screenshoter')
date_path = root_path + '/' + str(date)
w_handle = None

welcome = '''
Программа готова к использованию.
Управление:
    Сохранить скриншот :: CTRL + ALT
    Скопировать скриншот в буфер :: CTRL + WIN
    Выход :: CTRL + Q
'''


def alert(msg):
    notification.notify(title='Screenshoter', message=msg, app_name='Screenshoter')


def copy_to_clipboard(clipboard_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clipboard_type, data)
    win32clipboard.CloseClipboard()


def screenshot(command):
    hwnd = win32gui.GetForegroundWindow()
    coordinates = win32gui.GetWindowRect(hwnd)
    filename = os.listdir(date_path).__len__() + 1

    image = ImageGrab.grab((coordinates[0] + 10, coordinates[1], coordinates[2] - 10, coordinates[3] - 10))

    if command == 'save':  # сохранить
        image.save(date_path + '/%d.png' % filename, 'PNG')
        print('Скриншот сохранен как %s' % date_path + '/%d.png' % filename)
        alert('Скриншот сохранен как %s' % date_path + '/%d.png' % filename)
    elif command == 'copy':  # скопировать в буфер
        toclip = BytesIO()
        image.convert('RGB').save(toclip, 'BMP')
        data = toclip.getvalue()[14:]
        toclip.close()
        copy_to_clipboard(win32clipboard.CF_DIB, data)
        print('Скриншот скопирован в буфер обмена')
        alert('Скриншот скопирован в буфер обмена')


if __name__ == '__main__':
    os.mkdir(root_path) if not os.path.exists(root_path) else None
    os.mkdir(date_path) if not os.path.exists(date_path) else None
    print(welcome)
    alert('Программа готова к работе')

    keyboard.add_hotkey("Ctrl + Alt", lambda: screenshot('save'))
    keyboard.add_hotkey("Ctrl + Win", lambda: screenshot('copy'))
    keyboard.wait('Ctrl + Q')
