# Day 2—生成器與迭代器  
目標：掌握 Lazy Evaluation，節省記憶體。

## 學習重點  
1. 生成器函數（`yield`）  
2. 生成器表達式
3. `next()` 與迭代器協議

1. 生成器函數（Generator Function）  
關鍵詞：`yield`  
- 函數用 `return`，會一次回傳全部結果，結束後就不能再繼續。
- 生成器函數用 `yield`，可以 「暫停」 函數執行，下一次呼叫會從暫停的地方繼續。
- 好處：
    * 節省記憶體（一次產生一筆，不會全部載入到記憶體）
    * 適合處理大檔案、無限序列等情境
```python
def read_file_line_by_line(filename):
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()  # 暫停這裡，等下一次呼叫再繼續
```

2. 生成器表達式（Generator Expression）
- 跟 list comprehension 很像，但用 小括號。
- 它不會馬上生成完整列表，而是懶加載（lazy evaluation），一次取一個值。
- 好處：在處理數十萬甚至數百萬筆資料時，效能與記憶體消耗比 list comprehension 好很多。
```python
for line in read_file_line_by_line("test.txt"):
    print(line)
```

3. 迭代器（Iterator）  
關鍵詞：`iter()`、`next()`、`StopIteration`
- 迭代器是一個可以被逐步取值的物件，內部實作了 `__iter__() 和 __next__()`。
- for 迴圈就是不斷呼叫迭代器的 `__next__()`。
- 當資料取完時，會丟出 StopIteration 例外（`for` 迴圈會自動處理，不會報錯）。
- 生成器本身就是迭代器。
```python
nums = [10, 20, 30]
it = iter(nums)   # 轉成迭代器
print(next(it))   # 10
print(next(it))   # 20
print(next(it))   # 30
```