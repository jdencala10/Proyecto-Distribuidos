import sys
import glob
sys.path.append('gen-py')
sys.path.insert(0, glob.glob('/home/jamil/thrift-0.9.3/lib/py/build/lib*'[0]))

from prueba import Saludo

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

def main():

    transport = TSocket.TSocket('localhost', 9090)

    transport = TTransport.TBufferedTransport(transport)

    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    
    client = Saludo.Client(protocol)

    transport.open()

    saludoGerudo=client.saludar()
    print(saludoGerudo)

    topCiudades = client.TopEstrellas()
    print(topCiudades)


    transport.close()

if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)
