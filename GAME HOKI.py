from tkinter import *
layar=Tk()
layar.title("Papan Taruhan")
layar.configure(background="tan")
masukan=StringVar()

operator=""

def toss():
    global operator
    for i in range(1,3):
        from random import randint
        y=randint(1,6)
        operator=operator+str(y)
    if operator=="00":
        masukan.set("You Win")
    elif operator=="11":
        masukan.set("You Win")
    elif operator=="22":
        masukan.set("You Win")
    elif operator=="33":
        masukan.set("You Win")
    elif operator=="44":
        masukan.set("You Win")
    elif operator=="55":
        masukan.set("You Win")
    elif operator=="66":
        masukan.set("You Win")
    else:
        masukan.set(operator)
        
def hapus():
    global operator
    operator=""
    masukan.set("")
 
#desain GUI
tombol=Entry(layar,bd=25,bg="snow",
font=("arial",25,"bold"),relief="ridge",
textvariable=masukan,justify="right")
tombol.grid(columnspan=4)
    
#tombol player 1
tblpla1=Button(layar,bd=20,font=("arial",15,"bold"),
bg="deepskyblue",text="PLAYER 1",relief="raised")
tblpla1.grid(row=2 ,column=0)

#tombol vs
tblvs=Button(layar,bd=20,font=("arial",15,"bold"),
bg="peachpuff",text="VS",relief="raised")
tblvs.grid(row=2,column=1)


#tombol player 2
tblpla2=Button(layar,bd=20,font=("arial",15,"bold"),
bg="deepskyblue",text="PLAYER 2",relief="raised")
tblpla2.grid(row=2,column=2)

#tombol delete
tbldelete=Button(layar,bd=20,font=("arial",15,"bold"),
bg="darkorange",text="DELETE",relief="raised",command=hapus)
tbldelete.grid(row=3,column=1)

#tombol roll
tblroll=Button(layar,bd=20,font=("arial",15,"bold"),
bg="cyan",text="ROLL",relief="raised",command=toss)
tblroll.grid(row=3,column=0)

#tombol roll
tblroll=Button(layar,bd=20,font=("arial",15,"bold"),
bg="cyan",text="ROLL",relief="raised",command=toss)
tblroll.grid(row=3,column=2)   

    
