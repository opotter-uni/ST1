#!/usr/bin/env python3

eggs = 14
sausage = "the quick brown fox jumps over the lazy dog"
bacon = False


if not bacon:
    eggs **=3
    eggs /=25
    eggs +=150
    eggs = round(eggs)
print(eggs)

spam = []
for char in sausage:
    if char in ["a","e","i","o","u"]:
        spam.append("spam")
    else: spam.append(char)

spam = "".join(spam)
print(spam)