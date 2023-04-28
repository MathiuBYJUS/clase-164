
from tkinter import * 
from PIL import ImageTk, Image
from tkinter import ttk


root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.configure(background="lightblue")

imagen1= ImageTk.PhotoImage(Image.open("earth.jpg"))
Mercury = ImageTk.PhotoImage(Image.open ("mercury.jpg"))
imagen3= ImageTk.PhotoImage(Image.open("venus.jpg"))

label_1=Label(root,text="Planetas :",bg="lightgreen",font=15)
label_1.place(relx=0.1 , rely=0.1, anchor=CENTER)
label_2=Label(root,text="Planeta", font=("courier",15))
label_2.place(relx=0.3 ,rely=0.3 , anchor=CENTER)
label_3=Label(root,text="",highlightthickness="5",borderwidth=1,bg="gold",relief="solid")
label_3.place(relx=0.5 , rely=0.5, anchor=CENTER)
label_4=Label(root,text="Informacion")
label_4.place(relx=0.5,rely=0.7 , anchor=CENTER)
label_5=Label(root,text="info",bg="lightgreen",font=("arial",10))
label_5.place(relx=0.5 , rely=0.9,anchor=CENTER)

array1=["Mercury","Earth","Venus"]
a=StringVar()
b=ttk.Combobox(root,values=a,textvariable=b)


root.mainloop()
