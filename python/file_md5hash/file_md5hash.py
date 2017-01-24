#! /usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import
import hashlib
import sys
import os


'''
Name          MD5                               Bytes
------------  --------------------------------  ------
FastHash.ini  c40911fa141dab099a69f5b3bdd81153   1,227
------------------------------------------------------
Total  1 Files  1,227 Bytes

'''


def output_info(target_path):
    fileSize = os.path.getsize(target_path)
    size = "{:,d}".format(fileSize)
    path = os.path.basename(target_path)
    m5 = md5(target_path)
    sizes = [len(x) for x in [path, m5, size]]
    sep = ["-" * a for a in sizes]
    fmts = ["{" + str(i) + ":" + str(a) + "}" for i, a in enumerate(sizes)]
    fmt = "  ".join(fmts)
    label = fmt.format("Name", "MD5", "Bytes")
    print(label)
    print(fmt.format(sep[0], sep[1], sep[2]))
    print(fmt.format(path, m5, size))
    print(len(label) * "-")
    print("Total  1 Files  " + size + " Bytes")


def md5(filename):
    with open(filename, "rb") as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()


def main():
    num = len(sys.argv)
    for i in range(1, num):
        output_info(sys.argv[i])


if __name__ == '__main__':
    main()
