import psycopg2 as pg
from dotenv import load_dotenv as ld
import os
# pip install psycopg2
# pip install dotenv

#Carrear as variaveis do .env
ld()

paraments = {
    "dbname" : os.getenv("DB_NAME"),
    "user" : os.getenv("DB_USER"),
    "password" : os.getenv("DB_PASSWORD"),
    "host" : os.getenv("DB_HOST"),
    "port" : os.getenv("DB_PORT")
}

