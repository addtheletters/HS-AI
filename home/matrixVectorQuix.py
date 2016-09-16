    #       Matrix-Vector Multiplication 
    #       Ben Zhang
    #       Period 2
    #       5/7/14

    def matrixMult( V, M ):
      if len(V) != len(M):
        print( "Bad dimensions:", V, M )
        return 'error'
      
      W = [0] * len(M[0])
      for wIndex in range( len(W) ):
        W[wIndex] = sum( [ (V[ind] * M[ind][wIndex]) for ind in range(len(M)) ] )
      
      return W

    vec =   [14, 5, 5]
    matr = [ [1,  2,  3],
            [2, -1,  3],
            [3,  4, -2],]

    print( matrixMult(vec, matr) )
    
    