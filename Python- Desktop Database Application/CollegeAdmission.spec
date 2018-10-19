# -*- mode: python -*-

block_cipher = None


a = Analysis(['CollegeAdmission.py'],
             pathex=['/Users/yusufusanu/Documents/Python- Desktop Database Application/Tkinter Project_Final'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='CollegeAdmission',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='ndowed')
app = BUNDLE(exe,
             name='CollegeAdmission.app',
             icon='ndowed',
             bundle_identifier=None)
