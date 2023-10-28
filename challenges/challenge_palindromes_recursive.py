# Função recursiva para verificar se uma palavra é um
# palíndromo.
def is_palindrome_recursive(word, low_index, high_index):
    if not word:  # Se a palavra estiver vazia, não
        return False

    if low_index >= high_index:  # Se índices se
        return True

    if word[low_index] != word[high_index]:  # Se
        return False

    # Chama recursivamente com índices alterados
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
