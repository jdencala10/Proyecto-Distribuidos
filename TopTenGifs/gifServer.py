import glob
import sys
import mysql.connector
import redis
import time
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('../thrift-0.11.0/lib/py/build/lib*'[0]))
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
		puntero.execute("SELECT id, gifUrl, contador, Descripcion FROM Gifs ORDER BY contador DESC LIMIT 10;")
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
		puntero.execute("SELECT id, gifUrl, contador, Descripcion FROM Gifs ORDER BY contador DESC LIMIT 10;")
		resultado = puntero.fetchall()
		lista_gifs = []
		for x in resultado:
			gif = Gif()
			gif.id = x[0]
			gif.url = x[1]
			gif.contador = x[2]
			gif.descripcion = x[3]
			lista_gifs.append(gif)
		return lista_gifs

	def eliminarLlaves(self):
		rd = redis.StrictRedis( host="localhost", port=6379, db=0)
		for x in rd.keys():
			rd.delete(x)
		print(rd.keys())

	def top10ConCache(self):
		rd = redis.StrictRedis( host="localhost", port=6379, db=0)
		today = time.strftime("%d/%m/%y")
		llavero = rd.keys()
		if (rd.get(today) is not None):
			print("uso cache")
			listaGifs = []
			data = (str(rd.get(today))+".")[6:-1].split("Gif")
			for x in data:
				y = x[1:-3]
				datosGif = []
				elGif = Gif()
				for e in y.split(", "):
					gi = e.split("=")
					print(gi)
					if(gi[0] == 'url'):
						elGif.url = gi[1][1:-1]
					elif(gi[0] == 'contador'):
						elGif.contador = int(gi[1])
					elif(gi[0] == 'id'):
						elGif.id = int(gi[1])
					else:
						elGif.descripcion = gi[1]
				listaGifs.append(elGif)
			return listaGifs
		else:
			print("sin usar cache")
			losGifs = self.ObtenerListaGif()
			print("-"*20)
			print(losGifs)
			print("-"*20)
			rd.set(today, losGifs)
			print(rd.get(today))
			print("-"*20)
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

