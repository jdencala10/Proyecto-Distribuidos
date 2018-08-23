//ovar thrift = require('/etc/apt/thrift-0.11.0/lib/js/src/thrift')
var thrift = require('thrift')
var losGifs =require('../gen-nodejs/losMejoresGifs')

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

var request = require('request');
var urlIp = 'http://18.222.140.36/';

var tiemposConCache = [];
var tiemposSinCache = [];

for(var i = 0; i < 10; i++){
  request.get({ url: urlIp+'cache', time: true }, function (err, response) {
    tiemposConCache.push(response.elapsedTime);
    console.log(tiemposConCache);
    });
}

for(var i = 0; i < 10; i++){
  request.get({ url: urlIp+'mySql', time: true }, function (err, response) {
    tiemposSinCache.push(response.elapsedTime);
    console.log(tiemposSinCache);
  });
}

app.set('view engine','ejs');
app.set('views',__dirname+'/views')

console.log(tiemposConCache);
console.log(tiemposSinCache);

app.get('/', function(req, res){
  res.render('menu');
});


//Pagina sin cache
app.get('/mySql', function(req, res){

  cliente.top10(function(err, response){
    listaGifs = response;
    res.render('index', {"listaGifs": listaGifs, "titulo":"Usando solo MySQL" });
  });

});


//Pagina secundaria (con cache)
app.get('/cache', function(err, res){

  cliente.top10ConCache(function(err, response){
    listaGifs = response;
    res.render('index', {"listaGifs": listaGifs, "titulo":"Usando MySQL + Redis (cache)"});
  });

});

//pagina de rendimiento
app.get('/rendimiento', function(err, res){


     res.render('rendimiento', {"cache":tiemposConCache, "MySQL":tiemposSinCache});
});

app.listen(3000, ()=>console.log('Node Js listening 3000'))
