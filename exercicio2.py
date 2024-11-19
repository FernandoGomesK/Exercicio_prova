lista1 = [1, 8, 3, 4, 5, 6]

def order_check2(x):
    order = []
    for i in x:
        if i > i+1:
            print("o número é menor que o anterior")
            order.append(i)
        elif i < i+1:
            print(" o número é maior que o anterior")
            order.append(i)
    print(order)
    
result = order_check2(lista1)
print(result)