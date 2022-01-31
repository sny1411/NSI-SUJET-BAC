def recherche(caractere : str, mot : str) -> int:
    i = 0
    for elt in mot:
        if elt == caractere:
            i += 1
    return i

print(recherche("e","sciences"))
print(recherche('i',"mississippi"))

pieces=[100,50,20,10,5,2,1]

def rendu_glouton(arendre, solution, i):
    global pieces
    if arendre == 0:
        return solution
    p = pieces[i]
    if p <= arendre:
        solution.append(p)
        return rendu_glouton(arendre - p, solution, i)
    else:
        return rendu_glouton(arendre,solution, i + 1)

print(rendu_glouton(68, [], 0))
print(rendu_glouton(291, [], 0))