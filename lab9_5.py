import InputBox
from tkinter import *

s = "result:\n"

InputBox.ShowDialog("Enter your email: ")
email = InputBox.GetInput()
if not re.match(r"\w+@\w+\.(com|org|net|gov|edu|mil)", email):
    s += "Not a valid email address.\n"
else:
    s += "A valid email address.\n"

InputBox.ShowDialog("Enter a U.S. social security number: ")
ssn = InputBox.GetInput()
if not re.match(r"^\d{3}-\d{2}-\d{4}$", ssn):
    s += "It is not a valid social security number.\n"
else:
    s += "It is a valid social security number.\n"

pattern = r"^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$"
InputBox.ShowDialog("Enter a U.S. phone number: ")
phone = InputBox.GetInput()
if not re.match(pattern, phone):
    s += "It is not a valid U.S. phone number.\n"
else:
    s += "It is a valid U.S. phone number.\n"

pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
InputBox.ShowDialog("Enter an IPv4 address: ")
ipv4 = InputBox.GetInput()
if not re.match(pattern, ipv4):
    s += "It is not a valid IPv4 address.\n"
else:
    s += "It is a valid IPv4 address.\n"

pattern = r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$"
InputBox.ShowDialog("Enter a URL: ")
url = InputBox.GetInput()
if not re.match(pattern, url):
    s += "It is not a valid URL.\n"
else:
    s += "It is a valid URL.\n"

InputBox.ShowDialog("Enter an HTML color code: ")
color = InputBox.GetInput()
if not re.match(r"^#[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9AFa-f]",
                color):
    s += "Not a valid HTML color code.\n"
else:
    s += "It is a valid HTML color code.\n"

InputBox.ShowDialog("Enter a Visa card number: ")
visa = InputBox.GetInput()
if not re.match(r"^4[0-9]{12}(?:[0-9]{3})?$", visa):
    s += "Not a valid Visa card number.\n"
else:
    s += "Not a valid visa card number.\n"

InputBox.ShowDialog("Enter a MasterCard number: ")
master = InputBox.GetInput()
if not re.match(r"^5[1-5][0-9]{14}$", master):
    s += "Not a valid MasterCard number.\n"
else:
    s += "A valid MasterCard number.\n"

InputBox.ShowDialog("Enter an American Express card number: ")
ae = InputBox.GetInput()
if not re.match(r"^3[47][0-9]{13}$", ae):
    s += "Not a valid American Express card number.\n"
else:
    s += "A valid American Express card number.\n"

root = Tk()
root.title('Message Box')
Label(root, justify=LEFT, text=s).grid()

root.mainloop()
