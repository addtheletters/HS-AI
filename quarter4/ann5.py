#   Back Propagate
#   (ANN 5?)
#   Ben Zhang
#   Period 2

#   2014-06-10

def matrixMult( V, M ):
      if len(V) != len(M):
        print( "Bad dimensions:", V, M )
        return 'error'
      
      W = [0] * len(M[0])
      for wIndex in range( len(W) ):
        W[wIndex] = sum( [ (V[ind] * M[ind][wIndex]) for ind in range(len(M)) ] )
      
      return W

class NeuralNetwork():
    def __init__(self, inputVector, numOfHiddenNodes1, targetVector, fileName = ''):
        self.learningRate       = 0.25
        self.inputVector        = inputVector + [-1]
        self.hiddenVector1      = [0]*numOfHiddenNodes1 + [-1]
        #self.hiddenVector2      = [0]*numOfHiddenNodes2 + [-1]
        self.outputVector       = [0]*len(targetVector)
        self.targetVector       = targetVector
        self.errorVector        = [0]*len(targetVector)
        self.sumOfSquaresError  = 1000

        self.matrix1 = self.initializeWeightMatrix(numOfHiddenNodes1, len(self.inputVector))
        #self.matrix1 = [[0.7, 0.2],[0.3, 0.5],[0.9, 0.1],[0.4, 0.6],]

        self.matrix2 = self.initializeWeightMatrix(len(self.hiddenVector1), len(self.outputVector))
        #self.matrix2 = [[0.4, 0.1, 0.6],[0.2, 0.9, 0.5],[0.3, 0.7, 0.8],]

        #self.matrix3 = self.initializeWeightMatrix(len(self.hiddenVector2), len(self.outputVector))
        #self.matrix3 = [[0.8, 0.2], [0.5, 0.4], [0.6, 0.3], [0.1, 0.7],]

        self.retreiveWeightsFromFile('')

        self.printMatrix(self.matrix1, 'matrix1')
        self.printMatrix(self.matrix2, 'matrix2')
        #self.printMatrix(self.matrix3, 'matrix3')

    def __repr__(self):
        self.print()
        return ''

    def print(self):
        print("Network Data:")
        print('input vector', self.inputVector)
        self.printMatrix(self.matrix1, 'matrix1')
        print('hv1', self.hiddenVector1)
        self.printMatrix(self.matrix2, 'matrix2')
        #print('hv2', self.hiddenVector2)
       # self.printMatrix(self.matrix3, 'matrix3')
        print('out', self.outputVector)
        print('targ', self.targetVector)
        print('err', self.errorVector)
        print('sumofsquareserr', self.sumOfSquaresError)
        print('learnrate', NeuralNetwork.learningRate)
        print('-'*10, '\n')

    def nodeValues(self, V, M):
        assert len(V) == len(M), [len(V), len(M), 'vector and metrix sizes not compatible for multiplying']
        VectorOfDotProducts = matrixMult(V, M)
        return self.sigmoid(VectorOfDotProducts)

    def sigmoid(self, vector):
        from math import exp
        nodeValueVector = []
        for n in range(len(vector)):
            nodeValueVector.append( 1/(1+exp( -vector[n]  )) )
        return nodeValueVector

    def initializeWeightMatrix(self, row, col):
        assert row > 0 and col > 0, 'row and col dims are negative'
        from random import random
        self.weightMatrix = [[random() * 0.8 + 0.2 for r in range(row)] for c in range(col)]
        return self.weightMatrix
        
    def computeErrorDifferences(self):
        assert len(self.targetVector) == len(self.outputVector), 'Target and output are diff lens'
        self.errorVector = [self.outputVector[k] - self.targetVector[k]
                            for k in range(len(self.targetVector))]

        squares = [ val * val for val in self.errorVector  ]
        
        self.sumOfSquaresError =  ( sum(squares) )

    def printMatrix(self, Lst, title = 'MATRIX'):
        assert type(Lst) == list and type(Lst[0]) == list, 'Tried to print non-matrix type'
        print('---'+title+':')
        for row in Lst:
            newRow = []
            for x in row:
                newRow.append(round(x, 4))
            for x in newRow:
                print('%11.4f'%x, end = '')
            print()
        print('==========')
        return

    def feedForward(self):
        self.hiddenVector1  = self.nodeValues(self.inputVector,     self.matrix1) + [-1]
        #self.hiddenVector2  = self.nodeValues(self.hiddenVector1,   self.matrix2) + [-1]
        self.outputVector   = self.nodeValues(self.hiddenVector1,   self.matrix2)
        self.computeErrorDifferences()

    def backPropagate(self):
        #print('Trying...')
        
        from copy import deepcopy
        
        matrixW = deepcopy(self.matrix2)
        matrixV = deepcopy(self.matrix1)
        
        delta1  = [ self.errorVector[k] * self.outputVector[k] * (1 - self.outputVector[k]) 
                   for k in range( len( self.outputVector ) ) ]
        matrixW = [ [ ( self.matrix2[j][k] - self.learningRate * delta1[k] * self.hiddenVector1[j] ) 
                     for k in range(len(self.outputVector))  ]
                     for j in range(len(self.hiddenVector1)) ]
        delta2  = [  (  sum([delta1[k]*self.matrix2[j][k] for k in range(len(self.outputVector))])
                        * self.hiddenVector1[j] * (1 - self.hiddenVector1[j])
                       )  for j in range(len(self.hiddenVector1)) ]
        matrixV = [ [ ( self.matrix1[i][j] - self.learningRate * delta2[j] * self.inputVector[i] ) 
                     for j in range(len(self.hiddenVector1)-1)  ]
                     for i in range(len(self.inputVector)) ]
        # Code written by Ben Zhang, class of 2015. Please respect the honor code.
        self.matrix2 = matrixW
        self.matrix1 = matrixV
        
        return
    
    def storeWeightsIntoFile(self, fileName):
        file1 = open(fileName, 'wb')
        import pickle
        pickle.dump([self.matrix1, self.matrix2], file1)
        file1.close()

    def verifyFileMatrixDimensions(self, candidateInputWeightMatrix, candidateHiddenWeightMatrix):
        if(len(self.candidateInputWeightMatrix) != len(InputWeightMatrix) or
           len(self.candidateInputWeightMatrix[0]) != len(InputWeightMatrix[0]) or
           len(self.candidateHiddenWeightMatrix) != len(HiddenWeightMatrix) or
           len(self.candidateHiddenWeightMatrix[0]) != len(HiddenWeightMatrix[0])):
            print('unmatching weights')
            #print statements ommitted
            exit()
            
    def retreiveWeightsFromFile(self, fileName):
        if fileName != '':
            file1 = open(fileName, 'rb')
            import pickle
            [candidateInputWeightMatrix, candidateHiddenWeightMatrix] = pickle.load(file1)
            file1.close()
            verifyFileMatrixDimensions(self.candidateInputWeightMatrix,
                                       self.candidateHiddenWeightMatrix)
            from copy import deepcopy
            self.InputWeightMatrix = deepcopy(candidateInputWeightMatrix)
            self.HiddenWeightMatrix = deepcopy(candidateHiddenWeightMatrix)
    
    
maxEpochsForTraining = 1

def main():
    print("Code made available on Github. Please respect the honor code.")
    print('Back propagate test!')
  
    x = NeuralNetwork(inputVector = [1, 0, 1],
                      numOfHiddenNodes1 = 2,
                      targetVector = [1, 0, 1],
                      fileName = '')
    
    for it in range(1001):
      x.feedForward()
      if it%100 == 0:
        print("----------------------------Iteration", it)
        x.printMatrix(x.matrix1, 'matrix1')
        x.printMatrix(x.matrix2, 'matrix2')
        print('sumofsquareserror =' , x.sumOfSquaresError / 2, '\n')
        print('----------------------------')
      x.backPropagate()

if __name__ == '__main__':
    from time import clock; START_TIME = clock(); main();
    print('runtime', round(clock() - START_TIME, 2), 'seconds')


