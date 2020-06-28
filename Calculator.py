from tkinter import *

window=Tk()
window.title("Calculator")
window.resizable(0, 0) #Don't allow resizing in the x or y direction
display_text = StringVar()
display_text1 = StringVar()
label=Label(window,width=60,height=5,text="0",anchor='e',bg="#d3dde0",textvariable=display_text)
label1=Label(window,width=60,anchor='se',bg="#d3dde0",textvariable=display_text1)
window.config(bg="#d3dde0")
window.iconbitmap("Calculator-icon.png")

def intermediate():
    intermediateValue = display_text.get()
    intermediateResult = eval(intermediateValue)
    display_text1.set(intermediateResult)

def buttonClick(num):
    value=display_text.get()
    display_text.set(value+num)
    intermediate()

def buttonAdding():


    display_text.set(str(display_text.get()) + "+")



def buttonSubtracting():


    display_text.set(str(display_text.get()) + "-")


def buttonDividing():


    display_text.set(str(display_text.get()) + "/")

def buttonMultiplying():


    display_text.set(str(display_text.get()) + "*")


def buttonEquals():
    newValue=display_text.get()
    result=eval(newValue)
    display_text.set(result)
    display_text1.set("")


def buttonClear():
    display_text.set("")


# Defining Buttons

button7=Button(window,text=7,width=15,height=4,activebackground="#172429",bg="#344b57",fg="white",command=lambda: buttonClick("7"))
button8=Button(window,text=8,width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command=lambda: buttonClick("8"))
button9=Button(window,text=9,width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command=lambda: buttonClick("9"))

button4=Button(window,text=4,width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command=lambda: buttonClick("4"))
button5=Button(window,text=5,width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command=lambda: buttonClick("5"))
button6=Button(window,text=6,width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command=lambda: buttonClick("6"))

button1=Button(window,text=1,width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command=lambda: buttonClick("1"))
button2=Button(window,text=2,width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command=lambda: buttonClick("2"))
button3=Button(window,text=3,width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command=lambda: buttonClick("3"))

buttonAdd=Button(window,text="+",width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command= buttonAdding)
buttonSubtract=Button(window,text="-",width=15,bg="#344b57",activebackground="#172429",fg="white",height=4,command= buttonSubtracting)
buttonDivide=Button(window,text="/",width=15,bg="#344b57",activebackground="#172429",fg="white",height=4,command= buttonDividing)
buttonMulty=Button(window,text="X",width=15,bg="#344b57",activebackground="#172429",fg="white",height=4,command=buttonMultiplying)

buttonZero=Button(window,text=0,width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command=lambda: buttonClick("0"))
buttonDot=Button(window,text=".",width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command=lambda: buttonClick("."))
buttonEqual=Button(window,text="=",width=15,height=4,bg="#344b57",activebackground="#172429",fg="white",command=buttonEquals)

buttonClear=Button(window,text="Clear",width=64,height=4,bg="#344b57",activebackground="#172429",fg="white",command=buttonClear)



label.grid(row=0,columnspan=4)
label1.grid(row=1,columnspan=4)

button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
buttonAdd.grid(row=2,column=3)

button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
buttonSubtract.grid(row=3,column=3)

button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
buttonDivide.grid(row=4,column=3)

buttonZero.grid(row=5,column=0)
buttonDot.grid(row=5,column=1)
buttonMulty.grid(row=5,column=2)
buttonEqual.grid(row=5,column=3)
buttonClear.grid(row=6,columnspan=5)






window.mainloop()