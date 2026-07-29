import pulp

# ==========================================
# 1. CONJUNTOS E PARÂMETROS
# ==========================================
professores = [
    'Alberto Vazquez Saa', 'Ethan Guy Cotterill', 'Christian da Silva Rodrigues', 'Laura Leticia Ramos Rifo',
    'Diego Sebastian Ledesma', 'Joerg Dietrich Wilhelm Schleicher', 'Marcelo da Silva Montenegro',
    'Gabriela Del Valle Planas', 'Maicon Ribeiro Correa', 'Sahibzada Waleed Noor', 'João Vitor da Silva',
    'Alessio Fiscella', 'Artem Lopatin', 'Mahendra Prasad Panthee', 'Nicholas Braun Rodrigues',
    'Tiago Jardim da Fonseca', 'Maria Amelia Novais Schleicher', 'Plamen Emilov Kochloukov', 'Michele Martins Lopes',
    'Guilherme Vieira Neto', 'Viviana Jorgelina Del Barco', 'Argenis Jose Mendez Garcia', 'Erik Antonio Rojas Mendoza',
    'Luiz Fernando da Silva Gouveia', 'Eder de Moraes Correa', 'Pedro José Catuogno', 'Claudemir Fideles Bezerra Junior',
    'João Paulo Pitelli Manoel', 'Joachim Weber', 'Lino Anderson da Silva Grama', 'Gabriel Ponce', 'Giuliano Angelo Zugliani',
    'Sergio Antonio Tozoni', 'Andre Magalhaes de sa Gomes', 'Bianca Morelli Rodolfo Calsavara', 'Ricardo Miranda Martins',
    'Lucas Catão de Freitas Ferreira', 'Paulo Jose da Silva e Silva', 'Marcio Antonio de Faria Rosa', 'Peter Sussner',
    'José Régis Azevedo Varão Filho', 'Paulo Regis Caron Ruffino', 'Christian Horacio Olivera', 'Marcelo Firer',
    'Victor Freguglia Souza', 'Larissa Avila Matos', 'Jesus Enrique Garcia', 'Veronica Andrea Gonzalez Lopez',
    'Mauricio Enrique Zevallos Herencia', 'Hildete Prisco Pinheiro', 'Caio Lucidius Naberezny Azevedo', 'Diego Fernando de Bernardini',
    'Alvaro Alexander Burbano Moreno', 'Elcio Lebensztayn', 'Filidor Edilfonso Vilca Labra', 'Felipe Augusto Fernandes',
    'Samara Flamini Kiihl', 'Alex Rodrigo Dos Santos Sousa', 'Everton Emanuel Campos de Lima', 'Rafael Pimentel Maia',
    'Carlos Cesar Trucios Maza', 'Guilherme Vieira Nunes Ludwig', 'Laercio Luis Vendite', 'Roberto Andreani',
    'Stefano de Leo', 'Estevão Esmi Laureano', 'João Batista Florindo', 'Ricardo Caetano Azevedo Biloti', 'Marcos Eduardo Ribeiro do Valle Mesquita',
    'Jayme Morandi Vaz', 'Laecio Carvalho de Barros', 'Lucio Tunes Dos Santos', 'Lázaro Aurélio Padilha Júnior', 'Kelly Cristina Poldi',
    'Giuseppe Romanazzi'
]

materias = [
    'MA044', 'MA091', 'MA104', 'MA105', 'MA111', 'MA141', 'MA148', 'MA211', 'MA220', 'MA225',
    'MA311', 'MA327', 'MA446', 'MA453', 'MA502', 'MA602', 'MA621', 'MA705', 'MA712', 'MA720',
    'MA724', 'MA740', 'MA902', 'ME110', 'ME111', 'ME115', 'ME173', 'ME176', 'ME210', 'ME310',
    'ME322', 'ME323', 'ME414', 'ME601', 'ME607', 'ME613', 'ME623', 'ME705', 'ME712', 'ME714',
    'ME721', 'ME812', 'ME908', 'ME920', 'ME921', 'ME951', 'MS123', 'MS149', 'MS211', 'MS213',
    'MS380', 'MS512', 'MS513', 'MS550', 'MS580', 'MS590', 'MS620', 'MS712', 'MS728', 'MS902',
    'MS904', 'MS943', 'MS991', 'MS992'
]

