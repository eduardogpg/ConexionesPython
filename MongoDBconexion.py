import pymongo
#puerto estandar de MongoDb (27017).

try:

	con= pymongo.Connection()
	db= con.mensajes
	pais =  { 'nombre': 'Mexico','habitantes':120000 , 'Continente': 'America', 'moneda':'Peso'}
	paises = db.paises
	#paises.insert(pais)
	paisActual =paises.find_one({'nombre': 'Mexico'}) 
	print "Conexion Exitosa, Datos Guardados correctamente"
	print paisActual
except:
	print "Problemas con la conexion"


