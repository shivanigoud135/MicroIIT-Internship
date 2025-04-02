from tkinter import *
root =Tk()
root.title("Calculator App")
s=Entry(root,width=30,borderwidth=30,fg="blue")
s.grid(row=0,column=0,columnspan=40,padx=20,pady=30)

def buttonClick(number):
    cur=s.get()
    s.delete(0, END)
    s.insert(0, str(cur) + str(number))

def clear():
    s.delete(0, END)

def buttonadd():
    firstnum=s.get()
    global fnum
    global math
    math="add"
    fnum=int(firstnum)
    s.delete(0, END)

def equal():
    secondnum=s.get()
    s.delete(0,END)

    if math=="add":
        s.insert(0,fnum + int(secondnum))
    elif math=="sub":
        s.insert(0,fnum - int(secondnum))
    elif math=="mul":
        s.insert(0,fnum * int(secondnum))
    elif math=="div":
        s.insert(0,fnum / int(secondnum))
    elif math=="pow":
        s.insert(0,fnum ** int(secondnum))


def sub():
    firstnum=s.get()
    global fnum
    global math
    math="sub"
    fnum=int(firstnum)
    s.delete(0, END)
    return

def mul():
    firstnum=s.get()
    global fnum
    global math
    math="mul"
    fnum=int(firstnum)
    s.delete(0, END)
    return

def div():
    firstnum=s.get()
    global fnum
    global math
    math="div"
    fnum=int(firstnum)
    s.delete(0, END)
    return

def pow():
    firstnum=s.get()
    global fnum
    global math
    math="pow"
    fnum=int(firstnum)
    s.delete(0, END)
    return

button1 = Button(root,text="1",padx=35,pady=15,command=lambda:buttonClick(1))
button2 = Button(root,text="2",padx=35,pady=15,command=lambda:buttonClick(2))
button3 = Button(root,text="3",padx=35,pady=15,command=lambda:buttonClick(3))
button4 = Button(root,text="4",padx=35,pady=15,command=lambda:buttonClick(4))
button5 = Button(root,text="5",padx=35,pady=15,command=lambda:buttonClick(5))
button6 = Button(root,text="6",padx=35,pady=15,command=lambda:buttonClick(6))
button7 = Button(root,text="7",padx=35,pady=15,command=lambda:buttonClick(7))
button8 = Button(root,text="8",padx=35,pady=15,command=lambda:buttonClick(8))
button9 = Button(root,text="9",padx=35,pady=15,command=lambda:buttonClick(9))
button0 = Button(root,text="0",padx=35,pady=15,command=lambda:buttonClick(0))

buttonAdd=Button(root,text='+',padx=35,pady=15,command=buttonadd)
buttonSub=Button(root,text='-',padx=35,pady=15,command=sub)
buttonMul=Button(root,text='*',padx=35,pady=15,command=mul)
buttonDiv=Button(root,text='/',padx=35,pady=15,command=div)
buttonEqul=Button(root,text='=',padx=35,pady=15,command=equal)
buttonClear=Button(root,text='clear',padx=30,pady=15,command=clear)
buttonPow=Button(root,text='**',padx=35,pady=15,command=pow)
buttonQuit=Button(root,text='exit',padx=30,pady=15,command=root.quit)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
buttonAdd.grid(row=4,column=1)
buttonSub.grid(row=4,column=2)
buttonMul.grid(row=5,column=0)
buttonDiv.grid(row=5,column=1)
buttonPow.grid(row=5,column=2)
buttonQuit.grid(row=6,column=0)
buttonClear.grid(row=6,column=1)
buttonEqul.grid(row=6,column=2)
root.mainloop()