horarios = ['8h', '10h', '14h', '16h', '19h', '21h']
# salas = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] # Falha mapeada no relatório: salas comentadas
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex']
bloco_par = ['Seg', 'Qua', 'Sex']
bloco_impar = ['Ter', 'Qui']

blocos = {
    'MA044':bloco_par, 'MA091': bloco_par, 'MA104': bloco_impar, 'MA105':bloco_par, 'MA111': bloco_par, 
    'MA141': bloco_impar, 'MA148':bloco_impar, 'MA211':bloco_par, 'MA220': bloco_impar, 'MA225':bloco_par,
    'MA311':bloco_par, 'MA327':bloco_impar, 'MA446': bloco_impar, 'MA453':bloco_impar, 'MA502': bloco_par, 
    'MA602': bloco_par, 'MA621':bloco_impar, 'MA705': bloco_par, 'MA712': bloco_par, 'MA720':bloco_impar,
    'MA724':bloco_par, 'MA740': bloco_par, 'MA902': bloco_par, 'ME110': bloco_par, 'ME111': bloco_impar,
    'ME115': bloco_impar, 'ME173':bloco_par, 'ME176': bloco_impar, 'ME210': bloco_impar, 'ME310':bloco_impar,
    'ME322':bloco_par, 'ME323': bloco_par, 'ME414': bloco_par, 'ME601':bloco_par, 'ME607': bloco_impar,
    'ME613': bloco_par, 'ME623':bloco_par, 'ME705': bloco_impar, 'ME712': bloco_par, 'ME714':bloco_impar,
    'ME721':bloco_impar, 'ME812': bloco_par, 'ME908': bloco_impar, 'ME920':bloco_impar, 'ME921':bloco_par, 
    'ME951': bloco_par, 'MS123':bloco_par, 'MS149':bloco_impar, 'MS211':bloco_par, 'MS213':bloco_impar,
    'MS380': bloco_par, 'MS512': bloco_par, 'MS513': bloco_impar, 'MS550': bloco_par, 'MS580': bloco_impar,
    'MS590': bloco_impar, 'MS620': bloco_impar, 'MS712': bloco_par, 'MS728': bloco_impar, 'MS902':bloco_par,
    'MS904':bloco_impar, 'MS943': bloco_par, 'MS991': bloco_impar, 'MS992':bloco_impar
}

preferencias = {}
# Inicializa todas as preferências para 0
for professor in professores:
    for materia in materias:
        preferencias[(professor, materia)] = 0

