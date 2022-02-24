from tkinter import *#memanggil modul tkinter
from math import sin,cos,tan#memanggil modul sin,cos,tan di modul math
layar=Tk()#layar nama dari tkinter
layar.title("Kalkulator")#membuat title  dari tkinter
layar.configure(background="lightskyblue")#warna background dari tkinter
text_masukan=StringVar()#mendeklarasikan teks masukan

operator=""
    
def keluaran(numbers):#fungsi keluaran
    from math import pi
    global operator
    if numbers=="π":
        numbers=round(pi,2)
    operator=operator+str(numbers) #memasukkan hasil operator ke dalam teks masukkan
    text_masukan.set(operator)   
    
def hapussemua():# fungsi hapus
    global operator
    operator=""
    text_masukan.set("")#menghapus semua operator dan numbers yang ada di teks masukan
            
def cetakhasil():
    try:
        global operator
        cetak=eval(operator)#logika dari operator matematika
        text_masukan.set(cetak)#memasukan hasil ke teks masukan
    except:
        text_masukan.set("ERROR")
        
#Kolom keluaran
tombol=Entry(layar,bd=20,bg="snow",
font=("arial",25,"bold"),relief="ridge",
textvariable=text_masukan,justify="right")
tombol.grid(columnspan=4)

#tombol row pertama
tblsin=Button(layar,bd=5,font=("arial",20,"bold"),
bg="peachpuff",text="Sin",relief="raised",
command=lambda:keluaran("sin"))
tblsin.grid(row=1,column=0)

tblcos=Button(layar,bd=5,font=("arial",20,"bold"),
bg="peachpuff",text="Cos",relief="raised",
command=lambda:keluaran("cos"))
tblcos.grid(row=1,column=1)

tbltan=Button(layar,bd=5,font=("arial",20,"bold"),
bg="peachpuff",text="Tan",relief="raised",
command=lambda:keluaran("tan"))
tbltan.grid(row=1,column=2)

tblpangkat=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text="^",relief="groove",
command=lambda:keluaran("**"))
tblpangkat.grid(row=1,column=3)


#tombol row ke dua
tbl1=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text=1,relief="groove",
command=lambda:keluaran(1))
tbl1.grid(row=2,column=0)

tbl2=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text=2,relief="groove",
command=lambda:keluaran(2))
tbl2.grid(row=2,column=1)

tbl3=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text=3,relief="groove",
command=lambda:keluaran(3))
tbl3.grid(row=2,column=2)

plus=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text="+",relief="groove",
command=lambda:keluaran("+"))
plus.grid(row=2,column=3)


#tombol row ke tiga
tbl4=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text=4,relief="groove",
command=lambda:keluaran(4))
tbl4.grid(row=3,column=0)

tbl5=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text=5,relief="groove",
command=lambda:keluaran(5))
tbl5.grid(row=3,column=1)

tbl6=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text=6,relief="groove",
command=lambda:keluaran(6))
tbl6.grid(row=3,column=2)

kurang=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text="-",relief="groove",
command=lambda:keluaran("-"))
kurang.grid(row=3,column=3)


#tombol row ke empat
tbl7=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text="7",relief="groove",
command=lambda:keluaran(7))
tbl7.grid(row=4,column=0)

tbl8=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text=8,
relief="groove",command=lambda:keluaran(8))
tbl8.grid(row=4,column=1)

tbl9=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",relief="groove",text=9,
command=lambda:keluaran(9))
tbl9.grid(row=4,column=2)

kali=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",relief="groove",text="x",
command=lambda:keluaran("*"))
kali.grid(row=4,column=3)

#tombol row ke lima
tblkoma=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text=".",relief="groove",
command=lambda:keluaran("."))
tblkoma.grid(row=5,column=0)

tbl0=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text=0,relief="groove",
command=lambda:keluaran(0))
tbl0.grid(row=5,column=1)

tblhasil=Button(layar,bd=10,font=("arial",20,"bold"),
bg="darksalmon",text="=",relief="groove",
command=cetakhasil)
tblhasil.grid(row=5,column=2)

bagi=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text="/",relief="groove",
command=lambda:keluaran("/"))
bagi.grid(row=5,column=3)

#tombol hapus
hapus=Button(layar,bd=10,bg="orange",
font=("arial",20,"bold"),text="C",
relief="groove",command=hapussemua)
hapus.grid(row=6,column=0)

#tombol pi
pi=Button(layar,bd=10,bg="peachpuff",
font=("arial",20,"bold"),text="π",
relief="groove",command=lambda:keluaran("π"))
pi.grid(row=6,column=1)

#tombol buka kurung
bk=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text="(",relief="groove",
command=lambda:keluaran("("))
bk.grid(row=6,column=2)

#Tombol tutup kurung
tk=Button(layar,bd=10,font=("arial",20,"bold"),
bg="peachpuff",text=")",relief="groove",
command=lambda:keluaran(")"))
tk.grid(row=6,column=3)

layar.mainloop()
