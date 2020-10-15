#pyi-makespec main.py
#pyinstaller -D main.spec -i image\0108.ico -w
#pyinstaller -D main.spec -i image\0108.ico -w --clean --win-private-assemblies

# D：产生一个目录（包含多个文件）作为可执行程序；
# w：去掉控制台窗口；
# i：指定生成exe的图标；
# F：生成单个可执行文件，即可以把应用打包成一个独立的exe文件。注意指令区分大小 写。这里是大写；不加该参数是一个带各种dll和依赖文件的文件夹。


# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\GUI\\MGI Engineering Tools'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [('panda.ico','D:\\GUI\\MGI Engineering Tools\\image\\panda.ico','DATA')],
          exclude_binaries=True,
          name='MGI_Tools',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,icon='panda.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
