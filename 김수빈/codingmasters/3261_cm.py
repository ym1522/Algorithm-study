# -*- coding: utf-8 -*-
import sys

java_t = sys.stdin.readline().strip()
py_t = sys.stdin.readline().strip()
print("JAVA") if float(java_t[:-1]) <= float(py_t[:-1]) else print("PYTHON")