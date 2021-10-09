# https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python
# NAO CONSEGUI

def determinant(matrix):

    len_matrix = len(matrix)
    
    if len_matrix == 1:
        return matrix[0][0]
    elif len_matrix == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    elif len_matrix == 3:
        value = 1
        result1 = 0
        result2 = 0
        values1 = []
        values2 = []

        for i in range(0, len_matrix):
            for j in range(0, len(matrix[i]) - 1):
                matrix[i].append(matrix[i][j])

        matrix.append(matrix[0] + matrix[0])
        matrix.append(matrix[1] + matrix[1])

        j = 0
        i = 0

        for i in range(0,len_matrix):
            for j in range(0, len_matrix):
                value *= matrix[j][j+i]
                if j == len_matrix - 1:
                    values1.append(value)
                    value = 1

        j = 0
        i = 0

        for i in range(0,len_matrix):
            for j in range(0, len_matrix):
                value *= matrix[j][-1-j-i]
                if j == len_matrix - 1:
                    values2.append(value)
                    value = 1
            
        for value in values1:
            result1 += value

        for value in values2:
            result2 += value

        return result1 - result2
    #else:
       
        #     value = 1
        #     result1 = 0
        #     result2 = 0
        #     values1 = []
        #     values2 = []

        #     for i in range(0, len_matrix):
        #         for j in range(0, len(matriz[i]) - 1):
        #             matriz[i].append(matriz[i][j])

        #     matriz.append(matriz[0] + matriz[0])
        #     matriz.append(matriz[1] + matriz[1])

        #     j = 0
        #     i = 0

        #     for i in range(0,len_matrix):
        #         for j in range(0, len_matrix):
        #             value *= matriz[j][j+i]
        #             if j == len_matrix - 1:
        #                 values1.append(value)
        #                 value = 1

        #     j = 0
        #     i = 0

        #     for i in range(0,len_matrix):
        #         for j in range(0, len_matrix):
        #             value *= matriz[j][-1-j-i]
        #             if j == len_matrix - 1:
        #                 values2.append(value)
        #                 value = 1
                
        #     for value in values1:
        #         result1 += value

        #     for value in values2:
        #         result2 += value

        #     return result1 - result2

        print(new_matrix3[0])


        print(new_matrix)
        print(new_matrix1)
        print(new_matrix2)
        print(new_matrix3)

# print(determinant([ [3,1,-2,1],[5,2,2,3],[7,4,-5,0],[1,-1,11,2] ]))

matrix = [ [3,1,-2,1],[5,2,2,3],[7,4,-5,0],[1,-1,11,2] ]

len_matrix = len(matrix)

values1 = []
new_matrix = []
new_matrix1 = []
new_matrix2 = []
new_matrix3 = []

for i in range(0, len_matrix):
    values1.append(matrix[0][i])
    if not i == 0:
        new_matrix.append(matrix[i])

i = 0

for i in range(0, len_matrix):
    for j in range(0, len(new_matrix)):
        for k in range(0, len(new_matrix)):
            if i == 0:
                new_matrix1.append(new_matrix[j][k+1])
            
            elif k >= 1 and i == 1:
                new_matrix1.append(new_matrix[j][k+1])
            elif k >= 2 and i == 2:
                new_matrix1.append(new_matrix[j][k + 1])
            elif k >= 3 and i == 3:
                new_matrix1.append(new_matrix[j][k + 1])
            elif k >= 4 and i == 4:
                new_matrix1.append(new_matrix[j][k + 1])
            elif k >= 5 and i == 5:
                new_matrix1.append(new_matrix[j][k + 1])
            elif k >= 6 and i == 6:
                new_matrix1.append(new_matrix[j][k + 1])
            elif k >= 7 and i == 7:
                new_matrix1.append(new_matrix[j][k + 1])
            elif k >= 8 and i == 8:
                new_matrix1.append(new_matrix[j][k + 1])
            elif i + 1 == len(new_matrix):
                new_matrix1.append(new_matrix[j][k])
            else:
                new_matrix1.append(new_matrix[j][k])

            if k + 1 == len(new_matrix):
                new_matrix2.append(new_matrix1)
                new_matrix1 = []

    new_matrix3.append(new_matrix2)
    new_matrix2 = []

aaaaa = []

for matriz in new_matrix3:
    aaaaa.append(determinant(matriz))

conta = 0

print(values1)
print(aaaaa)

for l in range(0,len(aaaaa)):
    conta += values1[l]*aaaaa[l]

print(conta)