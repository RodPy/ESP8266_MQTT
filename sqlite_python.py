import sqlite3
from sqlite3 import Error

# Conexión a la base de datos SQLite (se creará si no existe)
DB_PATH = "example.db"

# Función para crear una conexión a SQLite
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect(DB_PATH)
        print(f"Conectado a SQLite (versión: {sqlite3.version})")
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    
    return connection

# Función para crear una tabla
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        connection.commit()
        print("Tabla 'users' creada o ya existe")
    except Error as e:
        print(f"Error al crear la tabla: {e}")

# Función para insertar datos en la tabla
def insert_user(connection, name, age, email):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO users (name, age, email) VALUES (?, ?, ?)"
        cursor.execute(query, (name, age, email))
        connection.commit()
        print(f"Usuario {name} agregado con éxito")
    except Error as e:
        print(f"Error al insertar datos: {e}")

# Función para obtener todos los usuarios
def select_all_users(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        
        print("Lista de usuarios:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error al consultar la tabla: {e}")

# Función para cerrar la conexión a la base de datos
def close_connection(connection):
    if connection:
        connection.close()
        print("Conexión cerrada")

# Función principal
def main():
    # Crear conexión a SQLite
    connection = create_connection()

    if connection is not None:
        # Crear tabla
        create_table(connection)

        # Insertar algunos usuarios de ejemplo
        insert_user(connection, "Alice", 25, "alice@example.com")
        insert_user(connection, "Bob", 30, "bob@example.com")
        insert_user(connection, "Charlie", 22, "charlie@example.com")

        # Consultar todos los usuarios
        select_all_users(connection)

        # Cerrar conexión
        close_connection(connection)
    else:
        print("Error al crear la conexión a la base de datos")

if __name__ == "__main__":
    main()
