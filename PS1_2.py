#problem 2
#2.1
import numpy as np
M1 = np.random.randint(0,51,50).reshape(5,10)
M2 = np.random.randint(0,51,50).reshape(10,5)
print("生成的矩阵M1为：")
print(M1)
print("生成的矩阵M2为：")
print(M2)   
#2.2
def Matrix_multip(Matrix1,Matrix2):
    result=np.zeros((5,5))
    for i in range(5):
        for j in range(5):
            for k in range(10):
                result[i][j] += Matrix1[i][k]*Matrix2[k][j]
    print("M1和M2相乘的结果是：")
    print(result)
Matrix_multip(M1,M2)

