from tkinter import *



from tkinter import ttk
#definitionn de la fenetre

fenetre = Tk()
fenetre.title('Fenetre')
fenetre.geometry('600x500+320+110')
fenetre.configure(background='#CD6155')
def search():
    pass

#création des widghets
fr=Frame(fenetre,width='300',height='40')
fr.place(x=160,y=20)

champ=StringVar()
nom=Label(fr,textvar=champ,font=('arial',12,),bg='white')
nom.place(x=0,y=0,width=300,height=40)

#les fonctions des boutons
resu=True

def plus():
    cc=str(champ.get())
    champ.set(cc+'+')
    

def moins():
    champ.set(str(champ.get()) + '-') 

def produit():
    champ.set(str(champ.get()) + '*') 
def divi():
    champ.set(str(champ.get()) + '/') 

def mod():
    champ.set(str(champ.get()) + '%') 

def carre():
    champ.set(str(champ.get()) + '**') 

def egal():
    try:
        resultat=eval(champ.get())
        champ.set(''+str(resultat))
        resu=False
    except: champ.set('Erreur de signe quelque part !')

def vider():
    champ.set("")

def tan():
    pass

def racin( ):
    pass



def un():
    champ.set(str(champ.get()) + '1')

def deux():
    champ.set(str(champ.get()) + '2')

def trois():
    champ.set(str(champ.get()) + '3')

def qtr():
    champ.set(str(champ.get()) + '4')

def cnq():
    champ.set(str(champ.get()) + '5') 

def six():
    champ.set(str(champ.get()) + '6') 

def sept():
    champ.set(str(champ.get()) + '7')

def huit():
    champ.set(str(champ.get()) + '8')


def neuf():
    champ.set(str(champ.get()) + '9')


def zero():
    champ.set(str(champ.get()) + '0')



#grand frame

gr=Frame(fenetre,width='300',height='300',bg='blue')
gr.place(x=160,y=66)

#frame de signe

sign=Frame(gr,width='100',height='300',bg='green')
sign.place(x=238,y=0,width=62,height=300)


p=IntVar()
plus=Button(sign,text='+',font=('arial',14,'bold'),command=plus)
plus.place(x=12,y=10,width=40,height=40)

moin=Button(sign,text='-',font=('arial',14,'bold'),command=moins)
moin.place(x=12,y=50,width=40,height=40)

produit=Button(sign,text='×',font=('arial',14,'bold'),command=produit)
produit.place(x=12,y=90,width=40,height=40)

div=Button(sign,text='/',font=('arial',14,'bold'),command=divi)
div.place(x=12,y=130,width=40,height=40)

mod=Button(sign,text='MOD',font=('arial',10,'bold'),command=mod)
mod.place(x=12,y=170,width=40,height=40)

carre=Button(sign,text='x²',font=('arial',14,'bold'),command=carre)
carre.place(x=12,y=210,width=40,height=40)

egal=Button(sign,text='=',font=('arial',14,'bold'),bg='orange',fg='blue',command=egal)
egal.place(x=12,y=251,width=40,height=40)

sign=Frame(gr,width='100',height='300',bg='magenta')
sign.place(x=0,y=0,width=238,height=50)

dele=Button(sign,text='C',font=('arial',14,'bold','italic'),bg='red',fg='black',command=vider)
dele.place(x=9,y=6,width=44,height=40)

racine=Button(sign,text='√',font=('algerian',14,'bold'),bg='orange')
racine.place(x=55,y=6,width=43,height=40)

sin=Button(sign,text='sin',font=('arial',13,'bold'),bg='orange',)
sin.place(x=99,y=6,width=44,height=40)

cos=Button(sign,text='cos',font=('arial',13,'bold'),bg='orange',)
cos.place(x=145,y=6,width=47,height=40)

tan=Button(sign,text='tan',font=('arial',13,'bold'),bg='orange',)
tan.place(x=194,y=6,width=43,height=40)

#frame nombre1
nombre=Frame(gr,width='100',height='300',bg='pink')
nombre.place(x=0,y=50,width=238,height=60)



n=IntVar()
un=Button(nombre,text='1',font=('elephant',18,'bold'),bg='purple',fg='white',command=un)
un.place(x=9,y=6,width=76,height=50)

d=Button(nombre,text='2',font=('elephant',18,'bold'),bg='purple',fg='white',command=deux)
d.place(x=87,y=6,width=73,height=50)

tr=Button(nombre,text='3',font=('elephant',18,'bold'),bg='purple',fg='white',command=trois)
tr.place(x=161,y=6,width=76,height=50)

#frame nombre2

nombre=Frame(gr,width='100',height='300',bg='pink')
nombre.place(x=0,y=110,width=238,height=60)

quatre=Button(nombre,text='4',font=('elephant',18,'bold'),bg='purple',fg='white',command=qtr)
quatre.place(x=9,y=6,width=76,height=50)

cinq=Button(nombre,text='5',font=('elephant',18,'bold'),bg='purple',fg='white',command=cnq)
cinq.place(x=87,y=6,width=73,height=50)



six=Button(nombre, text='6', font=('elephant',18,'bold'), bg='purple', fg='white',command=six)
six.place(x=161,y=6,width=76,height=50)

#frame nombre3
nombre=Frame(gr,width='100',height='300',bg='pink')
nombre.place(x=0,y=170,width=238,height=60)

sept=Button(nombre,text='7',font=('elephant',18,'bold'),bg='purple',fg='white',command=sept)
sept.place(x=9,y=6,width=76,height=50)

huit=Button(nombre,text='8',font=('elephant',18,'bold'),bg='purple',fg='white',command=huit)
huit.place(x=87,y=6,width=73,height=50)

neuf=Button(nombre,text='9',font=('elephant',18,'bold'),bg='purple',fg='white',command=neuf)
neuf.place(x=161,y=6,width=76,height=50)

#dernier_frame_nombre

nombre=Frame(gr,width='100',height='300',bg='pink')
nombre.place(x=0,y=230,width=238,height=69)

#nombre0
neuf=Button(nombre,text='0',font=('elephant',18,'bold'),bg='purple',fg='white',command=zero)
neuf.place(x=9,y=6,width=228,height=50)


#nom.pack(side=LEFT,padx=5,pady=5)
#chpnom=Entry(fenetre, font=('arial',10,'bold'),bg='white', fg='blue')
#chpnom.grid(row=2, column=11, padx=0, pady=0)
"""
prenom=Label(fenetre, text='Prenom', font=('arial',12,'bold'),bg='white', fg='purple')
prenom.grid(row=3, column=10,padx=1,pady=0)
chpprenom=Entry(fenetre, font=('arial',10,'bold'),bg='white', fg='blue')
chpprenom.grid(row=3, column=11, padx=1, pady=0)

age=Label(fenetre, text='Age', font=('arial',12,'bold'),bg='white', fg='purple')
age.grid(row=4, column=10,padx=3,pady=27)
chpage=ttk.Combobox(fenetre, font=('arial',10,'bold'),values=[i for i in range(1,21)])
chpage.grid(row=4, column=11, padx=0, pady=0)

chp=Label(fenetre,text='')

valider=Button(fenetre,text='Rechercher', font=('arial',12,'bold'),bg='purple', fg='white',command=search)
valider.grid(row=5, column=11,padx=1,pady=0)

"""
fenetre.mainloop()