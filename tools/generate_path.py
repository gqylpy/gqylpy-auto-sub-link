#!/usr/bin/python
# coding: utf-8

"""
@Author: Zhu Yongkang
@Email: 137326237@qq.com
@Software: PyCharm
@File: generate_path.py
@Time: 2019-07-09 14:53
"""
import os


def gen_path(*args: str) -> 'An absolute path':
    # Generate an absolute path.
    return os.path.abspath(os.path.join(*args))
