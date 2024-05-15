from tkinter import *

def cavemrrd():
    concave_mirror["fg"] = "#dddddd"
    concave_mirror["bg"] = "#222222"
    concave_mirror["font"] = ("Calibri Light", 18, "italic")
    concave_lens["fg"] = "black"
    concave_lens["bg"] = "#b0b0b0"
    concave_lens["font"] = ("Calibri Light", 18)
    convex_lens["fg"] = "black"
    convex_lens["bg"] = "#b0b0b0"
    convex_lens["font"] = ("Calibri Light", 18)
    convex_mirror["fg"] = "black"
    convex_mirror["bg"] = "#b0b0b0"
    convex_mirror["font"] = ("Calibri Light", 18)

def vexmrrd():
    convex_mirror["fg"] = "#dddddd"
    convex_mirror["bg"] = "#222222"
    convex_mirror["font"] = ("Calibri Light", 18, "italic")
    concave_mirror["fg"] = "black"
    concave_mirror["bg"] = "#b0b0b0"
    concave_mirror["font"] = ("Calibri Light", 18)
    concave_lens["fg"] = "black"
    concave_lens["bg"] = "#b0b0b0"
    concave_lens["font"] = ("Calibri Light", 18)
    convex_lens["fg"] = "black"
    convex_lens["bg"] = "#b0b0b0"
    convex_lens["font"] = ("Calibri Light", 18)

def cavelnsd():
    concave_lens["fg"] = "#dddddd"
    concave_lens["bg"] = "#222222"
    concave_lens["font"] = ("Calibri Light", 18, "italic")
    convex_mirror["fg"] = "black"
    convex_mirror["bg"] = "#b0b0b0"
    convex_mirror["font"] = ("Calibri Light", 18)
    concave_mirror["fg"] = "black"
    concave_mirror["bg"] = "#b0b0b0"
    concave_mirror["font"] = ("Calibri Light", 18)
    convex_lens["fg"] = "black"
    convex_lens["bg"] = "#b0b0b0"
    convex_lens["font"] = ("Calibri Light", 18)

def vexlnsd():
    convex_lens["fg"] = "#dddddd"
    convex_lens["bg"] = "#222222"
    convex_lens["font"] = ("Calibri Light", 18, "italic")
    convex_mirror["fg"] = "black"
    convex_mirror["bg"] = "#b0b0b0"
    convex_mirror["font"] = ("Calibri Light", 18)
    concave_mirror["fg"] = "black"
    concave_mirror["bg"] = "#b0b0b0"
    concave_mirror["font"] = ("Calibri Light", 18)
    concave_lens["fg"] = "black"
    concave_lens["bg"] = "#b0b0b0"
    concave_lens["font"] = ("Calibri Light", 18)

def cleard():
    convex_mirror["fg"] = "black"
    convex_mirror["bg"] = "#b0b0b0"
    convex_mirror["font"] = ("Calibri Light", 18)
    concave_mirror["fg"] = "black"
    concave_mirror["bg"] = "#b0b0b0"
    concave_mirror["font"] = ("Calibri Light", 18)
    concave_lens["fg"] = "black"
    concave_lens["bg"] = "#b0b0b0"
    concave_lens["font"] = ("Calibri Light", 18)
    convex_lens["fg"] = "black"
    convex_lens["bg"] = "#b0b0b0"
    convex_lens["font"] = ("Calibri Light", 18)

    ue.delete(0, END)
    ve.delete(0, END)
    hie.delete(0, END)
    hoe.delete(0, END)
    me.delete(0, END)
    fe.delete(0, END)

