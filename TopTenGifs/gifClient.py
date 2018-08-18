import glob
import sys
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('/etc/apt/thrift-0.11.0/lib/py/build/lib*'[0]))

from theGifServer import losMejoresGifs

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():
	transport = TSocket.TSocket('localhost', 9090)
	transport = TTransport.TBufferedTransport(transport)
	protocol = TBinaryProtocol.TBinaryProtocol(transport)
	client = losMejoresGifs.Client(protocol)
	transport.open()
        listaGifs=client.top10()
        print(listaGifs)
        transport.close()

if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)

