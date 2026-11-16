# 说明文档：使用 GitHub Actions 实现自动化测试

本仓库是实验 3 实践项目 1 的代码，演示「推送代码 → GitHub Actions 自动跑 pytest → 查看结果」。

## 目录结构

```
.
├── .github/
│   └── workflows/
│       └── ci.yml           # 工作流：检出代码 → 设置Python → 安装依赖 → 运行测试
├── calculator.py            # 被测代码：add / multiply
├── test_calculator.py       # 单元测试：test_add / test_multiply
├── requirements.txt         # 项目依赖（pytest）
└── README.md
```

## 工作流执行步骤

| 步骤 | 动作 | 作用 |
| ---- | ---- | ---- |
| 1 | `actions/checkout@v4` | 检出代码：获取仓库代码到虚拟环境 |
| 2 | `actions/setup-python@v5` | 设置 Python 3.11 环境 |
| 3 | `pip install pytest` | 安装测试所需的包 |
| 4 | `pytest -v` | 运行测试，`-v` 显示详细结果 |

## 本地运行

```bash
pip install -r requirements.txt
pytest -v
```

## 如何判断测试结果

- **测试通过**：Actions 页签中状态为绿色对勾，日志中出现 `2 passed` / `PASSED`。
- **测试失败**：状态为红色叉号，日志中出现 `FAILED`，并明确指出哪个用例失败及断言差异。

## 步骤 5：失败案例演示

1. 把 `calculator.py` 的 `add` 改成错误的实现：

   ```python
   def add(a, b):
       return a * b   # 错误的实现
   ```

2. 提交并推送，工作流变为失败（红叉）。
3. 打开失败的 job 查看日志，可见：

   ```
   assert (2 * 3) == 5
   E       assert 6 == 5
   ```

4. 把实现改回 `return a + b` 再推送，工作流恢复绿色，此时再提交仓库地址。
