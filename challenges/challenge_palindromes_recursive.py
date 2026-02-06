def is_palindrome_recursive(word, low_index, high_index):
    # Caso base de segurança: se a string for vazia, não validamos como palíndromo
    if not word:
        return False

    # Caso base de sucesso: se os índices se encontrarem ou se cruzarem, 
    # significa que todas as letras correspondentes foram verificadas
    if low_index >= high_index:
        return True

    # Se os caracteres nas posições atuais forem diferentes, interrompemos a recursão
    if word[low_index] != word[high_index]:
        return False

    # Chamada recursiva movendo o índice inicial para frente e o final para trás
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)