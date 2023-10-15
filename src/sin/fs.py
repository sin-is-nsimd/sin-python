#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''`sin.fs` offers helpers for filesystem operations.'''

# Copyright © 2021,2023 Lénaïc Bagnères, lenaicb@singularity.fr

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import hashlib


def md5(path):
    '''Compute the md5 of the file `path`.'''
    m = hashlib.md5()
    with open(path, 'rb') as f:
        while True:
            buf = f.read(2048)
            if not buf:
                break
            m.update(buf)
    return m.hexdigest()


def symlink(src, dest):
    '''
    Create the symlink `src` -> `dest`.

    If destination already exists, this function does nothing.
    '''
    if os.name == 'posix':
        try:
            os.symlink(os.path.abspath(src), dest)
        except FileExistsError:
            pass
    else:
        raise NotImplementedError(
            'sin.fs.symlink is not implemented for your OS (' + os.name + ')')
