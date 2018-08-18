import csv
import random
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root123",
  database="GifsDB"
)

dataCursor= mydb.cursor()

sql = "INSERT INTO Gifs (gifUrl, contador, descripcion) VALUES (%s, %s, %s)"

with open("TGIF-Release/data/tgif-v1.0.tsv") as tsvfile:
  tsvreader = csv.reader(tsvfile, delimiter="\t")
  for line in tsvreader:
    numR = random.randint(1,99999)
    val = (line[0], numR, line[1])
    dataCursor.execute(sql, val)
    mydb.commit()
