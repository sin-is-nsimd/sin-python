#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""`sin.term` offers colored texts for terminals."""

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


def grey(s):
    """Return the string `s` with grey color code (for VT100 terminals)."""
    return "\033[90m" + s + "\033[0m"


def red(s):
    """Return the string `s` with grey color code (for VT100 terminals)."""
    return "\033[91m" + s + "\033[0m"


def green(s):
    """Return the string `s` with grey color code (for VT100 terminals)."""
    return "\033[92m" + s + "\033[0m"


def orange(s):
    """Return the string `s` with grey color code (for VT100 terminals)."""
    return "\033[93m" + s + "\033[0m"


def blue(s):
    """Return the string `s` with grey color code (for VT100 terminals)."""
    return "\033[94m" + s + "\033[0m"


def purple(s):
    """Return the string `s` with grey color code (for VT100 terminal)."""
    return "\033[95m" + s + "\033[0m"


def tag_ok():
    """Return the string `[OK]` with `sin.term.green` color."""
    return "[" + green("OK") + "]"


def tag_info():
    """Return the string `[INFO]` with `sin.term.blue` color."""
    return "[" + blue("INFO") + "]"


def tag_warning():
    """Return the string `[WARNING]` with `sin.term.orange` color."""
    return "[" + orange("WARNING") + "]"


def tag_error():
    """Return the string `[ERROR]` with `sin.term.red` color."""
    return "[" + red("ERROR") + "]"


def tag_todo():
    """Return the string `[TODO]` with `sin.term.purple` color."""
    return "[" + purple("TODO") + "]"
