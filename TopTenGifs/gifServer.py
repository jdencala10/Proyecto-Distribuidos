import glob
import sys
import mysql.connector
import redis
import time
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('/etc/apt/thrift-0.11.0/lib/py/build/lib*'[0]))
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
		mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root123", database = "GifsDB")
		puntero=mydb.cursor()
		puntero.execute("SELECT * FROM Gifs ORDER BY contador DESC LIMIT 10")
		resultado = puntero.fetchall()
		lista_gifs = []
		for x in resultado:
			gif = Gif()
			gif.id = x[0]
			gif.url = x[1]
			gif.contador = x[2]
			gif.descripcion=x[3]
			lista_gifs.append(gif)
		return lista_gifs


	def probandoRedis(self):
		print("wertyui")
		redis_db = redis.StrictRedis( host="localhost", port=6379, db=0)
		redis_db.keys()
		redis_db.set('full stack', 'python')
		redis_db.keys()
		print(redis_db.get('full stack'))


	def ObtenerListaGif(self):
		mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root123", database = "GifsDB")
		puntero=mydb.cursor()
		puntero.execute("SELECT * FROM Gifs ORDER BY contador DESC LIMIT 10")
		resultado = puntero.fetchall()
		lista_gifs = []
		for x in resultado:
			gif = Gif()
			gif.id = x[0]
			gif.url = x[1]
			gif.contador = x[2]
			gif.descripcion=x[3]
			lista_gifs.append(gif)
		return lista_gifs

	def eliminarLlaves(self):
		rd = redis.StrictRedis( host="localhost", port=6379, db=0)
		for x in rd.keys():
			rd.delete(x)
		print(rd.keys())

	def top10ConCache(self):
		print("-"*30)
		rd = redis.StrictRedis( host="localhost", port=6379, db=0)
		today = time.strftime("%d/%m/%y")
		llavero = rd.keys()
		if (rd.get(today) is not None):
			listaGifs = []
			data = (str(rd.get(today))+".")[6:-1].split("Gif")
			for x in data:
				y = x[1:-3]
				datosGif = []
				for e in y.split(", "):
					gi = e.split("=")
					datosGif.append(gi[1]) 
				elGif = Gif()
				elGif.url = datosGif[0]
				elGif.contador = datosGif[1]
				elGif.id = datosGif[2]
				elGif.descripcion = datosGif[3]
				listaGifs.append(elGif)
			return listaGifs
		else:
			losGifs = self.ObtenerListaGif()
			rd.set(today, losGifs)
			return losGifs


if __name__ == '__main__':
	handler = theGifServerHandler()
	processor = losMejoresGifs.Processor(handler)
	transport = TSocket.TServerSocket(host='127.0.0.1', port=9090)
	tfactory = TTransport.TBufferedTransportFactory()
	pfactory = TBinaryProtocol.TBinaryProtocolFactory()

	server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

	print('Its dangerous go alone')
	print('Take this server')
	server.serve()