# Matriz de preferência real
mat_prof = [
    ('MA044', 'Alberto Vazquez Saa'), ('MA044', 'Ethan Guy Cotterill'), ('MA091', 'Christian da Silva Rodrigues'),
    ('MA104', 'Laura Leticia Ramos Rifo'), ('MA105', 'Diego Sebastian Ledesma'), ('MA111', 'Joerg Dietrich Wilhelm Schleicher'),
    ('MA111', 'Marcelo da Silva Montenegro'), ('MA111', 'Gabriela Del Valle Planas'), ('MA111', 'Maicon Ribeiro Correa'),
    ('MA111', 'Sahibzada Waleed Noor'), ('MA111', 'João Vitor da Silva'), ('MA111', 'Alessio Fiscella'),
    ('MA111', 'Artem Lopatin'), ('MA111', 'Mahendra Prasad Panthee'), ('MA111', 'Nicholas Braun Rodrigues'), 
    ('MA111', 'Tiago Jardim da Fonseca'), ('MA141', 'Maria Amelia Novais Schleicher'), ('MA141', 'Plamen Emilov Kochloukov'),
    ('MA141', 'Michele Martins Lopes'), ('MA141', 'Guilherme Vieira Neto'), ('MA141', 'Viviana Jorgelina Del Barco'),
    ('MA141', 'Argenis Jose Mendez Garcia'), ('MA141', 'Erik Antonio Rojas Mendoza'), ('MA141', 'Luiz Fernando da Silva Gouveia'),
    ('MA141', 'Eder de Moraes Correa'), ('MA141', 'Osmar Rogerio Reis Severiano'), ('MA141', 'Pedro José Catuogno'),
    ('MA148', 'Claudemir Fideles Bezerra Junior'), ('MA211', 'João Paulo Pitelli Manoel'), ('MA211', 'Joachim Weber'),
    ('MA211', 'Luiz Fernando da Silva Gouveia'), ('MA211', 'Lino Anderson da Silva Grama'), ('MA220', 'Gabriel Ponce'),
    ('MA225', 'Giuliano Angelo Zugliani'), ('MA311', 'Sergio Antonio Tozoni'), ('MA311', 'Andre Magalhaes de sa Gomes'), 
    ('MA311', 'Bianca Morelli Rodolfo Calsavara'), ('MA311', 'Ricardo Miranda Martins'), ('MA311', 'Osmar Rogerio Reis Severiano'),
    ('MA311', 'Lucas Catão de Freitas Ferreira'), ('MA327', 'Joachim Weber'), ('MA327', 'Paulo Jose da Silva e Silva'), 
    ('MA327', 'Marcio Antonio de Faria Rosa'), ('MA327', 'Peter Sussner'), ('MA446', 'Plamen Emilov Kochloukov'), 
    ('MA453', 'José Régis Azevedo Varão Filho'), ('MA502', 'Paulo Regis Caron Ruffino'), ('MA502', 'Christian Horacio Olivera'), 
    ('MA602', 'Marcelo da Silva Montenegro'), ('MA621', 'Giuliano Angelo Zugliani'), ('MA705', 'Pedro José Catuogno'), 
    ('MA712', 'Marcelo Firer'), ('MA720', 'João Vitor da Silva'), ('MA724', 'Giuliano Angelo Zugliani'),
    ('MA740', 'Marcelo Firer'), ('MA902', 'José Régis Azevedo Varão Filho'), ('ME110', 'Victor Freguglia Souza'),
    ('ME111', 'Larissa Avila Matos'), ('ME115', 'Jesus Enrique Garcia'), ('ME173', 'Veronica Andrea Gonzalez Lopez'), 
    ('ME173', 'Mauricio Enrique Zevallos Herencia'), ('ME176', 'Hildete Prisco Pinheiro'), ('ME210', 'Caio Lucidius Naberezny Azevedo'), 
    ('ME210', 'Diego Fernando de Bernardini'), ('ME210', 'Alvaro Alexander Burbano Moreno'), ('ME310', 'Elcio Lebensztayn'), 
    ('ME310', 'Filidor Edilfonso Vilca Labra'), ('ME322', 'Veronica Andrea Gonzalez Lopez'), ('ME323', 'Felipe Augusto Fernandes'), 
    ('ME414', 'Elcio Lebensztayn'), ('ME601', 'Benilton de sa Carvalho'), ('ME607', 'Caio Lucidius Naberezny Azevedo'),
    ('ME613', 'Samara Flamini Kiihl'), ('ME623', 'Tatiana Andrea Benaglia Carvalho'), ('ME705', 'Mariana Rodrigues Motta'),
    ('ME712', 'Alex Rodrigo Dos Santos Sousa'), ('ME714', 'Hildete Prisco Pinheiro'), ('ME721', 'Everton Emanuel Campos de Lima'), 
    ('ME812', 'Mariana Rodrigues Motta'), ('ME908', 'Rafael Pimentel Maia'), ('ME920', 'Carlos Cesar Trucios Maza'), 
    ('ME921', 'Guilherme Vieira Nunes Ludwig'), ('ME951', 'Larissa Avila Matos'), ('MS123', 'Laercio Luis Vendite'), 
    ('MS149', 'Roberto Andreani'), ('MS149', 'Stefano de Leo'), ('MS211', 'Estevão Esmi Laureano'), 
    ('MS211', 'João Batista Florindo'), ('MS211', 'Michele Martins Lopes'), ('MS211', 'Ricardo Caetano Azevedo Biloti'), 
    ('MS213', 'Marcos Eduardo Ribeiro do Valle Mesquita'), ('MS380', 'Jayme Morandi Vaz'), ('MS380', 'Laecio Carvalho de Barros'), 
    ('MS512', 'Lucio Tunes Dos Santos'), ('MS513', 'Paulo Jose da Silva e Silva'), ('MS550', 'Jayme Morandi Vaz'), 
    ('MS580', 'Peter Sussner'), ('MS590', 'Maria Amelia Novais Schleicher'), ('MS620', 'Lázaro Aurélio Padilha Júnior'), 
    ('MS712', 'Maicon Ribeiro Correa'), ('MS728', 'Kelly Cristina Poldi'), ('MS902', 'Stefano de Leo'),
    ('MS904', 'Marcos Eduardo Ribeiro do Valle Mesquita'), ('MS943', 'Ricardo Caetano Azevedo Biloti'), 
    ('MS991', 'Giuseppe Romanazzi'), ('MS992', 'Roberto Andreani')
]

