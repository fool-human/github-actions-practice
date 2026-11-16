"""test_calculator.py —— 单元测试。

文件名以 test_ 开头，pytest 默认的发现规则（pytest.ini 中 testpaths = .）会收集它，
工作流里执行 `pytest -v` 即可运行。
"""

import pytest

from calculator import add, multiply


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(2, 0) == 0
