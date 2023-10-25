#problem 1
def print_values(a,b,c):
    if a > b:
        if b > c:
            print("a,b,c")
        if b <= c:
            if a > c:
                print("a,c,b")
            else:
                print("c,a,b")
    else:
        if b > c:
            if a > c:
                print("b,a,c")
            else:
                print("b,c,a")
        else:
            print("c,b,a")
print_values(15,17,14)
print_values(11,8,19)

