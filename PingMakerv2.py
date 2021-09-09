from ping3 import ping, verbose_ping
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
numeroPantalla=StringVar()
v2=tk.StringVar()

a=0
b=0

################################################### Funciones de TK ###################################################
def Informacion():
    messagebox.showinfo("Informacion","Programa hacedor de ping")

def Contribucion():
    messagebox.showinfo("Borrar","Borrar")

def infoadicional():
    messagebox.showinfo("Aceca de","Redes: todos estan en mis redes")

def avisolicencia():
    messagebox.showwarning("licencia","producto sin licencia")  

def saliraplicacion(): 
    valor=messagebox.askokcancel("salir","deseas salir de la aplicacion") 
    
    if valor==TRUE: 
        root.destroy()

def cerrardocumento():
    valor=messagebox.askretrycancel("reintentar","deseas salir de la aplicacion") 
    if valor==FALSE:
        root.destroy()

################################################# Funciones Generales #################################################

def ip_checkv4(ip):
        parts=ip.split(".")
        if len(parts)<4 or len(parts)>4:
            return "Ip Invalida "
        else:
            while len(parts)== 4:
                a=int(parts[0])
                b=int(parts[1])
                c=int(parts[2])
                d=int(parts[3])
                if a<= 0 or a == 127 :
                    return "Ping a lookback supongo, no, este programa no te sera de ayuda"
                elif d == 0:
                    return "No lo se, ping a direcciones de Broadcast...."
                elif a>=255:
                    return "El valor de un Octeto no puede ser mayor de 255 o menor a 0"
                elif b>=255 or b<0: 
                  return   "El valor de un Octeto no puede ser mayor de 255 0 menor a 0"
                elif c>=255 or c<0:
                    return "El valor de un Octeto no puede ser mayor de 255 o menor a 0"
                elif d>=255 or d<0:
                    return "El valor de un Octeto no puede ser mayor de 255 o menor a 0"
                else:
                    return "1"

def Ejecutar():
    ipcheck=numeroPantalla.get()
    global a
    ipcheck.strip()
    if ipcheck!="":
         
        g=ip_checkv4(ipcheck)
        g.strip() 

        if g == "1":
            btn['state'] = 'disabled'
            pantalla['state'] = 'disabled'
            btnr['state'] = 'normal'
            try:
                #global b
                #b=1

                a=a+1
                #P= float(ipcheck)
                P="{0:.2f}".format(1000*ping(ipcheck))
                #lb.insert(0,"ping to: "+ str(ipcheck)+"  ...  "+str(P)+" ms "+", seq= "+ str(a))
                lb.insert(0,"ping to: "+ str(ipcheck)+"  ...  Seq = "+ str(a) + ", Time = " +  str(P)+" ms ")
                frame.after(1000, Ejecutar)
            except  TypeError :
                a=a-1
                lb.insert(0,"lost")
                frame.after(1000, Ejecutar)
            except OSError:
                a=a-1
                lb.insert(0,"Network inalcanzable")
                frame.after(1000, Ejecutar)
        
        else :
            messagebox.showinfo("aviso",ip_checkv4(ipcheck))

    else:
        pass
        messagebox.showinfo("aviso","Ingresa una IP")

def Limpieza():
    global a
    global b 
    lb.delete (0, last=a )
    a=0
    pantalla['state'] = 'normal'
    pantalla.delete(0,END)
    #pantalla.insert(0,"  ")
    #btn.after(100)
    btn['state'] = 'normal'     
    
def Comprobar():
    global b
    if b == 0:
        Limpieza()
    elif b==1:
        Ejecutar()



#######################################################################################################################

barraMenu=Menu(root)

root.config(bg="#03A9F4",menu=barraMenu,width=300,height=300)
root.title("Ping Maker")
root.resizable(0,0)
root.geometry("500x200")

#Label(root,text="Ping Maker",fg="white",font=("Arial", 20),bg="#03A9F4" ).place(x=190,y=10)

frame=Frame(root)
frame.config(bg="white",width=450,height=150)
frame.place(x=25,y=25)

Label(frame,text="Ip Ping Address: ",fg="black",font=("Arial", 10),bg="white" ).place(x=18,y=10)

####################################################### Botton ########################################################

pantalla = Entry(frame,textvariable=numeroPantalla, width=15)
pantalla.place(x=120,y=10)
pantalla.config(background="white",fg="black",justify="right")

btn = Button(frame,text="Do",padx="20",command=Ejecutar)
btn.place(x=280,y=5)

btnr = Button(frame,text="Retry",padx="20",command=Limpieza)
btnr.place(x=350,y=5)
btnr['state'] = 'disabled'

lb=tk.Listbox(root,width=45,height=4,listvariable=v2)
lb.place(x=45,y=75)

################################################### Menu Superior #####################################################

AAyuda=Menu(barraMenu)
AAyuda=Menu(barraMenu,tearoff=0)

AAyuda.add_command(label="Informacion",command=Informacion)
AAyuda.add_command(label="Contribucion",command=Contribucion)
AAyuda.add_command(label="acerca de",command=infoadicional)

barraMenu.add_cascade(label="ayuda",menu=AAyuda)

#######################################################################################################################

root.mainloop()

#######################################################################################################################
