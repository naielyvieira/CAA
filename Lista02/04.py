def Elemento_majoritario(nums):
    candidato = None
    count = 0

    for num in nums:
        if count == 0:
            candidato = num
        count += 1 if num == candidato else -1

    count = 0
    for num in nums:
        if num == candidato:
            count += 1

    if count > len(nums) // 2:
        return candidato
    else:
        return None

# Exemplo de uso:
nums1 = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(Elemento_majoritario(nums1))

nums2 = [2, 2, 1, 1, 1, 2, 2]
print(Elemento_majoritario(nums2))
