from Tkinter import *
import top_block as tb

global E1

def callback():
    print(E1.get())
    file = open("file.txt", "w")
    file.write(E1.get())
    file.close()
    tb.main()

top = Tk()
L1 = Label(top, text="Mensagem")
L1.grid(row=0, column=0)
E1 = Entry(top, bd = 5)
E1.grid(row=0, column=1)

MyButton1 = Button(top, text="Submit", width=10, command=callback)
MyButton1.grid(row=1, column=1)

top.mainloop()
