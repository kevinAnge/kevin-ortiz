from flask import Flask, render_template

index = Flask(__name__)


@index.route('/')
def inicio(): return render_template('index.html')

@index.route('/nosotros')
def nosotros(): return render_template('nosotros.html')

@index.route('/param/<string:nombre>')
def parametros(nombre):
    ies = "Palomeras-Vallecas"

    usuario = {
        "nombre": "Juan",
        "apellidos": "Garcia Gonzales",
        "edad": 21
    }

    lista_usuarios = [
        {
            "nombre": "Juan",
            "apellidos": "Garcia Gonzales",
            "edad": 21  
        },

        {
            "nombre": "Ana",
            "apellidos": "Jimenez Fernandes",
            "edad": 20 
        },

        {
            "nombre": "Helen",
            "apellidos": "Smith",
            "edad": 19  
        }
    ]

    return render_template('param.html', nombre=nombre, centro=ies,  usu=usuario, lista_usu=lista_usuarios)

if __name__ == '__main__':index.run(debug=True)
