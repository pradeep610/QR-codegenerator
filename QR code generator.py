


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import pyqrcode
from PIL import Image, ImageTk
import os

def showimage():
     fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("All Files","*.*")))
     img = Image.open(fln)
     img.thumbnail((250,250))

     img = ImageTk.PhotoImage(img)
     lbl.configure(image=img)
     lbl.image = img
     print(type(lbl.image))
     global Qr,Qr_output
     if   lbl.image:
          Qr = pyqrcode.create(img.format)
          Qr_output = BitmapImage(data = Qr.xbm(scale = 8), foreground="black", background="white")
     else:
          messagebox.showerror("Image Not Found","Select image First")
     try:
        show()
     except:
        pass

def generate():                                                # QR Code generation function
    global Qr,Qr_output
    if len(subject.get())==0:
        messagebox.showerror("Enter a subject","Please Enter a Text / Url")
    else:
        Qr = pyqrcode.create(subject.get())
        Qr_output = BitmapImage(data = Qr.xbm(scale = 8), foreground="black", background="white")
    try:
        show()
    except:
        pass
     
     
def show():                                                    # displaying image
    image.config(image=Qr_output)

def save():                                                    # saving function
    dir = os.getcwd() + "\\QR Codes"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(fname.get())!=0:
            Qr.png(os.path.join(dir,fname.get()+".png"),scale = 6)
        elif len(fname.get())==0:
            messagebox.showerror("Filename is Empty","File Name couldn't be Empty")
    except:
        messagebox.showerror("Generate a  QR Code first"," Generate a  QR Code first")

def reset():
     genentry.delete(0,END)
     genentry.config(bg='white')

     fentry.delete(0,END)
     fentry.config(bg = 'white')

     Qr_output.__del__()
        
mainwindow = Tk()
mainwindow.title("QR Code Generator")
mainwindow.config(bg='plum1')
mainwindow.geometry("1200x500")



Name = Label(mainwindow,text="QR Code Generator ",bg='yellow',fg='blue',font=('forte',35,'bold'))
Name.grid(row = 0,column=2)

gentext = Label(mainwindow ,text="Enter Text / Url etc",font=('italic',35,'bold'),fg = 'red',bd = 3,bg = "plum1")              # subject to generate code of
gentext.grid(row=1,column=0)

subject = StringVar()
genentry = Entry(mainwindow,textvariable = subject,width=30,font = "times 20")
genentry.grid(row=1,column=3)

filename1 = Label(mainwindow , text="Enter File Name to Save",font=('italic',30,'bold'),fg = 'red',bd = 3,bg = "plum1")        # filename for saving
filename1.grid(row=2, column=0)

fname = StringVar()
fentry = Entry(mainwindow, textvariable= fname,width=30,font = "times 20")
fentry.grid(row=2 , column=3)

filename2 = Label(mainwindow , text="Convert Image to QRCode",font=('italic',30,'bold'),fg = 'red',bd = 3,bg = "plum1")        # filename for saving
filename2.grid(row=3, column=0)

btn = Button(mainwindow, text = "Browse Image",bg='violet',fg='red',font = ("times 25",25,'bold','italic'), width=20, command = showimage)
btn.grid(row =3,column=3)

genb = Button(mainwindow,text="Generate",command = generate,bg='silver',fg='darkolivegreen4',activebackground='blue',width=10,activeforeground='yellow',font = ("times 20",25,'bold','italic'))    # Creating "save as" and "generate" buttons
genb.grid(row=5, column=2)

savb = Button(mainwindow ,text="Save",bg='orange',width=10,command = save,font = ("times 20",25,'bold','italic'))
savb.grid(row=5, column=3)

resetApp= Button(mainwindow,text='Reset',bg='black',fg='white',font = ("times 20",25,'bold','italic'), width=10,command=reset)
resetApp.grid(row=6,column=3)

image = Label(mainwindow)                                       # Placing QR Code into the main window
image.grid(row=6,column=2)

lbl = Label(mainwindow)
lbl.grid(row =2,column=2)

btn2 = Button(mainwindow, text = "Exit", bg='black',fg='white',font = ("times 20",25,'bold','italic'), width=10, command = lambda: exit())
btn2.grid(row =7,column=3)

rows = 7
columns = 4

for row in range(rows+1):
    mainwindow.grid_rowconfigure(row,weight=1)

for column in range(columns+1):
    mainwindow.grid_columnconfigure(column,weight=1)

mainwindow.mainloop()
