# Função para calcular a quantidade de períodos de permanência
# que incluem o horário alvo.
def study_schedule(permanence_period, target_time):
    try:
        count = 0  # Inicializa a contagem de períodos inclusivos.
        for beginning, finish in permanence_period:
            if beginning <= target_time <= finish:
                count += 1
        return count  # Retorna o número de períodos que incluem o horário.
    except TypeError:
        return None  # Retorna None se houver erro de tipo durante a execução.
