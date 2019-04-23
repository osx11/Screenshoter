import keyboard
import os
from datetime import datetime

from PIL import ImageGrab
from plyer import notification
import win32gui

date = datetime.now().strftime('%d.%m.%Y')
root_path = os.path.expanduser('~/Documents/Screenshoter')
date_path = root_path + '/' + str(date)
w_handle = None

screen_width = 3840
screen_height = 2160

welcome = '''
Программа готова к использованию.
Управление:
    Скриншот :: CTRL + ALT
    Выход :: CTRL + Q
'''


def alert(msg):
    notification.notify(title='Screenshoter', message=msg, app_name='Screenshoter')


def first_startup():
    #  ######################################## creating directories ###################################################
    os.mkdir(root_path) if not os.path.exists(root_path) else None
    os.mkdir(date_path) if not os.path.exists(date_path) else None
    # ##################################################################################################################


def screenshot():
    coordinates = coords()
    if not coordinates:
        return

    filename = os.listdir(date_path).__len__() + 1

    img = ImageGrab.grab((coordinates[0] + 10, coordinates[1], coordinates[2] - 10, coordinates[3] - 10))
    img.save(date_path + '/%d.png' % filename, 'PNG')
    print('Скриншот сохранен как %s' % date_path + '/%d.png' % filename)
    alert('Скриншот сохранен как %s' % date_path + '/%d.png' % filename)


def coords():
    hwnd = win32gui.GetForegroundWindow()
    rect = win32gui.GetWindowRect(hwnd)
    return rect


if __name__ == '__main__':
    first_startup()
    print(welcome)

    keyboard.add_hotkey("Ctrl + Alt", lambda: screenshot())
    keyboard.wait('Ctrl + Q')
