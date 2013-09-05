import MySQLdb
from datetime import datetime

class DataBase:
	def __init__(self):
		print "Cargando base de datos ..."

	def run_coneccion(self):
		# Open database connection
		self.db = MySQLdb.connect("localhost","root","","django" )
		self.cursor = self.db.cursor()

	def insert(self,nombre,password):
		# Prepare SQL query to INSERT a record into the database.
		sql = "INSERT INTO usuarios(nombre,password) VALUES ('%s', '%s' )" %(nombre, password)
		
		try:
		   self.cursor.execute(sql)
		   self.db.commit()
		   print "Datos guardados :3"
		except:
		   # Rollback in case there is any error
		   print "Datos NO guardados :("
		   self.db.rollback()

	def update (self,):
		editar = raw_input("Nombre a editar : ")
		nombre = raw_input("Nuevo nombre : ")
		password = raw_input ("Nuevo password : ")
		sql = "UPDATE usuarios SET nombre = '%s' ,password = '%s' WHERE nombre = '%s'" % (nombre,password, editar)
		try:
		   self.cursor.execute(sql)
		   print "Base de datos acutualizada "
		   self.db.commit()
		except:
		   self.db.rollback()
		   print "Problemas con la base de datos "

	def delete(self):
		nombre = raw_input("Nombre a borrar : ")
		sql = "DELETE FROM usuarios WHERE nombre = '%s'"%nombre

		try:
			self.cursor.execute(sql)
			self.db.commit()
			print "Datos boorados de la base de datos"
		except:
			self.db.rollback()
			print "Problemas al borrar"
	
	def loggin(self,nombre, password):
		sql = "SELECT password FROM usuarios WHERE nombre= '%s'" %nombre
		try:
			self.cursor.execute(sql)
			self.db.commit()
			
			#self.results =self.cursor.fetchall()
			#self.results =self.cursor.fetchmany()
			self.results =self.cursor.fetchone()
		except:
			self.db.rollback()
			print "Problemas con la cuenta"

		print "Autentificando . . . "
		pass_db= str(self.results[0])
		print pass_db
		
		if password == pass_db:
			print "Bienvenido :D"
		else :
			print "Problemas con tu contrasena"
	def close(self):
		# disconnect from server
		self.db.close()

def time_now():
	now =datetime.now()
	print now.year
	print now.month
	print now.day
	print now.hour 
	print now.minute
	print now.second



nombre= raw_input("Introduce tu nombre de usuario : ")
password = raw_input("Introducir si password : ")

base = DataBase()
base.run_coneccion()
#base.insert(nombre,password)
#base.update()
base.loggin(nombre,password)
#base.delete()
base.close()
time_now()