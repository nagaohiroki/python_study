@setlocal enabledelayedexpansion
@for %%F in (*.cpp) do @set CPPS=!CPPS! %%F
@for %%H in (*.h) do @set HPPS=!HPPS! %%H

@echo �\�[�X�R�[�h�̐��`
clang-format -i %CPPS% %HPPS%

@echo �ÓI���
clang-check -analyze %CPPS% --

@echo �r���h
clang++ -std=c++14 -Wall -g %CPPS%

@echo ���s
a.exe

