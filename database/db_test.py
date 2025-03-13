import sqlite3

# Conectar a SQLite (la base de datos se creará automáticamente si no existe)
conn = sqlite3.connect('database/ai_sales_strategy.db')

# Crear una tabla básica de prueba
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS test_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT
);
''')

conn.commit()
conn.close()

print("✅ Base de datos configurada correctamente.")

