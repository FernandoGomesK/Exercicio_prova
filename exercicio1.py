p = input("digite True ou False para as frases: ")
q = input("digite True ou False para as frases: ")
r = input("digite True ou False para as frases: ")


def logic_checker1(p, q):
    if p == True and q == True:
        r = True
        return r
    else:
        print("frase falsa")
        r = False
        return r
    
def logic_checker2(r, q):
    if r == False or q == True:
        return True
    else:
        return False
    
def logic_checker3(p,q):
    if p == False and q == False:
        return True
    else:
        return False
    
phrase = logic_checker1(p, q)
print(f"se p for {p}, q for {q}, e r for {r} na frase('se p ou q forem verdadeiros, então r'), o resultado é {phrase}")
phrase2 = logic_checker2(r, q)
print(f"se p for {p}, q for {q}, e r for {r}. Na frase('se não for r ou q, então é verdadeiro'), o resultado é {phrase2}")
phrase3 = logic_checker3(p, q)
print(f"se p for {p}, q for {q}, e r for {r}. Na frase('se não p e não q'), o resultado é {phrase3} ")

