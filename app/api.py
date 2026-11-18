import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/search")
def search():
    term = request.args.get("q", "")
    cur = sqlite3.connect("shop.db").cursor()
    cur.execute(f"SELECT name, price FROM products WHERE name LIKE '%{term}%'")
    return jsonify(cur.fetchall())


@app.route("/product/<int:pid>")
def product(pid):
    cur = sqlite3.connect("shop.db").cursor()
    cur.execute("SELECT name, price FROM products WHERE id = ?", (pid,))
    return jsonify(cur.fetchone())
