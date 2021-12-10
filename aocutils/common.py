# AUTOGENERATED! DO NOT EDIT! File to edit: 00_common.ipynb (unless otherwise specified).

__all__ = ['to_int', 'ints', 'flatten', 'reverse_dict', 'zippify', 'list_multiply']

# Internal Cell
from collections.abc import Iterable
from collections import namedtuple, deque
import contextlib
from functools import reduce
import hashlib
import heapq
import logging
from math import sqrt, gcd
from pathlib import Path
import time
import pickle
import pandas as pd
import numpy as np

DATA_DIR = Path('data')

# Cell
def to_int(inp: Iterable, intonly=False):
    """
        returns items converted to int if possible
        keeps lists and tuples intact
        e.g. to_int(['-12', 2, 'a']) returns [-12, 2, 'a']
        watch out because passing a string '12t' will be ripped into a list [1,2,t]
    """
    if isinstance(inp,str):
        print('watch out string will be converted into list of characters and single digit ints')
    if isinstance(inp[0],list):
        return list(to_int(l) for l in inp)
    if isinstance(inp[0],tuple):
        return tuple(to_int(l) for l in inp)

    out = []
    for i in inp:
        try:
            out.append(int(i))
        except ValueError:
            if not intonly:
                out.append(i)
    if isinstance(inp,tuple): return tuple(out)
    else: return list(out)

# Cell
def ints(text: str) -> tuple[int]:
    """
        Return a tuple of all the integers in a string
    """
    return tuple(map(int, re.findall('-?[0-9]+', text)))

# Cell
def flatten(x):
    # recursive flattens the input. Returns a list
    return list(_flatten(x))

def _flatten(x):
    for item in x:
        if isinstance(item,Iterable) and not isinstance(item, str):
            yield from _flatten(item)
        else:
            yield item

# Cell
def reverse_dict(d):
    return {v:k for k,v in d.items()}

# Cell
def zippify(iterable, len=2, cat=False):
    """
        Zips an iterable with arbitrary length pieces
        e.g. to create a moving window with len n
        Example:
        zippify('abcd',2, cat=False)
        --> [('a', 'b'), ('b', 'c'), ('c', 'd')]

        If cat = True, joins the moving windows together
        zippify('abcd',2, cat=True)
        --> ['ab', 'bc', 'cd']
    """
    iterable_collection = [iterable[i:] for i in range(len)]
    res = list(zip(*iterable_collection))
    return [''.join(r) for r in res] if cat else res

# Cell
def list_multiply(a,b):
    """
        Multiplies two iterables elementwise
        Returns a list

        Example:
        list_multiply([1,2,3],[2,3,4])
        --> [2, 6, 12]
    """
    return (np.array(a)*np.array(b)).tolist()