def calculated():
    if (concave_mirror["fg"] == "#dddddd" ):
        temp1=1
    elif(convex_mirror["fg"] == "#dddddd"):
        temp1=2
    elif(concave_lens["fg"] == "#dddddd"):
        temp1=3
    elif(convex_lens["fg"] == "#dddddd"):
        temp1=4
    else:
        print("error_code: 01")
    
    if ue.get()!="":
        u=float(ue.get())
    else: u=-1
    if ve.get()!="":
        v=float(ve.get())
    if hoe.get()!="":
        ho=float(hoe.get())
    else:
        ho=1
    if hie.get()!="":
        hi=float(hie.get())
    if me.get()!="":
        m=float(me.get())
    if fe.get()!="":
        f=float(fe.get())

    if temp1==1 or temp1==2:
        
        # mirror

        # m=hi/ho
        # m=-1*(v/u)
        # f=(v*u)/(v+u)

        # hi=m*ho
        # ho=hi/m

        # u=-1*(v/m)
        # v=-1*u*m

        # v=(u*f)/(u-f)
        # u=(v*f)/(v-f)

        if u>=0 or ho<=0:
            print("error_code: 03")
        else:
            if ve.get()!="" and ue.get()!="":
                calcmm()
                calcmf()
                calchiorho()
            elif ue.get()!="" and fe.get()!="":
                calcmv()
                calcmm()
                calchiorho()
            elif ve.get()!="" and fe.get()!="":
                calcmu()
                calcmm()
                calchiorho()
            elif ue.get()!="" and me.get()!="":
                calcmv()
                calcmf()
                calchiorho()
            elif ve.get()!="" and me.get()!="":
                calcmu()
                calcmf()
                calchiorho()
            elif hie.get()!="" and hoe.get()!="":
                calcmm()
                if ue.get()!="":
                    calcmf()
                    calcmv()
                elif ve.get()!="":
                    calcmf()
                    calcmu()        
                else:
                    print("error_code: 10")
    
    elif temp1==3 or temp1==4:
        
        # lens

        # m=hi/ho
        # m=v/u
        # f=(v*u)/(u-v)

        # ho=hi/m
        # hi=m*ho

        # v=m*u
        # u=v/m

        # u=(f*v)/(f-v)
        # v=(f*u)/(f+u)

        if u>=0 or ho<=0:
            print("error_code: 03")
        else:
            if ve.get()!="" and ue.get()!="":
                calclm()
                calclf()
                calchiorho()
            elif ue.get()!="" and fe.get()!="":
                calclv()
                calclm()
                calchiorho()
            elif ve.get()!="" and fe.get()!="":
                calclu()
                calclm()
                calchiorho()
            elif ue.get()!="" and me.get()!="":
                calclv()
                calclf()
                calchiorho()
            elif ve.get()!="" and me.get()!="":
                calclu()
                calclf()
                calchiorho()
            elif hie.get()!="" and hoe.get()!="":
                calclm()
                if ue.get()!="":
                    calclf()
                    calclv()
                elif ve.get()!="":
                    calclf()
                    calclu()        
                else:
                    print("error_code: 16")

    else:
        print("error_code: 11")

def calchiorho():
    if hie.get()!="":
        calcho()
    elif hoe.get()!="":
        calchi()
    else:
        print("error_code: 02")

def calcmu():
    if ve.get()!="" and me.get()!="":
        v=float(ve.get())
        m=float(me.get())
        u=-1*(v/m)
        if u>0:
            u*=-1
    elif ve.get()!="" and fe.get()!="":
        v=float(ve.get())
        f=float(fe.get())
        u=(v*f)/(v-f)
        if u>0:
            u*=-1
    else:
        print("error_code: 04")
    ue.delete(0, END)
    ue.insert(0, str(u))

def calclu():
    if ve.get()!="" and me.get()!="":
        v=float(ve.get())
        m=float(me.get())
        u=v/m
    elif ve.get()!="" and fe.get()!="":
        v=float(ve.get())
        f=float(fe.get())
        u=(f*v)/(f-v)
    else:
        print("error_code: 012")
    ue.delete(0, END)
    ue.insert(0, str(u))

def calcmv():
    if ue.get()!="" and me.get()!="":
        u=float(ue.get())
        m=float(me.get())
        v=-1*u*m
    elif ue.get()!="" and fe.get()!="":
        u=float(ue.get())
        f=float(fe.get())
        v=(u*f)/(u-f)
    else:
        print("error_code: 05")
    ve.delete(0, END)
    ve.insert(0, str(v))

def calclv():
    if ue.get()!="" and me.get()!="":
        u=float(ue.get())
        m=float(me.get())
        v=m*u
    elif ue.get()!="" and fe.get()!="":
        u=float(ue.get())
        f=float(fe.get())
        v=(f*u)/(f+u)
    else:
        print("error_code: 13")
    ve.delete(0, END)
    ve.insert(0, str(v))

def calcmf():
    if ue.get()!="" and ve.get()!="":
        v=float(ve.get())
        u=float(ue.get())
        f=(v*u)/(v+u)
    else:
        print("error_code: 06")
    fe.delete(0, END)
    fe.insert(0, str(f))

def calclf():
    if ue.get()!="" and ve.get()!="":
        v=float(ve.get())
        u=float(ue.get())
        f=(v*u)/(u-v)
    else:
        print("error_code: 14")
    fe.delete(0, END)
    fe.insert(0, str(f))

