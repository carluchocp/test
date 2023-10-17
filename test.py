c = False
d = True
i = 5
j = 6

resultado = ((i + j == c) and not d) or ((d != i and j == c) and not (i == (4 + j)))

print(resultado)