# Função para calcular a quantidade de períodos de
# permanência que incluem o horário alvo.
def study_schedule(permanence_period, target_time):
    try:
        count = 0  # Inicializa a contagem de períodos de
        for beginning, finish in permanence_period:
            if beginning <= target_time <= finish:  # Verifica se
                count += 1  # Incrementa a contagem se o período
        return count  # Retorna o número de períodos que
    except TypeError:
        return None  # Retorna None se houver um erro de tipo
