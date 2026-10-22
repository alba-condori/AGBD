from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Datos para entrar a la base
DB_HOST = "10.9.120.5"
DB_PORT = 3306
DB_DATABASE = "Kairos-Trigo"
DB_USERNAME = "kairosTrigo"
DB_PASSWORD = "kt123456"

# La "dirección completa" de la base
url = URL.create(
    drivername = "mysql+pymysql",
    username = DB_USERNAME,
    password = DB_PASSWORD,
    host = DB_HOST,
    port = DB_PORT,
    database = DB_DATABASE,
)

# El engine es lo que conecta
engine = create_engine(url)

# Esto prueba si anda
if __name__ == "__main__":
    with engine.connect() as conn:
        print("Conectado a:", conn.execute(text("SELECT DATABASE()")).scalar())