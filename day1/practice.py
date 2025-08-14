from collections import Counter, defaultdict, deque

# list 推導式
nums = [x * 2 for x in range(5)]
# dict 推導式
squares = {x: x**2 for x in range(5)}
# set 推導式
unique_letters = {c for c in "hello world"}

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
