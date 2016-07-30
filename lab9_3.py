from tkinter import *
import re
import InputBox

s = "result:\n"

sp1 = ("hat", "cat", "sat", "take", "not")
for i in sp1:
    if re.search(r'at$', i):
        s += i + "\n"

sp2 = ("This is a sentence.", "With command,", "has a semicolon;", "and a colon:",
       "nothing")
for i in sp2:
    if re.search(r'[.,;]$', i):
        s += i + "\n"

sp3 = ("2", "7s", "372.65", "6.22e-23", "s123")
for i in sp3:
    if re.match(r'^\d', i):
        s += i + "\n"

sp4 = ("2", "7s", "372.65", "6.22e-23", "s123", "#ffffff")
for i in sp4:
    if re.match(r'^\D', i):
        s += i + "\n"

sp5 = ("apple tree", "Tom Smith", "hometown", "house ", " cat")
for i in sp5:
    if re.match(r'\s\w', i):
        s += i + "\n"

InputBox.ShowDialog("Enter a sentence contains the word 'apple': ")
sp6 = InputBox.GetInput()
p1 = re.compile(r"\bapple\b")
p2 = re.compile(r"\bapple\b.")
if p1.search(sp6) or p2.search(sp6):
    s += "pass\n"
else:
    s += "Must contain the word 'apple'.\n"

sp7 = ("sent", "sat", "sit", "site")
for i in sp7:
    if re.match(r'^\bs\S*t\b', i):
        s += i + "\n"

sp8 = ["sit sat", "so sad", "sat-seat", "no match"]
for i in sp8:
    if re.match(r"(s\w+)\W(s\w+)", i):
        s += i + "\n"

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()


