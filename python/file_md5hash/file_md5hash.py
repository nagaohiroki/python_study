# coding: utf-8
import hashlib
import sys
def md5(filename):
    '''
    md5変換
    '''
    with open(filename, "rb") as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()

def main():
    '''
    メイン
    '''
    num = len(sys.argv)
    if num <= 1:
        print('error set argments 2')
        return
    for i in range(1, num):
        print(md5(sys.argv[i]))

if __name__ == '__main__':
    main()
