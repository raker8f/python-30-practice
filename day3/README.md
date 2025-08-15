# Day 3 — 裝飾器（Decorator）
裝飾器就是一個用來「包裝」其他函數的函數，讓你在不改動原本程式碼的情況下，增加額外功能。

舉例一個沒有裝飾器的測試執行時間的程式:
```python
import time

def slow_function():
    time.sleep(1)
    print("完成！")

start = time.time()
slow_function()
end = time.time()
print(f"花費時間: {end - start:.4f} 秒")
```
可以得到slow_function()執行時間，但每次都得在函數外加上 `start` / `end`。  
相對我們可以先將計時程式寫成裝飾器:
```python
import time

# 定義裝飾器
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # 執行原本的函數
        end = time.time()
        print(f"{func.__name__} 花費時間: {end - start:.4f} 秒")
        return result
    return wrapper
```
再將其加到要測量的函式上:
```python
@timer  # 這一行就是「套用裝飾器」
def slow_function():
    time.sleep(1)
    print("完成！")

slow_function()
```
只要使用`slow_function()`皆會測量時間。