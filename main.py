from flask import Flask
import mysql.connector
from flask import jsonify
from bd import mydb

app = Flask(_name_)

@app.route('/sincronizar_datos', methods=['GET'])
def sincronizar_datos():
    try:
       
        cursor = mydb.cursor()
        cursor.execute(f"""
            SELECT * FROM ambulancias WHERE estado = 0 ORDER BY _id  DESC LIMIT 1;
        """)
        row = cursor.fetchone()
        
        
        resultado = {
            '_id': str(row[0]),
            'ip': str(row[1]),
            'id': str(row[2]),
            'msg': str(row[3]),
            'time': str(row[4]),
            'estado':str(row[5]),

        }
        cursor.close()
        return jsonify(resultado)

    except Exception as e:
        return jsonify({'detalle': f'error {e}'}),500


@app.route('/actualizar_datos_sincronizados/<id>', methods=['PUT'])
def actualizar_datos_sincronizados(id):
    try:
        cursor = mydb.cursor()
        cursor.execute(f"""
            UPDATE ambulancias SET estado = 1 WHERE _id = {id};
        """)
        mydb.commit()
        return jsonify({'detalle': 'Exitoso!'}),200
    
    except Exception as e:
        return jsonify({'detalle': f'error {e}'}),500


@app.route('/sincronizar_datos_faltantes/<dispositivo_id>', methods = ['GET'])
def sincronizar_datos_faltantes(dispositivo_id):
    try:    
        cursor = mydb.cursor()
        cursor.execute(f"""
            SELECT * FROM ambulancias WHERE estado = 0 AND id = '{dispositivo_id}';
        """)
        row = cursor.fetchone()
        resultado = []
        while row:
            resultado.append({
                '#n': str(row[0]),
                'ip': str(row[1]),
                'id': str(row[2]),
                'msg': str(row[3]),
                'time': str(row[4]),
                'estado':str(row[5]),

            })
            row = cursor.fetchone()
        cursor.close()
        return jsonify(resultado)

    except Exception as e:
        return jsonify({'detalle': f'error {e}'}),500

@app.route('/sincronizar_datos_masivos/<dispositivo_id>', methods = ['PUT'])
def sincronizar_datos_masivos(dispositivo_id):
    try:
        cursor = mydb.cursor()
        cursor.execute(f"""
            UPDATE ambulancias SET estado = 1 WHERE id = '{dispositivo_id}';
        """)
        mydb.commit()
        return jsonify({'detalle': 'Exitoso!'}),200
    except Exception as e:
        return jsonify({'detalle': f'error {e}'}),5


@app.route('/eliminar_registros/<dispositivo_id>', methods=['DELETE'])
def eliminar_registros(dispositivo_id):
    try:
        cursor = mydb.cursor()
        cursor.execute(f"""
           DELETE FROM ambulancias WHERE id = '{dispositivo_id}' AND estado = 1;
        """)
        mydb.commit()

        return jsonify({'detalle': 'Exitoso!'}),200

    except Exception as e:
        return jsonify({'detalle': f'error {e}'}),500

    

if _name_ == '_main_':
    app.run(host='0.0.0.0')