from __main__ import app, connection

from pymysql import connections

@app.route("/")
@app.route("/vendedores")
def listarVendedores():

    conn = connection.get_connection()

    c = conn.cursor()
    c.execute("SELECT * FROM seller")
    rows = c.fetchall()
    for row in rows:
        print(row)
    return 'vendedores'

@app.route("/vendedores/<id>")
def obter_por_id():
    return f'obter por id: {id}'

@app.route("/vendedores/cadastrar")
def cadastrar():
    return "mostrar formulario de cadastro"