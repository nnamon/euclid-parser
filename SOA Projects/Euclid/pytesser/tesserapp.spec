# -*- mode: python -*-
a = Analysis(['tesserapp.py'],
             pathex=['D:\\SOA Projects\\Euclid\\pytesser'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='tesserapp.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
