const express = require('express')
const app = express()

var grupo = ["luis","jamil","jorge"];

app.set('view engine','ejs');
app.set('views',__dirname+'/views')

app.get('/', function(req, res){
		res.render('index', {"grupo": grupo})
		});
app.listen(3000, ()=>console.log('Node Js listening 3000'))
