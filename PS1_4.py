#problem 4
def Least_moves(x):
    if x <= 3:
        return x-1
    else:
        T=[0 for i in range(x+1)]
        T[1],T[2],T[3]=0,1,2
        for j in range(4,x+1):
            if j%2 != 0:
                T[j] = 1 + T[j-1]
            else:
                T[j] = 1 + min(T[j//2] , T[j-1])
        print(T[x])
Least_moves(5)

