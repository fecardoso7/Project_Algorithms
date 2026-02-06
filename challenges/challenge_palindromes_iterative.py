def is_palindrome_iterative(word):
    # Se a string estiver vazia, não há o que validar
    if not word:
        return False
    
    # Definição de ponteiros para percorrer a palavra de fora para dentro
    # 'low' começa no início e 'high' no último caractere
    low = 0
    high = len(word) - 1
    
    # O loop continua enquanto os ponteiros não se cruzarem no centro
    while low < high:
        # Se os caracteres nas extremidades forem diferentes, não é palíndromo
        if word[low] != word[high]:
            return False
        
        # Movemos os ponteiros um passo em direção ao meio
        low += 1
        high -= 1
        
    # Se chegarmos aqui, a palavra é idêntica de frente para trás e vice-versa
    return True