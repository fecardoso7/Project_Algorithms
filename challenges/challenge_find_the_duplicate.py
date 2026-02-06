def find_duplicate(nums):
    # Validação inicial: garante que a entrada seja uma lista válida e não vazia
    if not nums or not isinstance(nums, list):
        return False

    # Ordenação da lista para que números iguais fiquem adjacentes
    # Isso otimiza a busca para complexidade de tempo O(n log n)
    nums.sort()

    # Iteração comparando cada elemento com o seu sucessor
    for i in range(len(nums) - 1):
        # Validação de regra de negócio: apenas inteiros positivos são válidos
        if not isinstance(nums[i], int) or nums[i] < 0:
            return False
        
        # Se o elemento atual for igual ao próximo, encontramos o duplicado
        if nums[i] == nums[i + 1]:
            return nums[i]

    # Caso percorra toda a lista sem encontrar repetições, retorna False
    return False