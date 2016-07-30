from tkinter import *
import re
s = "result:\n"

s += str(re.match(r"ab*", "")) + "\n"
s += str(re.match(r"ab*", "a")) + "\n"
s += str(re.match(r"ab*", "aa")) + "\n"
s += str(re.match(r"ab*", "ab")) + "\n"
s += str(re.match(r"ab*", "abb")) + "\n"
s += str(re.match(r"ab*", "abbb")) + "\n"
s += str(re.match(r"ab*", "abbbb")) + "\n"
s += str(re.match(r"ab*", "abbbbb")) + "\n"

s += str(re.search('[a-z]*', "")) + "\n"
s += str(re.search('[a-z]*', "f")) + "\n"
s += str(re.search('[a-z]*', "fl")) + "\n"
s += str(re.search('[a-z]*', "flo")) + "\n"
s += str(re.search('[a-z]*', "flow")) + "\n"
s += str(re.search('[a-z]*', "flowe")) + "\n"
s += str(re.search('[a-z]*', "flower")) + "\n"

sp3 = ["rub", "ruby", "rubyy", "rubyyy", "rubyyyy"]
for i in sp3:
    if re.match(r'ruby?', i):
        s += i + "\n"

sp4 = ["candy", "candyy", "candyyy", "candyyyy", "candyyyyy"]
for i in sp4:
    if re.match(r'candy+', i):
        s += i + "\n"

sp5 = ["apple", "banana", "cherry", "dragonfruit"]
for i in sp5:
    if re.match(r'a|b|c', i):
        s += str(i) + "\n"

sp6 = ["#ffccdd", "ffccdd", "#256", "ffccdd#"]
for i in sp6:
    if re.match(r'^#', i):
        s += i + "\n"

sp7 = ["apple", 'ant', 'amoeba', 'banana']
for i in sp7:
    if re.search(r'^a', i):
        s += i + "\n"
    else:
        s += "Not matched\n"

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()
