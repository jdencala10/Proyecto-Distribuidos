//ovar thrift = require('/etc/apt/thrift-0.11.0/lib/js/src/thrift')
var thrift = require('thrift')
var losGifs=require('../gen-nodejs/losMejoresGifs')

var ttypes = require('../gen-nodejs/theGifServer_types')
const assert=require('assert')
const express = require('express')
const app = express()

var transport = thrift.TBufferedTransport;
var protocol = thrift.TBinaryProtocol;

var listaGifs;
var listaGifsConCache;



var connection = thrift.createConnection("localhost", 9090, {
  transport : transport,
  protocol : protocol
});

connection.on('error', function(err) {
  assert(false, err);
});

var cliente =  thrift.createClient(losGifs, connection);

/*
cliente.top10(function(err, response) {
  listaGifs = response;
});

cliente.top10ConCache(function(err, response) {
 listaGifs = response;
});
*/

app.set('view engine','ejs');
app.set('views',__dirname+'/views')


//Pagina principal
app.get('/', function(req, res){

  cliente.top10(function(err, response){
    listaGifs = response;
    res.render('index', {"listaGifs": listaGifs });
  });

});


//Pagina secundaria (con cache)
app.get('/1', function(err, res){

  cliente.top10ConCache(function(err, response){
    listaGifs = response;
    res.render('index', {"listaGifs": listaGifs});
  });

});


app.listen(3000, ()=>console.log('Node Js listening 3000'))
