import tkinter as tk
from tkinter import ttk

#Parser Code
from termcolor import colored
listofbasevalues = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
listofbasevaluesint = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

def invertlist(listinput: list):
    # The output of the program is added to this
    output = []

    for i in range(len(listinput)-1, -1, -1):
        output.append(listinput[i])

    return output

# Convert both inputs to Array[string]
# Invert both lists 
def convert_basentobaseten(basen1: int, inputbase_n):
    # Convert both inputs to Array[string]
    # Invert both lists 
    inputbase_n1_list_inv = invertlist(list(str(inputbase_n)))

    out_baseten_int = 0

    for i in range(len(inputbase_n1_list_inv)):
        if (inputbase_n1_list_inv[i] in listofbasevalues):
            out_baseten_int += int(listofbasevalues.index(inputbase_n1_list_inv[i]))* (int(basen1)**i)
        else: 
            raise Exception("ParserItemNotInListException: Value Not in Accepted List of Base Values")

    return out_baseten_int

def basemarker(inputbase_n, basen1):
    return f"({(inputbase_n)})b{basen1}"

def conv_10pl_equiv(inputd, mode):
    #Base 10 equiv of the input
    rlist = []
    if mode == "to":
        for n in inputd:
            rlist.append(listofbasevalues[n])
    elif mode == "from":
        for n in inputd:
            if (type(n) == int):
                rlist.append(listofbasevaluesint.index(n))
            else: 
                rlist.append(listofbasevalues.index(n))

    return rlist

#Main convert function
def convert_bases(basen1: int | str, basen2: int | str, inputbase_n):
    basen1 = int(basen1)
    basen2 = int(basen2)
    base10v_input = int(convert_basentobaseten(basen1, inputbase_n))
    pbconv_cond = False
    returnlist = []
    prevval = base10v_input % basen2
    prevmodp1 = base10v_input
    fscount = 0

    while (not pbconv_cond):
        returnlist.append(int(prevval))

        prevmodp1 = (prevmodp1 - prevval) / basen2
        prevval = prevmodp1 % basen2
        fscount += 1
        if (((prevmodp1)/basen2) == 0):
            pbconv_cond = True
        if (fscount == 100):
            break

    return "".join(conv_10pl_equiv(invertlist(returnlist), "to"))

#GUI Code
root = tk.Tk()

def parseinput (base1, base2, inputmain):
    r = (convert_bases(base1, base2, inputmain))
    resultlabel.configure(text=r)

frm = ttk.Frame(root, padding=100, width=75, height=75)
frm.grid()
root.title("nBasen")
im1 = tk.PhotoImage(file="assets/i4.ppm")
ttk.Label(frm, image=(im1), compound='image').grid(column=0, row=0)

inval1 = tk.StringVar(frm)
inval2 = tk.StringVar(frm)
menu1 = ttk.Combobox(frm,textvariable=inval1)
menu2 = ttk.Combobox(frm,textvariable=inval2)
menu1.state(["readonly"])
menu2.state(["readonly"])
menu1["values"] = ["Select an Option", "Base 1", "Base 2", "Base 3", "Base 4", "Base 5", "Base 6", "Base 7", "Base 8", "Base 9", "Base 10", "Base 11","Base 12", "Base 13", "Base 14", "Base 15", "Base 16"]
menu2["values"] = ["Select an Option", "Base 1", "Base 2", "Base 3", "Base 4", "Base 5", "Base 6", "Base 7", "Base 8", "Base 9", "Base 10", "Base 11","Base 12", "Base 13", "Base 14", "Base 15", "Base 16"]
menu1.grid(column=0, row=1, pady=5)
menu2.grid(column=0, row=3)
entry1var = ""
entry1 = tk.Entry(frm, textvariable=entry1var, font=('Arial', 12), width=16, justify=tk.CENTER)
entry1.grid(column=0, row=2, pady=4)
submitbtn = ttk.Button(frm, text="Submit", command=lambda: parseinput(menu1.current(), menu2.current(), entry1.get()))
submitbtn.grid(column=0, row=5, pady=4)
resultlabel = ttk.Label(frm, text="", justify=tk.CENTER, font=('Arial', 12))
resultlabel.grid(column=0, row=4, pady=4)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=8, pady=30, padx=50)
root.wm_iconbitmap("assets/i4.ico")
root.mainloop()
