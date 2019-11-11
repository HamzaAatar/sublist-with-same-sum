def partition(n):

    x = list(range(1, n+1))
    s, s_1, s_2 = 0, 0, 0

    for i in x:
         s += i

    if n%4 == 0:

        print("{}==>{}".format(x, s))

        N_1 = x[0:int(n/4)] + x[n-int(n/4):n]
        N_2 = x[int(n/4):n-int(n/4)]

        for i in N_1:
            s_1 += i
        for j in N_2:
            s_2 += j

        print('{}==>{}\n{}==>{}'.format(str(N_1), str(s_1), str(N_2), str(s_2)))

    elif n%4 == 3:

        print(x)
        print(s)

        N_1 = x[0:int((((n-1)/2)+1)/2)-1] + x[n-int((((n-1)/2)+1)/2):n]
        N_2 = x[int((((n-1)/2)+1)/2)-1:n-int((((n-1)/2)+1)/2)]

        for i in N_1:
            s_1 += i
        for j in N_2:
            s_2 += j

        print('{}==>{}\n{}==>{}'.format(str(N_1), str(s_1), str(N_2), str(s_2)))

    else :

        print("Oops, I cant't create a partition. :/ ")


partition(6400)
