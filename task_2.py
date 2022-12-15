for X in 0,1:
    for Y in 0,1:
        for Z in 0,1:
            print('X = ', X, ', Y = ' , Y, ', Z = ', Z, ':',((not(X or Y or Z))==(not(X))and (not(Y))and(not(Z))))
