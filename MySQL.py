import mysql.connector
import datetime
import secrets
import json



# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Owenisas@123",
    database="owenisas",
    port=3305
)
