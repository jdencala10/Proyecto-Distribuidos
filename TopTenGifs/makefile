all:
	pwd
	thrift -r --gen py theGifServer.thrift
	thrift -r --gen js:node theGifServer.thrift	

server: all
	python3 gifServer.py

client: all
	node clienteJs/app.js
