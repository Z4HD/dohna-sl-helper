import os
import platform

import PyInstaller.__main__

if platform.os.name == 'nt':
    split_prefix = ';'
else:
    split_prefix = ':'

PyInstaller.__main__.run([
    '--name=dohna-sl-helper',
    '--onefile',
#    '--windowed',
    f'--add-data=pic/{split_prefix}pic',
#    f'--add-data=icon.ico{split_prefix}.',  # Add icon file into bundle
#    '--icon=%s' % os.path.abspath('icon.ico'),
    os.path.abspath('bootstrap_win.py')
])
