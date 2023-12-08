def maior_subsequência(S):
    n = len(S)
    dp = [[0] * n for _ in range(n)]
    

    for i in range(n):
        dp[i][i] = 1
    

    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if S[i] == S[j] and cl == 2:
                dp[i][j] = 2
            elif S[i] == S[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
    

    resultado = []
    i, j = 0, n - 1
    while i < j:
        if S[i] == S[j]:
            resultado.append(S[i])
            i += 1
            j -= 1
        elif dp[i][j - 1] > dp[i + 1][j]:
            j -= 1
        else:
            i += 1
    
    if i == j:
        resultado.append(S[i])
    
    return resultado

# Exemplo de uso:
sequencia = "ACGTGTCAAAATCG"
resultado = maior_subsequência(sequencia)
print("Subsequência palíndroma de tamanho máximo:", "".join(resultado))
