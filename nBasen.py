import tkinter as tk
from tkinter import ttk

#Global Values
listofbasevalues = ["0","1","2","3","4",
                    "5","6","7","8","9",
                    "A","B","C","D","E","F"]
listofbasevaluesint = [0,1,2,3,4,5,6,7,8,
                       9,"A","B","C",
                       "D","E","F"]
maxcharlen: int = 16

#Parser Code
def listtostr (inlist):
    return "".join(inlist)

def invertlist(listinput: list):
    output = []

    for i in range(len(listinput)-1, -1, -1):
        output.append(listinput[i])

    return output

# Convert both inputs to Array[string]
# Invert both lists 
def convert_basentobaseten(basen: int, inputbase_n):
    inputbase_n1: list = invertlist(list(str(str.upper(inputbase_n))))
    out_baseten_int = 0
    for i in range(0, len(inputbase_n1)):
        if (inputbase_n1[i] in listofbasevalues[:basen]):
            out_baseten_int += int(listofbasevalues.index(inputbase_n1[i]))* (int(basen)**i)
        else: 
            return None

    return out_baseten_int

def baseintoverflowdect (basen1, basen2, inputbase_n):
    currentb1val = convert_basentobaseten(int(basen1), inputbase_n)
    maxb2 = convert_basentobaseten(int(basen2), listtostr(maxcharlen*conv_10pl_equiv([basen2-1], "to")))
    return True if (currentb1val>maxb2) else False


def conv_10pl_equiv(inputd, mode):
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

    return listtostr(conv_10pl_equiv(invertlist(returnlist), "to"))

#GUI Code
root = tk.Tk()

#Frame
frm = ttk.Frame(root, padding=75, width=75, height=75)
frm.grid()

#Image
im1 = tk.PhotoImage(file="assets/i4.ppm")

#Styles
qbtnstyle = ttk.Style().configure("QButton.TButton", foreground="red", background="red")
cbtnstyle = ttk.Style().configure("CButton.TButton", foreground="orange", background="orange")
sbbtnstyle = ttk.Style().configure("SbButton.TButton", foreground="green", background="green")
swbtnstyle = ttk.Style().configure("SwButton.TButton", foreground="blue", background="blue")
ebtnstyle = ttk.Style().configure("EButton.TButton", foreground="ivory4", background="ivory4")

#Functions
def parseinput (base1, base2, inputmain):
    if type(convert_basentobaseten(int(base1), inputmain)) != int:
        throwerr("Error Code 1")
    elif base1 == 0 or base2 == 0:
        throwerr("Error Code 2")
    elif inputmain == "0" or inputmain == "":
        entry1var.set(inputmain)
        resultlabelvar.set(inputmain)
        return
    elif baseintoverflowdect(base1, base2, inputmain):
        throwerr("Error Code 3")
        return
    else:
        r = (convert_bases(base1, base2, inputmain))
        resultlabelvar.set(r)

def clear_result():
    resultlabelvar.set()
    entry1var.set()
    menu1.set("Select an option")
    menu2.set("Select an option")

def throwerr (errt):
    resultlabelvar.set(errt)

def swapinputs (base1, base2, inputmain, outputmain):
    tempsort = lambda x: "" if (str(x).count("Error") == 1) else x
    tempstorage = [tempsort(i) for i in [base1, base2, inputmain, outputmain]]
    menu1.set(lopts[tempstorage[1]])
    menu2.set(lopts[tempstorage[0]])
    print(tempstorage)
    entry1var.set(tempstorage[3])
    resultlabelvar.set(tempstorage[2])
    parseinput(menu1.current(), menu2.current(), entry1var.get())

