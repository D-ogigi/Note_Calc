import tkinter as tk
from tkinter.constants import E, N, S, W

base = None

root = tk.Tk()

icon = '''R0lGODlhIAAgAHAAACH5BAEAAP8ALAAAAAAgACAAh3NROXRROX5VP35aP3dVQH9d
R4BWP4FXQIJZQYVbQoRfQ4FZRYVbRIddRYleRYZhRYphR4tkR4VjS4thSI1iSY9l
SoliTolmTo9qSotoT5FmS5FnTJBqSpNoTZVqTpNtTJVuTpltT5ZwT4pkUI1qUZZr
UJFtU5dsUJJvVZluUZdwUJNwVpVyV5pxUp1xU5t0Upx1U55zVZ52VJZzWJp2W6J2
VZ6TU6qSXaSaW5qGe5uJfZ+JfamfYqCLf6aLfaaMfa2iZq+larSjbbGnbLOpbrWr
cbasc7eudbmvd7CvfbSwdLKwfbuxebyyecO9bsO9csXAbdzbe93eedzcfPPLZuXJ
defNfurPfvLPd+Lfd+HdeeHcfvXRefLRfPXTft/gfePidu/mcejjdeHgeOTjf/Hj
cvDlc/XmcfPjd/DldvXndvXodvfjefLnf/fnf/nle/nlfPXoevbofZ2LgKSNgqaR
hquTha2Sh66ph7Cribe2h6SikL2so7+upcCtpN3cgt/fh9/fjcvNm8zOm8vNnczP
ndLPl9PPmdPPndTPndXSmtPQmdTRn+fOgufOh+rPg+fPi+rQiPTTg/bUgPfUhfjV
iN/giODhg+TjguHiheThheblhuPjieTgiePkiubliuLjjeXjjOPkjeXljujnjfTm
g/TnhPjnhfbogfLphvfrhvroh/PpiffqiffsivPrjfXqjffsjvroiPnpjuPjkuXj
kuXmkeLilebmlennkujnlOnokuroluPjmebmmeXmnejnmenmnefom+fonevpmezp
m+npne3pnPTrkfbskvTrlfbslvjqkvjskfrrlfntlvbtmvbtnvntmfnunfztncvL
o8vNoczPocvKpObmoufnpOnnoOfpoufppenpouzqourqpu3rpe3sp+rqquzrq+3s
q+nqr+vsre3srvbuoffvpPnvofzuovnvpfzvpffwp/nwpvfwqvfwrPnxqvzwqfrx
rvzxrurrsevtsu7usevste3ute7uuPrysfnztQAAAAj/AP8J/Ofnzg8fB38cRKiw
oY+HCe34GTiwzwgBCDJmTIAggUePDDx21HjAgAALEwX2WYDAwYSXEyjIrECzZgWZ
MmFOaIBgAR+BIw44mFlhQwejHjyUKKG0RIenRzXQnODAwAiBAhpQoKkBaYkTJ0Kk
GDsWrNOoNCMwEPCvTtatRjsoPZGiRQsXePG2GLvUw4YNFSI0EFCnh4GhGJDSresi
huPHelOc8NBBgwYKDgTs6DFgaNekIe66qEG6NGm9IUL4BfxA8xwCBSRcyECChAkU
LGbMoMG7N40ZLFagMEEiwwUJBQjs0AFggIIHETBg+ABCxIsXMmTUyA7jugoQHzhg
/4jw4MEAADny2MDB4waQIEOIFDFyBAkSJk3yM0FyxEgRIkMEAQQQPOBgQx6MvCHL
LJU8Iw011LDjDj302GNhPxZS6A477EAojTOzyPJGItf8EQgtkPySzTbajDOOOffg
o88+/Oijzz3muAhONr/80sstgfxxDSJsnDILJc48Q8067MBDTz319ONPP1TaM487
7axDzYfNzHIKG4dcs0UntUTiSzDbgAPOOOjkQyM/cPKTDz7liOPNNtv4wkstnWxh
DSJolNKKJMssA8007agzT5RS+jOlPPLMo04600DDDDOwmIKGIYVEAQgojvTyyzDd
rHkOPvi8uc8++JxzTjfdcP/j4y20WDIFIYmcgUorkyTj4DTrtAPPolT2E+U888Cz
zjTSPNNMLK2gcoYhg2ihSSiP6AKMMcZ8I0454+Qj7rjo1AnON8YQw4sto2iixSCL
lOEGK14gk4yh0agDzzvxQOrvO++oUyk0ySADCyttlMGpFJeA0gguuAgzDDfeiDNO
Oefkg8455ZCjJjfGCAMMLrSAcokWhSxyhhyqeBFLM808c+g6NOsLDzxZLjvNM8/E
Eosrqsgx7SBjYPLJFbbswgsxxhzzjbffiiNOOE9/U4y6uuxCyieYjAFvGG2k0sUr
ryRzLzTRpB1NOmynEw00cCuDDDKvsJJKG2YsfAknV4zOYgvEwnC7jTfefAMO4dsM
EzLEttgiCieXeK3IGXG0rEorPsfMszTQSON5s8s8k4zPrQCtShxnLIINGGRscgUp
sO+i9NLEFHPM7VerK7vWW29CBhjV/CNGGm1gkQorrJA9t9zKKLNM83MnA0vddt+d
hhgC6QHGF1VkwoknnoQiit9/Q4xL4+yK4gknnGSSyRdg6DHQEmFQsUYc+MshByr8
99+//vjD3xrOEIYlUOQfexACFJzghAU64QkQjKAEn8BABkJBCXs4oAY3yMEOBgQA
Ow=='''

root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(data=icon))
root.title("NoteCalc")

check_b = tk.BooleanVar()
check_b.set(True)
check_button = tk.Checkbutton(root, variable=check_b, text="計算後改行")
check_button.grid(sticky= tk.W, row=0, column=0)

text_note = tk.Text(root)
text_note.grid(sticky = (E, W, S, N), columnspan = 2)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text_note.tag_config("goukei", foreground="red")

def textinput(event):
  kotae = text_note.get("insert -1lines linestart", "insert -1lines lineend")
  text_note.insert("insert", "{:,}".format(eval(kotae.replace(",",""))), "goukei")
  if check_b.get():
    text_note.insert("insert","\n")

root.bind("<Return>", textinput)

root.mainloop()