def study_schedule(permanence_period, target_time):
    try:
        # Inicializa o contador para os estudantes presentes no horário alvo
        count = 0
        
        # Itera sobre cada tupla (entrada, saída) na lista de períodos
        for beginning, finish in permanence_period:
            # Verifica se o horário alvo está dentro do intervalo inclusivo [entrada, saída]
            if beginning <= target_time <= finish:
                count += 1
        
        # Retorna o total de alunos que estavam estudando naquele momento
        return count
        
    except TypeError:
        # Caso target_time ou os dados no período sejam inválidos (ex: None ou String),
        # o erro é capturado para retornar None conforme a especificação.
        return None