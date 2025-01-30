#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright © 2021,2023,2025 Lénaïc Bagnères, lenaicb@singularity.fr
# Copyright © 2024 Rodolphe Cargnello

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

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "src"))
import sin.fs  # nopep8

TEST_FILE_PATH = "_test_file"
TEST_DIRECTORY_PATH = "_tmp"


def create_test_file():
    """Create the `TEST_FILE_PATH` file"""
    with open(TEST_FILE_PATH, "w") as f:
        _ = f.write("Temporary file to test sin/fs.py")


def remove_test_file():
    """Remove the `TEST_FILE_PATH` file"""
    os.remove(TEST_FILE_PATH)


def test_sin_fs_md5():
    """Test the `sin.fs.md5` function"""
    create_test_file()
    assert sin.fs.md5(TEST_FILE_PATH) == "d1abc9789a534a4cd2f469c7a782b690"
    remove_test_file()


def test_sin_fs_sha1():
    """Test the `sin.fs.sha1` function"""
    create_test_file()
    assert sin.fs.sha1(TEST_FILE_PATH) == "f4199e44e01d81573b3e3818dfc39ff465629390"
    remove_test_file()


def test_sin_fs_sha256():
    """Test the `sin.fs.sha256` function"""
    create_test_file()
    assert sin.fs.sha256(TEST_FILE_PATH) == "09981881a423886541273d5ad3860358f28ca7f3027116614f52a6e198309295"
    remove_test_file()


def test_sin_fs_sha512():
    """Test the `sin.fs.sha512` function"""
    create_test_file()
    assert sin.fs.sha512(TEST_FILE_PATH) == "c52f02de356ab0a0da914153c334f66b402a8599148c70b9b2a2c5229b358744d91878e5f9e403690b6e396908f4d1db3a2ba3fb7061eb8ac2d761f049e98e71"
    remove_test_file()


def test_sin_fs_symlink():
    """Test the `sin.fs.symlink` function"""
    create_test_file()
    symlink_path = TEST_FILE_PATH + "_symlink"
    sin.fs.symlink(TEST_FILE_PATH, symlink_path)
    assert os.path.islink(symlink_path)
    assert sin.fs.md5(symlink_path) == sin.fs.md5(symlink_path)
    os.remove(symlink_path)
    remove_test_file()


def test_sin_fs_pushd():
    """Test the `sin.fs.pushd` function"""
    os.mkdir(TEST_DIRECTORY_PATH)
    current_path = os.getcwd()
    with sin.fs.pushd(TEST_DIRECTORY_PATH):
        assert os.path.join(current_path, TEST_DIRECTORY_PATH) == os.getcwd()
    assert current_path == os.getcwd()
    os.rmdir(TEST_DIRECTORY_PATH)
