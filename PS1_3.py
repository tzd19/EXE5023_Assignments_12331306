#problem 3
def Pascal_triangle(k):
    triangle = [[1],[1,1]]
    for i in range(2,k):
        pre = triangle[i-1]
        cul = [1]
        for j in range(i-1):
            cul.append(pre[j]+pre[j+1])
        cul.append(1)        
        triangle.append(cul)
    print("帕斯卡三角形的第{}行为：{}".format(k,triangle[k-1]))
Pascal_triangle(5)
Pascal_triangle(6)
Pascal_triangle(100)
Pascal_triangle(200)

