import timeit
import numpy as np
from scipy import stats
import multiprocessing
import platform
import sys

# 顯示系統資訊
print("Python 版本:", sys.version)
print("系統架構:", platform.machine())
print("處理器:", platform.processor())
print("核心數:", multiprocessing.cpu_count())
print("\n")

# 任務 1: 斐波那契序列 (遞迴，測試單核 CPU 性能)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def test_fib():
    fib(35)  # 計算 fib(35)，足夠大但不至於太慢

fib_time = timeit.timeit(test_fib, number=5) / 5  # 重複 5 次取平均
print("斐波那契序列 (fib(35)) 平均時間:", fib_time, "秒")

# 任務 2: 大型矩陣乘法 (使用 NumPy，測試向量化和多核)
def test_matrix_mult():
    a = np.random.rand(2000, 2000)
    b = np.random.rand(2000, 2000)
    np.dot(a, b)

matrix_time = timeit.timeit(test_matrix_mult, number=3) / 3  # 重複 3 次取平均
print("2000x2000 矩陣乘法 平均時間:", matrix_time, "秒")

# 任務 3: 線性回歸擬合 (使用 SciPy，測試科學計算性能)
def test_linear_regression():
    x = np.random.rand(1000000)
    y = 2 * x + np.random.normal(0, 0.1, 1000000)
    stats.linregress(x, y)

reg_time = timeit.timeit(test_linear_regression, number=10) / 10  # 重複 10 次取平均
print("100萬點線性回歸 平均時間:", reg_time, "秒")