from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__)

# Definir uma variável global para armazenar os dados
dados = []

# Decorator para carregar os dados na memória antes do primeiro acesso à rota
@app.before_first_request
def carregar_dados():
    global dados
    with open('dados.json') as f:
        dados = json.load(f)

# Definir rota para retornar todas as questões
@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(dados)

# Definir rota para retornar somente o ID solicitado
@app.route('/questions/<int:id>', methods=['GET'])
def get_id(id):
    resultado = {}
    for d in dados:
        if d['id'] == id:
            resultado = d
            break
    return jsonify(resultado)

# http://127.0.0.1:5000/questions/area_conhecimento?area_conhecimento=linguagens
@app.route('/questions/area_conhecimento', methods=['GET'])
def get_area_conhecimento():
    area_conhecimento = request.args.get('area_conhecimento')
    if area_conhecimento == 'linguagens':
        area_conhecimento = 'Linguagens, Códigos e suas Tecnologias'
    
    questoes_filtradas = [questao for questao in dados if questao['area_conhecimento'] == area_conhecimento]
    return jsonify(questoes_filtradas)

# http://127.0.0.1:5000/questions/disciplina?disciplina=ingles
@app.route('/questions/disciplina', methods=['GET'])
def get_disciplina():
    disciplina = request.args.get('disciplina')
    if disciplina == 'ingles':
        disciplina = 'inglês'

    questoes_filtradas = [questao for questao in dados if questao['disciplina'] == disciplina]
    return jsonify(questoes_filtradas)

# http://127.0.0.1:5000/questions/ano?ano=2022
@app.route('/questions/ano', methods=['GET'])
def get_ano():
    ano = request.args.get('ano')
    
    questoes_filtradas = [questao for questao in dados if questao['ano'] == ano]
    return jsonify(questoes_filtradas)


# http://127.0.0.1:5000/questions/disciplina-ano?disciplina=ingles&ano=2022
@app.route('/questions/disciplina-ano', methods=['GET'])
def get_disciplina_ano():
    disciplina = request.args.get('disciplina')
    if disciplina == 'ingles':
        disciplina = 'inglês'
    ano = request.args.get('ano')

    questoes_filtradas = [questao for questao in dados if questao['disciplina'] == disciplina and questao['ano'] == ano]
    return jsonify(questoes_filtradas)

# http://127.0.0.1:5000/questions/area-ano?area_conhecimento=linguagens&ano=2022
@app.route('/questions/area-ano', methods=['GET'])
def get_area_conhecimento_ano():
    area_conhecimento = request.args.get('area_conhecimento')
    if area_conhecimento == 'linguagens':
        area_conhecimento = 'Linguagens, Códigos e suas Tecnologias'
    ano = request.args.get('ano')

    questoes_filtradas = [questao for questao in dados if questao['area_conhecimento'] == area_conhecimento and questao['ano'] == ano]
    return jsonify(questoes_filtradas)


# http://127.0.0.1:5000/questions/random?disciplina=ver
@app.route('/questions/random', methods=['GET'])
def get_random_questions():
    disciplina = request.args.get('disciplina')

    questoes_filtradas = [questao for questao in dados if questao['disciplina'] == disciplina]
    questoes_aleatorias = random.sample(questoes_filtradas, 30) # retornando 30 questoes

    return jsonify(questoes_aleatorias)



if __name__ == '__main__':
    app.run(debug=True)