def errorcodesmenu ():
    rooterr = tk.Toplevel(root)
    frmerr = ttk.Frame(rooterr, padding=50, width=25, height=50)
    frmerr.grid()
    ttk.Label(frmerr, image=(im1), compound='image').grid(column=0, row=0)
    frmerr2 = ttk.Frame(frmerr, width=25, height=50, borderwidth=2, relief="solid")
    frmerr2.grid(column=0, row=2, pady=10)
    ttk.Label(frmerr, justify=tk.CENTER, anchor=tk.CENTER, text="Error Codes", font=('Arial', 24)).grid(column=0, row=1, pady=10)
    ttk.Label(frmerr2, justify=tk.CENTER, anchor=tk.CENTER, text="Error Code 1: Value Not in Accepted List of Base Values", font=('Arial', 10)).grid(column=0, row=0, pady=5)
    ttk.Label(frmerr2, justify=tk.CENTER, anchor=tk.CENTER, text="Error Code 2: Input Base or Output Base Not Defined", font=('Arial', 10)).grid(column=0, row=1, pady=5)
    ttk.Label(frmerr2, justify=tk.CENTER, anchor=tk.CENTER, text="Error Code 3: Input Value Too Large for Output Base", font=('Arial', 10)).grid(column=0, row=2, pady=5)
    ttk.Button(frmerr, text="Back", style="BButton.TButton", command=rooterr.destroy).grid(column=0, row=3, pady=10)
    rooterr.title("nBasen: Error Codes")
    rooterr.wm_resizable(False, False)
    rooterr.wm_iconbitmap("assets/i4.ico")
    rooterr.mainloop()

#Components
ttk.Label(frm, image=(im1), compound='image').grid(column=0, row=0)
inval1 = tk.StringVar(frm)
inval2 = tk.StringVar(frm)
menu1 = ttk.Combobox(frm,textvariable=inval1)
menu2 = ttk.Combobox(frm,textvariable=inval2)
menu1.state(["readonly"])
menu2.state(["readonly"])
menu1.set("Select an option")
menu2.set("Select an option")
lopts = ["Select an option", "Base 1", 
        "Base 2", "Base 3", "Base 4", 
        "Base 5", "Base 6", "Base 7", 
        "Base 8", "Base 9", "Base 10", 
        "Base 11","Base 12", "Base 13", 
        "Base 14", "Base 15", "Base 16"]
menu1["values"] = lopts
menu2["values"] = lopts
menu1.grid(column=0, row=1, pady=5)
menu2.grid(column=0, row=3)
entry1var = tk.StringVar()
entry1 = tk.Entry(frm, textvariable=entry1var, font=('Arial', 12), 
        width=maxcharlen, justify=tk.CENTER, exportselection=0)
entry1.grid(column=0, row=2, pady=4)
submitbtn = ttk.Button(frm, text="Submit", style="SbButton.TButton",
        command=lambda: parseinput(menu1.current(), menu2.current(), entry1var.get()))
submitbtn.grid(column=0, row=5, pady=4)
clearbtn = ttk.Button(frm, text="Clear", style="CButton.TButton",
        command=lambda: clear_result())
clearbtn.grid(column=0, row=6, pady=4)
swapbtn = ttk.Button(frm, text="Swap", style="SwButton.TButton",
        command=lambda: swapinputs(menu1.current(), menu2.current(), entry1.get(), resultlabelvar.get()))
swapbtn.grid(column=0, row=7, pady=4)
errcbtn = ttk.Button(frm, text="Error Codes", style="EButton.TButton", 
        command=lambda: errorcodesmenu())
errcbtn.grid(column=0, row=8, pady=4)
resultlabelvar = tk.StringVar()
resultlabel = ttk.Label(frm, justify=tk.CENTER, anchor=tk.CENTER, font=('Arial', 12), borderwidth=2, relief="solid", width=maxcharlen, textvariable=resultlabelvar)
resultlabel.grid(column=0, row=4, pady=4)
ttk.Button(frm, text="Quit", style="QButton.TButton", command=root.destroy).grid(column=0, row=9, pady=10, padx=50)
#Configurations
root.title("nBasen")
root.wm_resizable(False, False)
root.wm_iconbitmap("assets/i4.ico")
root.mainloop()