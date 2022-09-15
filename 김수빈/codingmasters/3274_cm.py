# -*- coding: utf-8 -*-
import sys

N = int(sys.stdin.readline())
print(['jjamppong', 'jjajangmyeon', 'bokkeumbap', 'jjajangmyeon'][(N - 1) % 4])