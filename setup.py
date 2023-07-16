import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

#アイコンファイル指定
icon = "icon/notebook.ico"

# exeにしたいpythonファイルを指定
exe = Executable(
  script="notecalc.py",
  base=base,
  icon=icon
)

# セットアップ
setup(
  name="NoteCalc",
  version="0.6",
  author="ojiji",
  url="https://ojiprog.com",
  description="NoteCalc",
  executables=[exe]
)
