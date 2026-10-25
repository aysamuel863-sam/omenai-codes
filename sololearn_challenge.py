import string
word = list(input("Enter a word: "))
all = string.ascii_lowercase + string.ascii_uppercase + " "
wordd = word[::-1]
for ch in wordd:
    chh = any(ch in wordd for ch in all)
#if chh:
    #continue
for ch in wordd:
    if ch not in all:
        wordd.remove(ch)
worddd = set(word)

print(all)
use = "Hello, ><.343 I am 47849$%^&^54 Samuel;'.34"
print(use[::-1])
print(wordd)
print(worddd)
w = str(worddd)
print(w)
for i in worddd:
    if i not in all:
        worddd.remove(i)
print(worddd)