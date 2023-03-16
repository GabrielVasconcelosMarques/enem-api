from flask import Flask, jsonify, request
import json
import random

app = Flask(__name__)


# Definir uma variável global para armazenar os dados
dados = []

def formatar_area_conhecimento(area_conhecimento):
    if area_conhecimento == 'linguagens':
        area_conhecimento = 'Linguagens, Códigos e suas Tecnologias'
    elif area_conhecimento == 'exatas':
        area_conhecimento = 'Matemática e suas Tecnologias'
    elif area_conhecimento == 'humanas':
        area_conhecimento = 'Ciências Humanas e suas Tecnologias'
    elif area_conhecimento == 'natureza':
        area_conhecimento = 'Ciências da Natureza e suas Tecnologias'

    return area_conhecimento

def formatar_disciplina(disciplina):
    if disciplina == 'portugues':
        disciplina = 'Língua Portuguesa'
    elif disciplina == 'literatura':
        disciplina = 'Literatura'
    elif disciplina == 'ingles':
        disciplina = 'Inglês'
    elif disciplina == 'espanhol':
        disciplina = 'Espanhol'
    elif disciplina == 'artes':
        disciplina = 'Artes'
    elif disciplina == 'ed_fisica':
        disciplina = 'Educação Física'
    elif disciplina == 'tic':
        disciplina = 'Tecnologias da Informação e Comunicação'
    elif disciplina == 'matematica':
        disciplina = 'Matemática'
    elif disciplina == 'historia':
        disciplina = 'História'
    elif disciplina == 'geografia':
        disciplina = 'Geografia'
    elif disciplina == 'filosofia':
        disciplina = 'Filosofia'
    elif disciplina == 'sociologia':
        disciplina = 'Sociologia'
    elif disciplina == 'fisica':
        disciplina = 'Física'
    elif disciplina == 'quimica':
        disciplina = 'Química'
    elif disciplina == 'biologia':
        disciplina = 'Biologia'

    return disciplina
    

# Decorator para carregar os dados na memória antes do primeiro acesso à rota
@app.before_first_request
def carregar_dados():
    global dados
    with open('dados.json') as f:
        dados = json.load(f)


# rota para retornar todas as questões
# ex: /questions
@app.route('/questions', methods=['GET'])
def get_questions():
    return jsonify(dados)

# rota para retornar somente o ID solicitado
# ex: /questions/1
@app.route('/questions/<int:id>', methods=['GET'])
def get_id(id):
    resultado = {}
    for d in dados:
        if d['id'] == id:
            resultado = d
            break
    return jsonify(resultado)

# rota para retornar filtrando por área de conhecimento
# ex: /questions/area_conhecimento?area_conhecimento=linguagens
@app.route('/questions/area_conhecimento', methods=['GET'])
def get_area_conhecimento():
    area_conhecimento = request.args.get('area_conhecimento')
    area_conhecimento_ajustada = formatar_area_conhecimento(area_conhecimento)
    
    questoes_filtradas = [questao for questao in dados if questao['area_conhecimento'] == area_conhecimento_ajustada]
    return jsonify(questoes_filtradas)


# rota para retornar filtrando por disciplina
# ex: /questions/disciplina?disciplina=ingles
@app.route('/questions/disciplina', methods=['GET'])
def get_disciplina():
    disciplina = request.args.get('disciplina')
    disciplina_ajustada = formatar_disciplina(disciplina)
    
    questoes_filtradas = [questao for questao in dados if questao['disciplina'] == disciplina_ajustada]
    return jsonify(questoes_filtradas)


# rota para retornar filtrando por ano
# ex: /questions/ano?ano=2022
@app.route('/questions/ano', methods=['GET'])
def get_ano():
    ano = request.args.get('ano')
    
    questoes_filtradas = [questao for questao in dados if questao['ano'] == ano]
    return jsonify(questoes_filtradas)


# rota para retornar filtrando por disciplina e ano
# ex: /questions/disciplina-ano?disciplina=ingles&ano=2022
@app.route('/questions/disciplina-ano', methods=['GET'])
def get_disciplina_ano():
    disciplina = request.args.get('disciplina')
    disciplina_ajustada = formatar_disciplina(disciplina)

    ano = request.args.get('ano')

    questoes_filtradas = [questao for questao in dados if questao['disciplina'] == disciplina_ajustada and questao['ano'] == ano]
    return jsonify(questoes_filtradas)


# rota para retornar filtrando por área de conhecimento e ano
# ex: /questions/area-ano?area_conhecimento=linguagens&ano=2022
@app.route('/questions/area-ano', methods=['GET'])
def get_area_conhecimento_ano():
    area_conhecimento = request.args.get('area_conhecimento')
    area_conhecimento_ajustada = formatar_area_conhecimento(area_conhecimento)
    
    ano = request.args.get('ano')

    questoes_filtradas = [questao for questao in dados if questao['area_conhecimento'] == area_conhecimento_ajustada and questao['ano'] == ano]
    return jsonify(questoes_filtradas)


# rota para retornar filtrando 30 questões aleatórias por disciplina
# ex: /questions/random-disciplina?disciplina=ver
@app.route('/questions/random-disciplina', methods=['GET'])
def get_random_questions_disciplina():
    disciplina = request.args.get('disciplina')
    disciplina_ajustada = formatar_disciplina(disciplina)

    questoes_filtradas = [questao for questao in dados if questao['disciplina'] == disciplina_ajustada]
    questoes_aleatorias = random.sample(questoes_filtradas, 30) # retornando 30 questoes

    return jsonify(questoes_aleatorias)


# rota para retornar filtrando 30 questões aleatórias por área de conhecimento
# ex: /questions/random-area?area_conhecimento=linguagens
@app.route('/questions/random-area', methods=['GET'])
def get_random_questions_area():
    area_conhecimento = request.args.get('area_conhecimento')
    area_conhecimento_ajustada = formatar_area_conhecimento(area_conhecimento)

    questoes_filtradas = [questao for questao in dados if questao['area_conhecimento'] == area_conhecimento_ajustada]
    questoes_aleatorias = random.sample(questoes_filtradas, 30) # retornando 30 questoes

    return jsonify(questoes_aleatorias)


if __name__ == '__main__':
    app.run(debug=True)
