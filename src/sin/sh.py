#!/usr/bin/env python3

# Copyright © 2023 Lénaïc Bagnères
# Copyright © 2023 Rodolphe Cargnello

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
import sys

import sin.term


def run_cmd(cmd, print_cmd=True, exit_on_error=True, use_rosetta=False):
    """
    Run a command using `os.system`

    If `print_cmd` is `True`, the command is printed.
    `True` by default.

    If `exit_on_error` is `True`, `sys.exit(1)` is called.
    `True` by default.

    If `use_rosetta` is `True`, the command is called with `x86_64` emulation.
    <https://en.wikipedia.org/wiki/Rosetta_(software)>
    `False` by default.
    """
    if use_rosetta:
        cmd = cmd.replace('"', '\\"')
        cmd = f'arch -x86_64 /bin/zsh -c "{cmd}"'
    if print_cmd:
        print(cmd)
    r = os.system(cmd)
    if r != 0:
        print(sin.term.tag_error(), "The command `" + cmd + "` failed")
        if exit_on_error:
            sys.exit(1)
