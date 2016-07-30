
from tkinter import *

s = "result:\n"

sp1 = "one by one, case by case, step by step"
result = str(re.match(r'one', sp1)) + "\n"
result = result + str(re.match(r'case', sp1)) + "\n"
result = result + str(re.match(r'step', sp1)) + "\n"
s += result

s += str(re.search("^From", "From Here to Eternity")) + "\n"
s += str(re.search("^From", "Reciting From Memory")) + "\n"

sp3 = "one by one, case by case, step by step"
s += str(re.findall(r'case', sp3)) + "\n"
s += str(re.findall(r'step', sp3)) + "\n"
s += str(re.findall(r'one', sp3)) + "\n"

sp4 = "moon n23 net m69 dot map pat"
list = str(re.findall("[nm]\w+", sp4)) + "\n"
s += str(list)

p = re.compile(r'\bclass\b')
s += str(p.search('no class at all')) + "\n"
s += str(p.search('the declassified algorithm')) + "\n"
s += str(p.search('one subclass is')) + "\n"


root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()

