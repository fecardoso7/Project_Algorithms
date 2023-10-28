# Função para calcular a quantidade de períodos de permanência que incluem o horário alvo.
def study_schedule(permanence_period, target_time):
    try:
        count = 0  # Inicializa a contagem de períodos de permanência que incluem o horário alvo.
        for beginning, finish in permanence_period:
            if beginning <= target_time <= finish:  # Verifica se o horário alvo está dentro do período.
                count += 1  # Incrementa a contagem se o período incluir o horário alvo.
        return count  # Retorna o número de períodos que incluem o horário alvo.
    except TypeError:
        return None  # Retorna None se houver um erro de tipo durante a execução.
