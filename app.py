from flask import Flask, jsonify, request
import json
import random
from flask_restx import Api, Resource, fields


app = Flask(__name__)
api = Api(app, version='1.0', title='API Rest ENEM', description='API de questões do ENEM', doc='/documentation', default='Clique aqui para acessar a documentação dos Endpoints')

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
@api.route('/questions')
class QuestionsListTotal(Resource):
    def get(self):
        return jsonify(dados)

# rota para retornar somente o ID solicitado
# ex: /questions/1
@api.route('/questions/<int:id>')
class QuestionById(Resource):
    def get(self, id):
        resultado = {}
        for d in dados:
            if d['id'] == id:
                resultado = d
                break
        return jsonify(resultado)

# rota para retornar filtrando por área de conhecimento
# ex: /questions/area_conhecimento/linguagens
@api.route('/questions/area_conhecimento/<string:area_conhecimento>')
class QuestionsByArea(Resource):
    def get(self, area_conhecimento):
        area_conhecimento_ajustada = formatar_area_conhecimento(area_conhecimento)
        
        questoes_filtradas = [questao for questao in dados if questao['area_conhecimento'] == area_conhecimento_ajustada]
        return jsonify(questoes_filtradas)



# rota para retornar filtrando por disciplina
# ex: /questions/ingles
# Modifique a rota
@api.route('/questions/disciplina/<string:disciplina>', strict_slashes=False)
class QuestionsByDiscipline(Resource):
    def get(self, disciplina):
        disciplina_ajustada = formatar_disciplina(disciplina)
        
        questoes_filtradas = [questao for questao in dados if questao['disciplina'] == disciplina_ajustada]
        return jsonify(questoes_filtradas)


# rota para retornar filtrando por ano
# ex: /questions/2022
@api.route('/questions/ano/<int:ano>')
class QuestionsByYear(Resource):
    def get(self, ano):
        
        questoes_filtradas = [questao for questao in dados if questao['ano'] == str(ano)]
        return jsonify(questoes_filtradas)

#continuar daqui


# rota para retornar filtrando por disciplina e ano
# ex: /questions/disciplina-ano/ingles/2022
@api.route('/questions/disciplina-ano/<string:disciplina>/<int:ano>')
class QuestionsByDisciplineAndYear(Resource):
    def get(self, disciplina, ano):
        disciplina_ajustada = formatar_disciplina(disciplina)
        questoes_filtradas = [questao for questao in dados if questao['disciplina'] == disciplina_ajustada and questao['ano'] == str(ano)]
        return jsonify(questoes_filtradas)


# rota para retornar filtrando por área de conhecimento e ano
# ex: /questions/area-ano/linguagens/2022
@api.route('/questions/area-ano/<string:area_conhecimento>/<int:ano>')
class QuestionsByAreaAndYear(Resource):
    def get(self, area_conhecimento, ano):
        area_conhecimento_ajustada = formatar_area_conhecimento(area_conhecimento)

        questoes_filtradas = [questao for questao in dados if questao['area_conhecimento'] == area_conhecimento_ajustada and questao['ano'] == str(ano)]
        return jsonify(questoes_filtradas)


# rota para retornar filtrando 30 questões aleatórias por disciplina
# ex: /questions/random-disciplina/ver
@api.route('/questions/random-disciplina/<string:disciplina>')
class QuestionsRandomByDiscipline(Resource):
    def get(self, disciplina):
        disciplina_ajustada = formatar_disciplina(disciplina)

        questoes_filtradas = [questao for questao in dados if questao['disciplina'] == disciplina_ajustada]
        questoes_aleatorias = random.sample(questoes_filtradas, 30) # retornando 30 questoes

        return jsonify(questoes_aleatorias)


# rota para retornar filtrando 30 questões aleatórias por área de conhecimento
# ex: /questions/random-area/linguagens
@api.route('/questions/random-area/<string:area_conhecimento>')
class QuestionsRandomByArea(Resource):
    def get(self, area_conhecimento):
        area_conhecimento_ajustada = formatar_area_conhecimento(area_conhecimento)

        questoes_filtradas = [questao for questao in dados if questao['area_conhecimento'] == area_conhecimento_ajustada]
        questoes_aleatorias = random.sample(questoes_filtradas, 30) # retornando 30 questoes

        return jsonify(questoes_aleatorias)


if __name__ == '__main__':
    app.run(debug=True)
