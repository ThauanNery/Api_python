from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {
        'id': 1,
        'nome': 'Thauan',
        'sobrenome': 'Nery',
        'email': 'teste@gmail.com'
    },
    
    {
        'id': 2,
        'nome': 'Gildênia',
        'sobrenome': 'Moreira',
        'email': 'teste2@gmail.com'
    }
]

#consultar(todos)
@app.route('/usuarios', methods=['GET'])
def obter():
    return jsonify(usuarios)

#consultar(id)
@app.route('/usuarios/<int:id>', methods=['GET'])
def obter_id(id):
    for usuario in usuarios:
        if usuario.get('id') == id:
            return jsonify(usuario)

#Criar
@app.route('/usuarios', methods=['POST'])
def criar():
   criado = request.get_json()
   usuarios.append(criado)
   return jsonify(criado)
        
#Edita
@app.route('/usuarios/<int:id>', methods=['PUT'])
def editar(id):
    editado = request.get_json()
    for indice,usuario in enumerate(usuarios):
        if usuario.get('id') == id:
           usuarios[indice].update(editado) 
           return jsonify(usuarios[indice])
       
#Excluir
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir(id):
    for indice, usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            del usuarios[indice]
            return jsonify(usuarios)

app.run(port=5000,host='localhost',debug=True)