def calcmm():
    if hie.get()!="" and hoe.get()!="":
        hi=float(hie.get())
        ho=float(hoe.get())
        m=hi/ho
    elif ue.get()!="" and ve.get()!="":
        u=float(ue.get())
        v=float(ve.get())
        m=-1*(v/u)
    else:
        print("error_code: 07")
    me.delete(0, END)
    me.insert(0, str(m))

def calclm():
    if hie.get()!="" and hoe.get()!="":
        hi=float(hie.get())
        ho=float(hoe.get())
        m=hi/ho
    elif ue.get()!="" and ve.get()!="":
        u=float(ue.get())
        v=float(ve.get())
        m=v/u
    else:
        print("error_code: 15")
    me.delete(0, END)
    me.insert(0, str(m))

def calchi():
    if me.get()!="" and hoe.get()!="":
        m=float(me.get())
        ho=float(hoe.get())
        hi=m*ho
    else:
        print("error_code: 08")
    hie.delete(0, END)
    hie.insert(0, str(hi))

def calcho():
    if me.get()!="" and hie.get()!="":
        m=float(me.get())
        hi=float(hie.get())
        ho=hi/m
    else:
        print("error_code: 09")
    hoe.delete(0, END)
    hoe.insert(0, str(ho))

root = Tk()
root.geometry("281x495+100+100")
root.title("LIGHT")
root.configure(background="#222222")


cavemrr = """Concave
Mirror"""
vexmrr = """Convex
Mirror"""
cavelns = """Concave
Lens"""
vexlns = """Convex
Lens"""

concave_mirror = Button(root, command=cavemrrd, text=cavemrr, font=("Calibri Light", 18), fg="black", bg="#b0b0b0", borderwidth=0, width=10)
concave_mirror.place(x=10,y=10)

convex_mirror = Button(root, command=vexmrrd, text=vexmrr, font=("Calibri Light", 18), fg="black", bg="#b0b0b0", borderwidth=0, width=10)
convex_mirror.place(x=146,y=10)

concave_lens = Button(root, command=cavelnsd, text=cavelns, font=("Calibri Light", 18), fg="black", bg="#b0b0b0", borderwidth=0, width=10)
concave_lens.place(x=10,y=96)

convex_lens = Button(root, command=vexlnsd, text=vexlns, font=("Calibri Light", 18), fg="black", bg="#b0b0b0", borderwidth=0, width=10)
convex_lens.place(x=146,y=96)

ul = Label(root, text="u", font=("Calibri Light", 18), bg="#222222", fg="white").place(x=20,y=190)
ue = Entry(root, font=("Calibri Light", 18), width=6, borderwidth=0, bg="#b0b0b0")
ue.place(x=45,y=195)

vl = Label(root, text="v", font=("Calibri Light", 18), bg="#222222", fg="white").place(x=150,y=190)
ve = Entry(root, font=("Calibri Light", 18), width=6, borderwidth=0, bg="#b0b0b0")
ve.place(x=175,y=195)

hil = Label(root, text="hi", font=("Calibri Light", 18), bg="#222222", fg="white").place(x=18,y=250)
hie = Entry(root, font=("Calibri Light", 18), width=6, borderwidth=0, bg="#b0b0b0")
hie.place(x=45,y=255)

hol = Label(root, text="ho", font=("Calibri Light", 18), bg="#222222", fg="white").place(x=140,y=250)
hoe = Entry(root, font=("Calibri Light", 18), width=6, borderwidth=0, bg="#b0b0b0")
hoe.place(x=175,y=255)

ml = Label(root, text="m", font=("Calibri Light", 18), bg="#222222", fg="white").place(x=20,y=310)
me = Entry(root, font=("Calibri Light", 18), width=6, borderwidth=0, bg="#b0b0b0")
me.place(x=45,y=315)

fl = Label(root, text="f", font=("Calibri Light", 18), bg="#222222", fg="white").place(x=150,y=310)
fe = Entry(root, font=("Calibri Light", 18), width=6, borderwidth=0, bg="#b0b0b0")
fe.place(x=175,y=315)

calculateb = Button(root, text="Calculate", fg="black", bg="#b0b0b0", font=("Calibri Light", 18), command=calculated, borderwidth=0, width=21)
calculateb.place(x=11,y=375)

clearb = Button(root, text="Reset", fg="black", bg="#b0b0b0", font=("Calibri Light", 18), command=cleard, borderwidth=0, width=21)
clearb.place(x=11,y=435)

# warningl = Label(root, font=("Calibri Light", 18), fg="red", bg="#222222", text="""DO NOT ENTER
# NEGATIVE VALUES""")
# warningl.place(x=48,y=490)

root.mainloop()