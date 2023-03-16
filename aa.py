def alterar_disciplina(disciplina):
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


a = alterar_disciplina('tic')

print(a)