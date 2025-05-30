import winreg
import contextlib

def open_key(key, subkey):
    with winreg.OpenKey(key, subkey) as reg_key:
        print(reg_key)

def main():
    print("Hello, World!")


if __name__ == "__main__":
    main()
