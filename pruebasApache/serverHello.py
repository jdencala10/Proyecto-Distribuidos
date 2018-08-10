import glob
import sys
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('/home/jamil/thrift-0.9.3/lib/py/build/lib*'[0]))

from prueba import Saludo

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
