import pyodbc
from datetime import datetime
from random import randint

class Conexion():
	def __init__(self):
		print "Creando Conexion . . . . . "

	def establecerConexion(self):
		Bandera= True
		try:
			#self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.0.111;DATABASE=Equipo2;UID=sa;PWD=eduardo')
			self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.209;DATABASE=equipo2;UID=equipo2;PWD=equipo2')
			self.cursor = self.cnxn.cursor()
			print "Exito en la conexion  !!! "	
		except:
			print "Problemas de conexion !!!"
			Bandera = False
		return Bandera
	def InsertarCiudades(self, cantidad):
		Mensaje ="Datos Guadados Exitosamente"
		for x in range(cantidad):
			ciudad = "ciudad"+ str(x)
			#Sq = "INSERT INTO CIUDAD(idCiudad,Nombre) VALUES ('%s', '%s' )" %(x,ciudad)
			Sq = "INSERT INTO ciudad(idCiudad,Nombre) VALUES ('%s', '%s' )" %(x,ciudad)
			try:
			   self.cursor.execute(Sq)
			   self.cnxn.commit()
			except:
				Mensaje = "Problemas al Guadar Datos"
		print Mensaje

	def InsertarAlumnos(self, cantidad):
		Mensaje ="Datos Guadados Exitosamente"
		print cantidad

		for x in range(cantidad):
			Alumno = "Alumno"+ str(x)
			Edad = randint(2,50)
			S= self.Sexo(randint(0,1))
			ciudad = "ciudad"+ str(randint(0,100))
			
			#Sq = "INSERT INTO ALUMNOS(idAlumno,Nombre, Edad, Sexo, idCiudad) VALUES ('%s', '%s','%s','%s','%s' )" %(Alumno,Alumno,Edad,S, ciudad)
			Sq = "INSERT INTO alumno(idAlumno,Nombre, Edad, Sexo, idCiudad) VALUES ('%s', '%s','%s','%s','%s' )" %(Alumno,Alumno,Edad,S, ciudad)
			try:
				self.cursor.execute(Sq)
				self.cnxn.commit()
			except:
				Mensaje = "Problemas al Guadar Datos"
		print Mensaje

	def Actualizacion(self,cantidad):
		Mensaje = "Exito "
		for x in range(cantidad):		
			Aleatorio = randint(12, 50)
			idAleatorio =  "Alumno"+ str(randint(0, 10000))
			#Sq = "UPDATE ALUMNOS SET Edad = '%s' WHERE idAlumno = '%s'" % (Aleatorio,idAleatorio)
			Sq = "UPDATE alumno SET edad = '%s' WHERE idAlumno = '%s'" % (Aleatorio,idAleatorio)
			try:
				self.cursor.execute(Sq)
				self.cnxn.commit()
			except:
				Mensaje = "No Actualizados"
		print Mensaje


	def Seleccionar(self, cantidad):
		Mensaje = "Exito "

		for x in range(cantidad):
			Aleatorio = "ciudad"+ str(randint(0,100))
			#Sq = "SELECT * FROM CIUDAD,ALUMNOS WHERE CIUDAD.idCiudad= ALUMNOS.idCiudad and idCiudad = '%s'" %Aleatorio
			Sq = "SELECT * FROM ciudad,alumno WHERE ciudad.idCiudad= alumno.idCiudad and idCiudad = '%s'" %Aleatorio
			
			try:
				self.cursor.execute(Sq)
				self.cnxn.commit()
			except:
				Mensaje = "Problemas con la Seleccion"
		print Mensaje
	
	def Seleccionar_dos(self, cantidad):
		Mensaje = "Exito "
		print cantidad
		for x in range(cantidad):
			Aleatorio = "ciudad"+ str(randint(0,100))
			#Sq = "SELECT * FROM CIUDAD,ALUMNOS WHERE CIUDAD.idCiudad = ALUMNOS.idCiudad and idAlumno = '%s'" %Aleatorio
			Sq = "SELECT * FROM ciudad,alumno WHERE ciudad.idCiudad = alumno.idCiudad and idAlumno = '%s'" %Aleatorio
			try:
				self.cursor.execute(Sq)
				self.cnxn.commit()
			except:
				Mensaje = "Problemas con la Seleccion"
		print Mensaje

	def InsertarVisitas(self,cantidad):
		Mensaje = "Exito en insertar Hoteles"
		for x in range(cantidad):
			temporada = self.Temporada(randint(0,2))
			Alumno =  randint(0, 10000)
			ciudad = randint(0,100)
			Hotel = "Hotel "+ str(randint(2,50))
			tarifa = self.Estrellas(randint(0,4)) #No se que poner aqui
			Sq = "INSERT INTO visitas2(Hotel,idCiudad, temporada, Tarifa,idAlumno) VALUES ('%s', '%s','%s','%s','%s' )" %(Hotel,ciudad,temporada,tarifa,Alumno)

			try:
				self.cursor.execute(Sq)
				self.cnxn.commit()
			except:
				Mensaje = "Problemas con la inserccion"
		print Mensaje

	def ExamenFinal(self,cantidad):
		for x in range(cantidad):
			try:
				self.cursor.execute("execute Examen 1,0,200")
				self.cnxn.commit()
			except:
				print "Problemas con la inserccion"
		print "Termino"



	def Sexo(self,valor):
		Sexo = "Masculino"
		if valor == 0:
			Sexo = "Femenino"
		return Sexo
	def Temporada(self,valor):
		T = "Alta"
		if valor == 1:
			T= "Media"
		elif valor == 2:
			T = "Baja"
		return T

	def Estrellas(self,valor):
		calificacion= "*"
		if valor==1:
			calificacion= "**"
		elif valor==2 :
			calificacion= "***"
		elif valor==3:
			calificacion= "****"
		elif valor==4:
			calificacion= "*****"
		return calificacion	


def Tiempo():
	now =datetime.now()
	print "Minuto :"+str(now.minute)+ " Segundo : "+str(now.second)


Con = Conexion()
if (Con.establecerConexion()):
	print "Comienza  : "
	Tiempo()

##########################
	#Con.InsertarCiudades(100)

	#Con.InsertarAlumnos(100000)

	#Con.Seleccionar(5000)

	#Con.Actualizacion(5000)

	#Con.Seleccionar_dos(5000)

	#Con.InsertarVisitas(18348)

	Con.ExamenFinal(2000)
########################

	print "Termina : "
	Tiempo()
else:
	print "u.u"

