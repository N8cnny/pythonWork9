import InputBox
from tkinter import *


s = "result:\n"


InputBox.ShowDialog("Enter your email: ")
sp1 = InputBox.GetInput()
if not re.match(r"\w+@\w+\.(com|org|net|gov|edu|mil)", sp1):
    s += "Not a valid address.\n"
else :
    s += "A valid email address.\n"

sp2 = ("sit", "sat", "set", "sot", "sut", "seat")
for i in sp2:
    if re.match(r'^s(a|i|u|e|o)t$', i):
        s += i + "\n"

s += str(re.match(r"Mari[oe]", "Mario")) + "\n"
s += str(re.match(r"Mari[oe]", "Marie")) + "\n"
s += str(re.match(r"Mari[oe]", "Maria")) + "\n"

s += str(re.match(r'[xyz]', "xerox")) + "\n"
s += str(re.match(r'[xyz]', "yellow")) + "\n"
s += str(re.match(r'[xyz]', "Zebra")) + "\n"

s1 = ('Mariko', 'Maryko', 'Meriko', 'Meryko', 'Muriko', 'Maruko')
s2 = []
for i in s1:
    if re.match(r"M[ae]r[iy]ko", i):
        s2.append(i)
s += str(s2) + "\n"

sp6 = ('01x', '1yp', '249', '3c', '4gme', '5t', '66s', '714', '8a', '9zz')
for i in sp6:
    if re.match(r'[0-7]', i):
        s += i + "\n"

InputBox.ShowDialog("Enter a number: ")
sp7 = InputBox.GetInput()
if not re.match(r"[0-5][0-9]", sp7):
    s += "No matched. Must have two digits from 00 to 59.\n"
else:
    s += "Matched.\n"

InputBox.ShowDialog("Enter an HTML color code: ")
sp8 = InputBox.GetInput()
if (not re.match(r"^#[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9AFa-f]",
                 sp8)):
    s += "Not a valid HTML color code.\n"
else:
    s += "It is a valid color code.\n"

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()
