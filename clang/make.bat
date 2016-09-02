@setlocal enabledelayedexpansion
@for %%F in (*.cpp) do @set CPPS=!CPPS! %%F
@for %%H in (*.h) do @set HPPS=!HPPS! %%H

@echo ソースコードの整形
clang-format -i %CPPS% %HPPS%

@echo 静的解析
clang-check -analyze %CPPS% --

@echo ビルド
clang++ -std=c++14 -Wall -g %CPPS%

@echo 実行
a.exe

