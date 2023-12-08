#Solução Simples (Complexidade O(n²)):
def complexidade_simples(num, X):
    n = len(num)
    for i in range(n):
        for j in range(i + 1, n):
            if num[i] + num[j] == X:
                return [i, j]

# Exemplo de uso:
num1 = [2, 7, 11, 15]
X1 = 9
print("\nComplexdade simples:")
print(complexidade_simples(num1, X1)) 

num2= [3, 2, 4]
X2 = 6
print(complexidade_simples(num2, X2)) 


#Solução Melhorada (Complexidade abaixo de O(n²)):
def complexidade_melhorada(nums, X):
    num_indices = {}  # Dicionário para armazenar os índices dos números
    for i, num in enumerate(nums):
        complemento = X - num
        if complemento in num_indices:
            return [num_indices[complemento], i]
        num_indices[num] = i

# Exemplo de uso:
nums1 = [2, 7, 11, 15]
X1 = 9
print("\nComplexdade melhorada:")
print(complexidade_melhorada( nums1, X1))

nums2 = [3, 2, 4]
X2 = 6
print(complexidade_melhorada(nums2, X2))



#Solução Melhor Caso (Complexidade O(n)):
def complexidade_melhor_caso(nums, X):
    num_indices = {}
    for i, num in enumerate(nums):
        complemento = X - num
        if complemento in num_indices:
            return [num_indices[complemento], i]
        num_indices[num] = i

# Exemplo de uso:
nums1 = [2, 7, 11, 15]
X1 = 9
print("\nComplexdade de melhor caso:")
print(complexidade_melhor_caso(nums1, X1))

nums2 = [3, 2, 4]
X2 = 6
print(complexidade_melhor_caso(nums2, X2))


