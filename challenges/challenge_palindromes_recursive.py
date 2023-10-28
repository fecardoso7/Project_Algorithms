# Função recursiva para verificar se uma palavra é um palíndromo.
# Parâmetros:
# - word: a palavra a ser verificada.
# - low_index: índice inicial da palavra.
# - high_index: índice final da palavra.
# Retorna True se a palavra for um palíndromo, False caso contrário.
def is_palindrome_recursive(word, low_index, high_index):
    if not word:  # Se a palavra estiver vazia, não é um palíndromo.
        return False

    if low_index >= high_index:  # Se os índices se cruzarem, é um palíndromo.
        return True

    if word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