for materia, professor in mat_prof:
    preferencias[(professor, materia)] = 1

importancia = {m: 1 for m in materias} # Peso de relevância arbitrário

# Consideração máxima (irreal) criticada no relatório
disponibilidade = {(prof, hora): 1 for prof in professores for hora in horarios} 

# ==========================================
# 2. MODELAGEM (PU LP)
# ==========================================
alpha = 1
beta = 0

model = pulp.LpProblem("Course_Assignment", pulp.LpMaximize)

# Variáveis de decisão
x = pulp.LpVariable.dicts("x", [(p, m, h) for p in professores for m in materias for h in horarios], cat='Binary')
# y = pulp.LpVariable.dicts("y", [(m, s, h) for m in materias for s in salas for h in horarios], cat='Binary')

# Função objetivo
model += pulp.lpSum((alpha * preferencias[(p, m)] + beta * importancia[m]) * x[(p, m, h)] 
                    for p in professores for m in materias for h in horarios)

# ==========================================
# 3. RESTRIÇÕES
# ==========================================
# 3.1 Cada matéria é atribuída a exatamente um professor em um horário
for m in materias:
    model += pulp.lpSum(x[(p, m, h)] for p in professores for h in horarios) == 1

# 3.2 Cada professor pode ser atribuído a no máximo k matérias
k = 3
for p in professores:
    model += pulp.lpSum(x[(p, m, h)] for m in materias for h in horarios) <= k

# 3.3 Disponibilidade do professor
for p in professores:
    for h in horarios:
        for m in materias:
            model += x[(p, m, h)] <= disponibilidade[(p, h)]

# 3.4 Conflito de horários (um professor não pode ter mais de uma aula ao mesmo tempo)
for p in professores:
    for h in horarios:
        model += pulp.lpSum(x[(p, m, h)] for m in materias) <= 1

# 3.5 Blocos de dias (matérias devem seguir o bloco de dias designado)
for m in materias:
    for h in horarios:
        dia = dias[horarios.index(h) % len(dias)]
        if dia not in blocos[m]:
            for p in professores:
                model += x[(p, m, h)] == 0

# Restrições de salas (comentadas como constava no relatório por quebra do modelo)
# for h in horarios:
#     model += pulp.lpSum(x[(p, m, h)] for p in professores for m in materias) <= 1
# for m in materias:
#     model += pulp.lpSum(y[(m, s, h)] for s in salas for h in horarios) == 1
# disponibilidade_sala = {(s, h): 1 for s in salas for h in horarios}
# for h in horarios:
#     model += y[(m, s, h)] <= disponibilidade_sala[(s, h)]

# ==========================================
# 4. SOLUÇÃO E SAÍDA
# ==========================================
model.solve()

for p in professores:
    for m in materias:
        for h in horarios:
            if x[(p, m, h)].value() == 1:
                print(f"O professor {p} foi atribuído à matéria {m} no horário {h}")