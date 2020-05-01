# -*- coding: utf-8 -*-
#!/usr/bin/env python 
def triangle():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]

