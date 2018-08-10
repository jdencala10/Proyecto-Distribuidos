namespace py prueba

service Saludo {

	string saludar(),

	string SaludoConNombre(1:string nombre)
}