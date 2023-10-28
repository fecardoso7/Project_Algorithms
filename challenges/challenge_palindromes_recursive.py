# Função recursiva para verificar se uma palavra é um palíndromo.
def is_palindrome_recursive(word, low_index, high_index):
    if not word:  # Se a palavra estiver vazia, não é um palíndromo.
        return False

    if low_index >= high_index:  # Se os índices baixo e alto se cruzarem, é um palíndromo.
        return True

    if word[low_index] != word[high_index]:  # Se os caracteres nos índices baixo e alto são diferentes, não é um palíndromo.
        return False

    # Chama a função recursiva com os índices baixo aumentado e alto diminuído para verificar os caracteres seguintes.
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
