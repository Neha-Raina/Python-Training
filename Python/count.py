
word = "Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms."
d = {}
newword = word.split()

for letter in newword:
    if letter not in d:
        d[letter] = 1
    else:
        d[letter] +=1
print(d)
