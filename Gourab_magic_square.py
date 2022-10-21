def MagicSquare(n):
    if n % 2 == 0:
        print("This magic square is valid for only odd positive integers.")
        print()
    else:
        magicsquare = [[0 for i in range(n)] for j in range(n)]
        i = n // 2
        j = n - 1
        num = 1
        while num <= n ** 2:
            if i == -1 and j == n:
                i = 0
                j = n - 2
            else:
                if i == -1:
                    i = n - 1
                elif j == n:
                    j = 0
            if magicsquare[i][j] != 0:
                i = i + 1
                j = j - 2
                continue
            else:
                magicsquare[i][j] = num
                num = num + 1
            i = i - 1
            j = j + 1
        print("Magic Square of order is", n)
        print("Sum of each row/column/diagonal is", int((n * (n ** 2 + 1)) / 2), "\n")
        for i in range(n):
            for j in range(n):
                print(magicsquare[i][j], end=" ")
            print()


n = int(input("Enter the order of the magic square: "))
MagicSquare(n)

