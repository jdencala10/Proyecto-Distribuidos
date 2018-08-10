import glob
import sys
import mysql.connector
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('/home/jamil/thrift-0.9.3/lib/py/build/lib*'[0]))

from prueba import Saludo
from prueba.ttypes import City

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class SaludoHandler:
	def __init__(self):
		self.log = {}

	def saludar(self):
		return 'sawotta'

	def SaludoConNombre(self, nombre):
		return 'Sawotta '+ nombre

	def TopEstrellas(self):
		city = City()
		city.id = 1
		city.ciudad = "Pokemon"
		city.n_lunas = 20

		lista_ciudades = self.infoLunas()
		return lista_ciudades

	def infoLunas(self):
		mydb = mysql.connector.connect(
			host = "localhost",
			user = "root",
			password = "root",
			database = "prueba"
			)

		puntero = mydb.cursor()

		puntero.execute("SELECT * FROM lunas ORDER BY n_lunas DESC LIMIT 3")
		resultado = puntero.fetchall()

		lista_ciudades = []
		for x in resultado:
			city = City()
			city.id = x[0]
			city.ciudad = x[1]
			city.n_lunas = x[2]
			lista_ciudades.append(city)
		return lista_ciudades



if __name__ == '__main__':
	handler = SaludoHandler()
	processor = Saludo.Processor(handler)
	transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
	tfactory = TTransport.TBufferedTransportFactory()
	pfactory = TBinaryProtocol.TBinaryProtocolFactory()

	server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

	print('Its dangerous go alone')
	print('Take this server')
	server.serve()
