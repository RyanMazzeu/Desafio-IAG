from datetime import datetime

data_atual = datetime.now()

# Obter o dia da semana em português
dias_da_semana = [
    "Segunda-feira",
    "Terça-feira",
    "Quarta-feira",
    "Quinta-feira",
    "Sexta-feira",
    "Sábado",
    "Domingo",
]
dia_da_semana = dias_da_semana[data_atual.weekday()]

# Formatar a data e a hora com o dia da semana
data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S") + " " + dia_da_semana

print(data_formatada)
