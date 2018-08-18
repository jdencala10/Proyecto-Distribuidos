import glob
import sys
import mysql.connector
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('/etc/apt/thrift-0.11.0/lib/py/build/lib*'[0]'))
from theGifServer import losMejoresGifs 
from theGifServer.ttypes import Gif

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class theGifServerHandler:
	def __init__(self):
	self.log = {}
	def top10(self):
	 mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "root123",
		database = "GifsDB"
		)
	puntero=mydb.cursor()
	puntero.execute("SELECT * FROM Gifs ORDER BY contador DESC LIMIT 10")
		resultado = puntero.fetchall()
	lista_ciudades = []
	for x in resultado:
		gif = Gif()
		gif.id = x[0]
		gif.urlGif = x[1]
		gif.contador = x[2]
		gif.descripcion=x[3]
		lista_ciudades.append(city)
	return lista_ciudades

if __name__ == '__main__':
	handler = theGifServerHandler()
	processor = theGifServer.Processor(handler)
	transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
	tfactory = TTransport.TBufferedTransportFactory()
	pfactory = TBinaryProtocol.TBinaryProtocolFactory()

	server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

	print('Its dangerous go alone')
	print('Take this server')
	server.serve()
