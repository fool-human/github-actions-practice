"""calculator.py —— 被测试的功能模块。

实验 3 实践项目 1 中被 GitHub Actions 的 pytest 步骤调用的"被测代码"。
步骤 5 的失败案例要求临时把 add() 改成 return a * b，观察工作流变红、
日志里出现 FAILED 后再改回正确实现，保证最后一次运行是绿色对勾。
"""


def add(a, b):
    """两数相加。"""
    return a + b


def multiply(a, b):
    """两数相乘。"""
    return a * b
