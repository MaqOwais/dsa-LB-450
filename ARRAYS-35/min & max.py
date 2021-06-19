def MinMax(A):
    mini = A[0]
    maxi = A[0]
    for i in A:
        if i >= maxi:
            maxi = i
        elif i <= mini:
            mini = i
    
    return mini, maxi


if __name__ == '__main__':
    A = [0, 99 , -8, -94, 7, 2, 125, 6]
    ans = MinMax(A)
    print(ans)