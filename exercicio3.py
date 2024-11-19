matrix = [[1, 2],
          [1, 2]]



def num_receiver():
    matrix = [[0,0], [0,0]]
    row = 0
    colum = 0
    for row in matrix:
        for colum in matrix:
            number = int(input("digite o número para inserir na matriz: "))
            matrix.append(number)
            
    return matrix
    
num_receiver()