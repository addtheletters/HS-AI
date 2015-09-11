#   GAs
#   Ben Zhang
#   Period 2

from random import random

def randGene( length ):
  gene = [ str(int(random()+0.5)) for i in range(length) ]
  gene = ''.join(gene)
  return gene
  
def randCritter( numGenes, geneLen ):
  critter = [ randGene(geneLen) for i in range(numGenes)]
  return critter

def fitnessFunc( gene ):
    fitval = 0
    for item in gene:
        if item == '1':
            fitval += 1
    return fitval
  
def fitnessFunc_Multi( critter ):
    fitval = 0
    for gene in critter:
      fitval += fitnessFunc(gene)
    return fitval
  
def sortOnFitness( genes ):
  fitnesses = [0] * len(genes)
  for i in range(len(genes)):
    fitnesses[i] = fitnessFunc(genes[i])
  ssorted = []
  while max(fitnesses) > 0:
    ind = fitnesses.index(max(fitnesses))
    ssorted.append( genes[ind] )
    fitnesses[ind] = -1
  return ssorted

def sortOnFitness_Multi( critters ):
  fitnesses = [0] * len(critters)
  for i in range(len(critters)):
    fitnesses[i] = fitnessFunc_Multi(critters[i])
  ssorted = []
  while max(fitnesses) > 0:
    ind = fitnesses.index(max(fitnesses))
    ssorted.append( critters[ind] )
    fitnesses[ind] = -1
  return ssorted

def mate( ga, gb ):
    # length of ga and gb should be the same
    glen = len(ga)
    crossPoint = int(random() * glen)
    mated1 = ga[:crossPoint] + gb[crossPoint:]
    mated2 = gb[:crossPoint] + ga[crossPoint:]
    
    return [mated1, mated2]

def mate_multi( ca, cb ):
    child1 = []
    child2 = []
    for ind in range(len(ca)): #each chromosome
      chrompair = mate( ca[ind], cb[ind] )
      child1.append( chrompair[0] )
      child2.append( chrompair[1] )
    return [child1, child2]
    
def threshCull( genes, threshold = 5 ):
    filtered = genes[:]
    for gene in genes:
        if fitnessFunc( gene ) < threshold:
            filtered.remove(gene)
    return filtered

def mateRandomly( genes, numchildren = 10 ):
    count = 0
    out = []
    while count < numchildren:
        parentA = genes[int(random() * len(genes))]
        parentB = genes[int(random() * len(genes))]
        chlds = mate( parentA, parentB )
        out.append( chlds[0] )
        out.append( chlds[1] )
        count += 2
    return out

def runGeneration_threshold( genes, threshold ):
    genes = sortOnFitness(genes)
    culled = threshCull(genes, threshold)
    children = mateRandomly(culled, len(genes))
    return children

def runGeneration_topToBottom( genes ):
    genes = sortOnFitness(genes)
    count       = 0
    currPA      = 0
    currPlus    = 1
    children = []
    while count < len(genes):
        chlds = mate(genes[currPA], genes[currPA+currPlus])
        children.append( chlds[0] )
        children.append( chlds[1] )
        count           += 2
        currPlus        += 1
        if currPlus > (len(genes) // 2):
          currPlus       = 1
          currPA        += 1
    return children
  
def runGeneration_topToBottom_Multi( critters ):
    critters = sortOnFitness_Multi(critters)
    count       = 0
    currPA      = 0
    currPlus    = 1
    children = []
    while count < len(critters):
        #print(critters)
        chlds = mate_multi(critters[currPA], critters[currPA+currPlus])
        
        #print('mating', currPA, currPA + currPlus)
        children.append( chlds[0] )
        children.append( chlds[1] )
        count           += 2
        currPlus        += 1
        if currPlus > (len(critters) // 2):
          currPlus       = 1
          currPA        += 1
    return children
    

def showGen_Multi( msg, critters ):
  print(msg)
  for critter in critters:
    print( fitnessFunc_Multi(critter), ":", critter )

from math import sin

def ga3_fitnessFunc(item):
  xval = int(item[:10], 2)
  yval = int(item[10:], 2)
  return xval * sin(4 * xval) + 1.1 * yval * sin(2 * yval)



#print(fitnessFunc("1010101010"))

#--------------GA1
"""
currgen = ["00000000000",
           "01011000000",
           "10111111001",
           "01000001010",
           "11110111110",
           "00010100100",
           ]
           
currgen = randCritter( 6, 8 )
print( "original",currgen )
for i in range(5):
   currgen = runGeneration_topToBottom(currgen)
   print( "gen", i, currgen )
#------------------
"""

#------------GA2

currgen = [randCritter(10, 10) for i in range(6) ]
showGen_Multi('original', currgen)
for i in range(6):
  currgen = runGeneration_topToBottom_Multi(currgen)
  showGen_Multi('gen ' + str(i), currgen)

#---------------


#------------GA3



#---------------




