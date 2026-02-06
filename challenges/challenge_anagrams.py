# Função principal para verificar se duas strings são anagramas
def is_anagram(first_string, second_string):
    # Caso ambas as strings estejam vazias, retorna o padrão exigido com False
    if len(first_string) == 0 and len(second_string) == 0:
        return (first_string, second_string, False)

    # Normalização para minúsculas e conversão em listas para manipulação
    array_a, array_b = list(first_string.lower()), list(second_string.lower())

    # Aplicação do algoritmo Merge Sort para ordenar os caracteres
    # A ordenação é necessária para comparar as strings de forma linear
    array_a = merge_sort(array_a)
    array_b = merge_sort(array_b)

    # Reconstituição das listas ordenadas em strings para o retorno
    array_a, array_b = "".join(array_a), "".join(array_b)

    # Retorna a tupla contendo as strings ordenadas e o resultado da comparação
    return (array_a, array_b, array_a == array_b)


# Implementação do Merge Sort para garantir ordenação estável em O(n log n)
def merge_sort(numbers):
    # Condição de parada da recursão: listas com 0 ou 1 elemento já estão ordenadas
    if len(numbers) <= 1:
        return numbers

    # Divisão da lista ao meio para aplicar o conceito de 'Dividir para Conquistar'
    mid = len(numbers) // 2
    left_half = merge_sort(numbers[:mid])
    right_half = merge_sort(numbers[mid:])

    # Interpolação das partes ordenadas
    return merge(left_half, right_half)


# Função auxiliar para intercalar duas listas mantendo a ordem crescente
def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Compara os elementos das duas metades e insere o menor na lista final
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Adiciona os elementos restantes de ambas as listas, caso existam
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged