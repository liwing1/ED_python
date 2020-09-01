def primo(n):
    if n == 1:
        return "Não primo."
    for i in range(2, n):
        if (n % i == 0):
            return "Não primo."
    return "Primo."


print(primo(1))
