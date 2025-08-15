#Day 1 — 進階資料結構
目標：掌握 Python 內建高效資料結構，提升可讀性與效能。

學習重點
1. 推導式 (Comprehension)  
    推導式能夠用一行程式碼表達原本需要多行迴圈和條件判斷才能完成的功能，使程式碼更加精簡。 
```python
# list 推導式
nums = [x * 2 for x in range(5)]
# dict 推導式
squares = {x: x**2 for x in range(5)}
# set 推導式
unique_letters = {c for c in "hello world"}
```
2. collections 模組
- Counter：計數器
- defaultdict：帶預設值的字典
- deque：高效雙端佇列
```python
from collections import Counter, defaultdict, deque

# Counter
text = "apple banana apple orange banana apple"
counter = Counter(text.split())
print(counter)

# defaultdict
words_by_first_letter = defaultdict(list)
for word in ["apple", "banana", "apricot", "blueberry"]:
    words_by_first_letter[word[0]].append(word)
print(words_by_first_letter)

# deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)
```