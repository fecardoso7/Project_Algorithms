def encrypt_message(message, key):
    # Validações de tipo obrigatórias para garantir a integridade dos parâmetros
    if not isinstance(message, str):
        raise TypeError("tipo inválido para message")
    if not isinstance(key, int):
        raise TypeError("tipo inválido para key")

    # Se a chave estiver fora dos limites da string, apenas invertemos a mensagem toda
    if key < 1 or key >= len(message):
        return message[::-1]

    # Divide a mensagem em duas partes com base na posição da chave
    part_one = message[:key]
    part_two = message[key:]

    # Regra de criptografia baseada na paridade da chave
    if key % 2 != 0:
        # Se a chave for ÍMPAR: inverte as duas partes e mantém a ordem (part1_part2)
        return f"{part_one[::-1]}_{part_two[::-1]}"
    else:
        # Se a chave for PAR: inverte as duas partes e inverte a ordem (part2_part1)
        return f"{part_two[::-1]}_{part_one[::-1]}"