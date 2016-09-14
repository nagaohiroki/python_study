import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win64':base = 'Win64GUI'
exe = Executable(script = 'optpycs.py',base = base)

setup(
		name = 'optpycs',
		version = '1.0',
		description = 'coverter',
		executables = [exe])
