from tkinter import  CENTER, Tk, Button, Entry, Label, ttk, PhotoImage
from tkinter import  StringVar,Scrollbar,Frame
import tkinter as tk
import time
from turtle import rt

class Ventana(Frame):
	def __init__(self, master, *args):
		super().__init__( master,*args)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		self.menu = True
		self.color = True

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Alunas variables :)

		self.r= tk.StringVar()
		self.i= tk.StringVar()
		self.v2= tk.StringVar()
		self.r2= tk.StringVar()
		self.v3= tk.StringVar()
		self.i3= tk.StringVar()

		self.vp= tk.StringVar()
		self.rone= tk.StringVar()
		self.rtwo= tk.StringVar()
		self.rthree= tk.StringVar()

		self.rm1= tk.StringVar()
		self.rm1_1= tk.StringVar()
		self.rm1_2= tk.StringVar()
		self.im= tk.StringVar()
		self.rm= tk.StringVar()

		self.rm2= tk.StringVar()
		self.rm2_1= tk.StringVar()
		self.rm2_2= tk.StringVar()
		self.rm0= tk.StringVar()
		self.vm= tk.StringVar()

		self.vo2= tk.StringVar()
		self.in2= tk.StringVar()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		self.frame_inicio = Frame(self.master, bg='black', width=50, height=45)
		self.frame_inicio.grid_propagate(0)
		self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
		self.frame_menu = Frame(self.master, bg='black', width = 50)
		self.frame_menu.grid_propagate(0)
		self.frame_menu.grid(column=0, row = 1, sticky='nsew')
		self.frame_top = Frame(self.master, bg='black', height = 50)
		self.frame_top.grid(column = 1, row = 0, sticky='nsew')
		self.frame_principal = Frame(self.master, bg='black')
		self.frame_principal.grid(column=1, row=1, sticky='nsew')
		self.master.columnconfigure(1, weight=1)
		self.master.rowconfigure(1, weight=1)
		self.frame_principal.columnconfigure(0, weight=1)
		self.frame_principal.rowconfigure(0, weight=1)
		self.widgets()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	def pantalla_inicial(self):
		self.paginas.select([self.frame_uno])

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	def pantalla_serie(self):
		self.paginas.select([self.frame_dos])
		self.frame_dos.columnconfigure(0, weight=1)
		self.frame_dos.columnconfigure(1, weight=1)
		self.frame_dos.rowconfigure(2, weight=1)
		self.frame_tabla_uno.columnconfigure(0, weight=1)
		self.frame_tabla_uno.rowconfigure(0, weight=1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	def pantalla_paralelo(self):
		self.paginas.select([self.frame_tres])
		self.frame_tres.columnconfigure(0, weight=1)
		self.frame_tres.columnconfigure(1, weight=1)

# -----------------------------------------------------------------------------------------------------------------
	def pantalla_mixto(self):
		self.paginas.select([self.frame_cuatro])	
		self.frame_cuatro.columnconfigure(0, weight=1)
		self.frame_cuatro.columnconfigure(1, weight=1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	def menu_lateral(self):
		if self.menu is True:
			for i in range(60,300,20):				
				self.frame_menu.config(width= i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_cerrar.grid_forget()
				if clik_inicio is None:		
					self.bt_inicio.grid(column=0, row=0, padx =10, pady=10)
					self.bt_inicio.grid_propagate(0)
					self.bt_inicio.config(width=i)
					self.pantalla_inicial()
			self.menu = False
		else:
			for i in range(300,60,-20):
				self.frame_menu.config(width=  i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_inicio.grid_forget()
				if clik_inicio is   None:
					self.frame_menu.grid_propagate(0)		
					self.bt_cerrar.grid(column=0, row=0, padx =10, pady=10)
					self.bt_cerrar.grid_propagate(0)
					self.bt_cerrar.config(width=i)
					self.pantalla_inicial()
			self.menu = True

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	def widgets(self):
		self.imagen_inicio = PhotoImage(file ='inicio.png')
		self.imagen_menu = PhotoImage(file ='menu.png')
		self.imagen_serie = PhotoImage(file ='serie.png')
		self.imagen_paralelo = PhotoImage(file ='paralelo.png')
		self.imagen_mixto = PhotoImage(file ='mixto.png')
		self.imagen_ajustes = PhotoImage(file ='configuracion.png')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		self.logo = PhotoImage(file ='logo.png')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		self.bt_inicio = Button(self.frame_inicio, image= self.imagen_inicio, bg='black',activebackground='black', bd=0, command = self.menu_lateral)
		self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
		self.bt_cerrar = Button(self.frame_inicio, image= self.imagen_menu, bg='black',activebackground='black', bd=0, command = self.menu_lateral)
		self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)	

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Botones Meú lateral

		Button(self.frame_menu, image= self.imagen_serie, bg='black', activebackground='black', bd=0, command = self.pantalla_serie).grid(column=0, row=1, pady=20,padx=2)
		Button(self.frame_menu, image= self.imagen_paralelo, bg='black',activebackground='black', bd=0, command =self.pantalla_paralelo).grid(column=0, row=2, pady=20,padx=2)
		Button(self.frame_menu, image= self.imagen_mixto, bg= 'black',activebackground='black', bd=0, command = self.pantalla_mixto).grid(column=0, row=3, pady=20,padx=2)
		
		Label(self.frame_menu, text= 'Circuitos en serie', bg= 'black', fg= 'red', font= ('Chiller', 20)).grid(column=1, row=1, pady=20, padx=2)
		Label(self.frame_menu, text= 'Circuitos en paralelo', bg= 'black', fg= 'red', font= ('Chiller', 20)).grid(column=1, row=2, pady=20, padx=2)
		Label(self.frame_menu, text= 'Circuitos mixto/Serie-paralelo', bg= 'black', fg= 'red', font= ('Chiller', 15)).grid(column=1, row=3, pady=20, padx=2)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Crear Las Páginas

		estilo_paginas = ttk.Style()
		estilo_paginas.configure("TNotebook", background='black', foreground='black', padding=0, borderwidth=0)
		estilo_paginas.theme_use('default')
		estilo_paginas.configure("TNotebook", background='black', borderwidth=0)
		estilo_paginas.configure("TNotebook.Tab", background="black", borderwidth=0)
		estilo_paginas.map("TNotebook", background=[("selected", 'black')])
		estilo_paginas.map("TNotebook.Tab", background=[("selected", 'black')], foreground=[("selected", 'black')]);

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

		self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook') 
		self.paginas.grid(column=0,row=0, sticky='nsew')
		self.frame_uno = Frame(self.paginas, bg='black')
		self.frame_dos = Frame(self.paginas, bg='black')
		self.frame_tres = Frame(self.paginas, bg='black')
		self.frame_cuatro = Frame(self.paginas, bg='black')
		self.frame_cinco = Frame(self.paginas, bg='black')
		self.paginas.add(self.frame_uno)
		self.paginas.add(self.frame_dos)
		self.paginas.add(self.frame_tres)
		self.paginas.add(self.frame_cuatro)
		self.paginas.add(self.frame_cinco)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Titullo

		self.titulo = Label(self.frame_top,text= 'Tezla Zapp', bg='black', fg= 'red', font= ('Chiller', 50))
		self.titulo.pack(expand=1)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ventana Princupal

		Label(self.frame_uno, text= 'Calculadora De Circuitos', bg='black', fg= 'white', font= ('Chiller', 30)).pack(expand=1)
		Label(self.frame_uno ,image= self.logo, bg='black').pack(expand=0)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ventana Circuito Serie

		self.frame_tabla_uno = Frame(self.frame_dos, bg= 'black')
		self.frame_tabla_uno.grid(columnspan=3, row=2, sticky='nsew')		
		Label(self.frame_tabla_uno,text="Hallar Voltaje/Tensión (V)",  bg='black', fg= 'WHITE', font= ('Chiller', 20, 'bold')).place(x=50, y=3)
		Label(self.frame_tabla_uno,text="Hallar Corriente/Intensidad (I)",  bg='black', fg= 'WHITE', font= ('Chiller', 20, 'bold')).place(x=340, y=3)
		Label(self.frame_tabla_uno,text="Hallar Resistencia (R)",  bg='black', fg= 'WHITE', font= ('Chiller', 20, 'bold')).place(x=700, y=3)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Botones de calcular

		self.boton1 = tk.Button(self.frame_tabla_uno, text="Calcular Voltaje", command=self.v)
		self.boton1.config(bg="black", fg="cyan", font=("Chiller", 20))
		self.boton1.place(x= 90, y=240)

		self.boton2 = tk.Button(self.frame_tabla_uno, text="Calcular Corriente", command=self.i2)
		self.boton2.config(bg="black", fg="cyan", font=("Chiller", 20))
		self.boton2.place(x= 430, y=240)

		self.boton3 = tk.Button(self.frame_tabla_uno, text="Calcular Resistencia", command=self.r3)
		self.boton3.config(bg="black", fg="cyan", font=("Chiller", 20))
		self.boton3.place(x= 700, y=240)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Hallar el voltaje

		# Corriente
		Label(self.frame_tabla_uno,text="Ingresa la Corriente/Intensidad Total (I): ",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=20, y=70)
		self.intensidad = tk.Entry(self.frame_tabla_uno, font=("arial",10,"bold"), width=10, textvariable=self.i, justify= CENTER)
		self.intensidad.place(x=120, y=100)

		# Resistencia
		Label(self.frame_tabla_uno,text="Ingresa la Resistencia Total(R): ",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=50, y=145)
		self.resistencia = tk.Entry(self.frame_tabla_uno, font=("arial",10,"bold"),width=10, textvariable=self.r, justify= CENTER)
		self.resistencia.place(x=120, y=180)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Hallar la Corriente

		# Voltaje
		Label(self.frame_tabla_uno,text="Ingrese el Voltaje Total (V):",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=400, y=70)
		self.voltaje = tk.Entry(self.frame_tabla_uno, font=("arial",10,"bold"), width=10, textvariable=self.v2, justify= CENTER)
		self.voltaje.place(x=460, y=100)

		# Resistencia
		Label(self.frame_tabla_uno,text="Ingresa la Resistencia Total(R):",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=390, y=145)
		self.resistencia2 = tk.Entry(self.frame_tabla_uno, font=("arial",10,"bold"),width=10, textvariable=self.r2, justify= CENTER)
		self.resistencia2.place(x=460, y=180)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Hallar la Resistencia 

		# Voltaje
		Label(self.frame_tabla_uno,text="Ingrese el Voltaje Total (V):",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=700, y=70)
		self.voltaje2 = tk.Entry(self.frame_tabla_uno, font=("arial",10,"bold"), width=10, textvariable=self.v3, justify= CENTER)
		self.voltaje2.place(x=750, y=100)

		# Intensidad
		Label(self.frame_tabla_uno,text="Ingresa la Corriente/Intensidad Total (I):",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=645, y=145)
		self.intensidad3 = tk.Entry(self.frame_tabla_uno, font=("arial",10,"bold"),width=10, textvariable=self.i3, justify= CENTER)
		self.intensidad3.place(x=750, y=180)		

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Boton Calcular

		self.boton4 = tk.Button(self.frame_tres, text="Calcular", command=self.pa)
		self.boton4.config(bg="black", fg="cyan", font=("Chiller", 20))
		self.boton4.place(x= 200, y=200)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ventana Circuito Paralelo		

		Label(self.frame_tres,text="Circuitos Paralelos:",  bg='black', fg= 'WHITE', font= ('Chiller', 25, 'bold')).place(x=50, y=3)
		
		# Voltaje
		Label(self.frame_tres,text="Ingrese el Voltaje Total (V):",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=200, y=70)
		self.voltaje = tk.Entry(self.frame_tres, font=("arial",10,"bold"), width=10, textvariable=self.vp, justify= CENTER)
		self.voltaje.place(x=410, y=75)
		# Resistencias
		Label(self.frame_tres,text="Ingrese la resistencia 1: ",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=200, y=100)
		self.voltaje = tk.Entry(self.frame_tres, font=("arial",10,"bold"), width=10, textvariable=self.rone, justify= CENTER)
		self.voltaje.place(x=375, y=105)

		Label(self.frame_tres,text="Ingrese la resistencia 2: ",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=200, y=130)
		self.voltaje = tk.Entry(self.frame_tres, font=("arial",10,"bold"), width=10, textvariable=self.rtwo, justify= CENTER)
		self.voltaje.place(x=375, y=135)

		Label(self.frame_tres,text="Ingrese la resistencia 3: ",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=200, y=160)
		self.voltaje = tk.Entry(self.frame_tres, font=("arial",10,"bold"), width=10, textvariable=self.rthree, justify= CENTER)
		self.voltaje.place(x=375, y=165)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ventana Circuito Mixto :0
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		# Botones de calcular
		self.boton1 = tk.Button(self.frame_cuatro, text="Calcular Voltaje", command=self.vo1)
		self.boton1.config(bg="black", fg="cyan", font=("Chiller", 20))
		self.boton1.place(x= 67, y=305)

		self.boton2 = tk.Button(self.frame_cuatro, text="Calcular Corriente", command=self.in1)
		self.boton2.config(bg="black", fg="cyan", font=("Chiller", 20))
		self.boton2.place(x= 400, y=305)

		self.boton3 = tk.Button(self.frame_cuatro, text="Calcular Resistencia", command=self.re1)
		self.boton3.config(bg="black", fg="cyan", font=("Chiller", 20))
		self.boton3.place(x= 725, y=130)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Hallar el voltaje

		# Resistencias
		Label(self.frame_cuatro,text="Ingrese la resistencia 1:",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=50, y=0)
		self.voltaje = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"), width=10, textvariable=self.rm1, justify= CENTER)
		self.voltaje.place(x=100, y=30)

		Label(self.frame_cuatro,text="Ingrese la resistencia 2:",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=50, y=60)
		self.voltaje = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"), width=10, textvariable=self.rm1_1, justify= CENTER)
		self.voltaje.place(x=100, y=90)

		Label(self.frame_cuatro,text="Ingrese la resistencia 3:",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=50, y=120)
		self.voltaje = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"), width=10, textvariable=self.rm1_2, justify= CENTER)
		self.voltaje.place(x=100, y=150)

		# Corriente
		Label(self.frame_cuatro,text="Ingresa la Corriente/Intensidad Total (I):",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=10, y=180)
		self.intensidad = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"), width=10, textvariable=self.im, justify= CENTER)
		self.intensidad.place(x=100, y=215)

		# Resistencia
		Label(self.frame_cuatro,text="Ingresa la Resistencia en Serie (R):",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=20, y=240)
		self.resistencia = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"),width=10, textvariable=self.rm, justify= CENTER)
		self.resistencia.place(x=100, y=270)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Hallar la Corriente

		# Resistencias
		Label(self.frame_cuatro,text="Ingrese la resistencia 1:",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=390, y=0)
		self.voltaje = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"), width=10, textvariable=self.rm2, justify= CENTER)
		self.voltaje.place(x=440, y=30)

		Label(self.frame_cuatro,text="Ingrese la resistencia 2:",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=390, y=60)
		self.voltaje = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"), width=10, textvariable=self.rm2_1, justify= CENTER)
		self.voltaje.place(x=440, y=90)

		Label(self.frame_cuatro,text="Ingrese la resistencia 3:",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=390, y=120)
		self.voltaje = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"), width=10, textvariable=self.rm2_2, justify= CENTER)
		self.voltaje.place(x=440, y=150)

		# Voltaje
		Label(self.frame_cuatro,text="Ingrese el Voltaje Total (V):",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=375, y=175)
		self.voltaje = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"), width=10, textvariable=self.vm, justify= CENTER)
		self.voltaje.place(x=440, y=205)

		# Resistencia
		Label(self.frame_cuatro,text="Ingresa la Resistencia en Serie:",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=370, y=220)
		self.resistencia2 = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"),width=10, textvariable=self.rm0, justify= CENTER)
		self.resistencia2.place(x=440, y=255)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Hallar la Resistencia 

		# Voltaje
		Label(self.frame_cuatro,text="Ingrese el Voltaje Total (V):",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=700, y=0)
		self.voltaje2 = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"), width=10, textvariable=self.vo2, justify= CENTER)
		self.voltaje2.place(x=770, y=30)

		# Intensidad
		Label(self.frame_cuatro,text="Ingresa la Corriente/Intensidad Total (I):",  bg='black', fg= 'WHITE', font= ('Chiller', 15, 'bold')).place(x=640, y=60)
		self.intensidad3 = tk.Entry(self.frame_cuatro, font=("arial",10,"bold"),width=10, textvariable=self.in2, justify= CENTER)
		self.intensidad3.place(x=770, y=90)	

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Operaciones Serie

	def v(self):
		i1= float(self.i.get())
		r1= float(self.r.get())
		v1= i1*r1
		# Resultado
		Label(self.frame_tabla_uno,text="El voltaje del circuito es de "+ str(v1) + "V" ,  bg='black', fg= 'red2', font= ('Chiller', 20, 'bold')).place(x=30, y=300)

	def i2(self):
		v2= float(self.v2.get())
		r2= float(self.r2.get())
		i2= v2/r2
		# Resultado
		Label(self.frame_tabla_uno,text="La Corriente/Intensidad "+ str(i2) + "A" ,  bg='black', fg= 'red2', font= ('Chiller', 20, 'bold')).place(x=360, y=300)

	def r3(self):
		v3= float(self.v3.get())
		i3= float(self.i3.get())
		r3= v3/i3
		# Resultado
		Label(self.frame_tabla_uno,text="La Resistencia es de "+ str(r3) + "A" ,  bg='black', fg= 'red2', font= ('Chiller', 20, 'bold')).place(x=680, y=300)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Operaciones Paralelo

	def pa(self):
		vp= float(self.vp.get())
		rone= float(self.rone.get())
		rtwo= float(self.rtwo.get())
		rthree= float(self.rthree.get())
		rT= (1/rone)+(1/rtwo)+(1/rthree)
		Rt= 1/rT
		Rt1= round(Rt, 3)
		iT= vp/Rt
		It1= round(iT, 3)
		# Resultado
		Label(self.frame_tres,text="La resistencia total del circuito es de "+ str(Rt1) + "Ohmios, y la Intensidad total es de "+ str(It1) + "A (amperios)" ,  bg='black', fg= 'red2', font= ('Chiller', 20, 'bold')).place(x=50, y=270)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Operaciones Mixto

	def vo1(self):
		rm1= float(self.rm1.get())
		rm1_1= float(self.rm1_1.get())
		rm1_2= float(self.rm1_2.get())
		rm = float(self.rm.get())
		im = float(self.im.get())
		rT= (1/rm1)+(1/rm1_1)+(1/rm1_2)
		Rt= 1/rT
		Rt1= round(Rt, 3)
		vm0= im*(rm+Rt1)
		vm0_1= round(vm0, 3)
		# Resultado
		Label(self.frame_cuatro,text="El voltaje del circuito es de "+ str(vm0_1) +"V",  bg='black', fg= 'red2', font= ('Chiller', 20, 'bold')).place(x=0, y=360)

	def in1(self):
		rm2= float(self.rm2.get())
		rm2_1= float(self.rm2_1.get())
		rm2_2= float(self.rm2_2.get())
		rm0 = float(self.rm0.get())
		vm = float(self.vm.get())
		rT= (1/rm2)+(1/rm2_1)+(1/rm2_2)
		Rt= 1/rT
		Rt1= round(Rt, 3)
		imT= vm/(rm0+Rt1)
		imT1= round(imT, 3)
		# Resultado
		Label(self.frame_cuatro,text="La Corriente/Intensidad del circuito es de "+ str(imT1) +"A",  bg='black', fg= 'red2', font= ('Chiller', 20, 'bold')).place(x=380, y=360)

	def re1(self):
		vo2= float(self.vo2.get())
		in2= float(self.in2.get())
		res= vo2/in2
		res1= round(res, 3)
		# Resultado
		Label(self.frame_cuatro,text="La Resistencia del circuito es de "+ str(res1) +"Ω",  bg='black', fg= 'red2', font= ('Chiller', 17, 'bold')).place(x=630, y=200)

# Finnnn :/
if __name__ == "__main__":
	ventana = Tk()
	ventana.title('Tesla_Zapp')
	ventana.minsize(height= 475, width=795)
	ventana.geometry('1000x500+180+80')
	ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))	
	app = Ventana(ventana)
	app.mainloop()