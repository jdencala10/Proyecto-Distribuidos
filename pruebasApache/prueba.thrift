namespace py prueba

struct City {
  1: i32 id,
  3: string ciudad,
  2: i32 n_lunas,
}

service Saludo {

	string saludar(),

	string SaludoConNombre(1:string nombre),

	list<City> TopEstrellas(),


}