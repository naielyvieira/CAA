def partition(S, p, r):
    piv = S[p] 
    q1 = p  
    q2 = p 

    for k in range(p + 1, r + 1):
        if S[k] < piv:
           
            S[q2 + 1], S[k] = S[k], S[q2 + 1]
            q1 += 1
            q2 += 1
        elif S[k] == piv:
           
            S[q2 + 1], S[k] = S[k], S[q2 + 1]
            q2 += 1

    return q1, q2

# Exemplo de uso:
S = [4, 2, 7, 1, 5, 3, 8, 6]
p = 1
r = 7

q1, q2 = partition(S, p, r)

print("Índices q1 e q2:", q1, q2)
print("Vetor rearranjado:", S)
