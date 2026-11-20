from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.get("/buscar")
def buscar():
    # Ensayo de clase: SQLi por f-string (el gate diff-aware debe bloquearlo).
    q = request.args.get("q", "")
    con = sqlite3.connect("tienda.db")
    filas = con.execute(f"SELECT nombre, precio FROM productos WHERE nombre = '{q}'").fetchall()
    return {"resultados": filas}


if __name__ == "__main__":
    app.run()
