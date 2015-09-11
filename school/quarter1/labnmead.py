  ### Nelder Mead lab
  ### Ben Zhang
  ### Period 2

  from math import sin, cos, pi, sqrt
  from vector import Vector
  from random import random
  from time import clock

  # Universal Constants
  DOMAIN_LIMIT = 10
  MAX_RUNTIME = .1

  # Nelder-Mead Constants
  MAX_TRIANGLES = 50
  SMALLEST_TRIANGLE_SIZE = 0.001

  # Hill Climb Constants
  MINIMUM_HILLCLIMB_RADIUS = 0.1
  INITIAL_HILLCLIMB_RADIUS = 1
  HILLCLIMB_RADIUS_DECREASE_FACTOR = 2
  HILLCLIMB_ANGLE_STEP = pi/16
  HILLCLIMB_GRID_PROBES = 100


  def main():
    runNelderMead()
    runRandomProbeSearch()
    runHillClimbRandomProbeSearch()
    runHillClimbGridSearch()
    
  def runHillClimbGridSearch():
    startTime = initializeClock()
    spacing = getGridSpacing()
    currentPoint = getBlankVector()
    temporarybest = hillClimbSinglePoint(currentPoint)
    iterations = 1
    while isWithinDomain(currentPoint.scalars()[1]):
      while isWithinDomain(currentPoint.scalars()[0]):
	if iterations >= HILLCLIMB_GRID_PROBES: break
	iterations += 1
	localBest = hillClimbSinglePoint(currentPoint)
	if localBest.cost() < temporarybest.cost():
	  temporarybest.equals(localBest)
	currentPoint.scalars()[0] += spacing
      currentPoint.scalars()[0] = 0
      currentPoint.scalars()[1] += spacing
    print("HillClimb with Grid Probing used", iterations, "iterations and found min at:", temporarybest, "with cost of", temporarybest.cost())
    reportTime(startTime)

  def getGridSpacing():
    return DOMAIN_LIMIT / sqrt(HILLCLIMB_GRID_PROBES)

  def isWithinDomain(coord):
    return coord < DOMAIN_LIMIT


  def runHillClimbRandomProbeSearch():
    startTime = initializeClock()
    iterations = 1
    temporarybest = hillClimbSinglePoint(randomVector())
    while haventExceededRuntime(startTime):
      iterations += 1
      localbest = hillClimbSinglePoint(randomVector())
      if localbest.cost() < temporarybest.cost():
	temporarybest.equals(localbest)
    print("HillClimb with Random Probing used", iterations, "iterations and found min at:", temporarybest, "with cost of", temporarybest.cost())
    reportTime(startTime)

  def hillClimbSinglePoint(start):
    temporaryresult = getBlankVector()
    temporaryresult.equals(start)
    currentRadius = INITIAL_HILLCLIMB_RADIUS
    while currentRadius > MINIMUM_HILLCLIMB_RADIUS:
      bestNeighbor = getMinNeighbor(temporaryresult, currentRadius)
      if bestNeighbor.cost() < temporaryresult.cost():
	temporaryresult.equals(bestNeighbor)
      currentRadius = currentRadius / HILLCLIMB_RADIUS_DECREASE_FACTOR
    return temporaryresult

  def getMinNeighbor(point, radius):
    temporaryresult = getBlankVector()
    temporaryresult.equals(point)
    for angle in frange(0, 2*pi, HILLCLIMB_ANGLE_STEP):
      pointOnRadius = Vector( point.scalars()[0] + radius * cos(angle), point.scalars()[1] + radius * sin(angle) )
      if pointOnRadius.cost() < temporaryresult.cost():
	temporaryresult.equals(pointOnRadius)
    return temporaryresult


  def runRandomProbeSearch():
    startTime = initializeClock()
    iterations = 1
    temporarybest = randomVector()
    while haventExceededRuntime(startTime):
      iterations += 1
      randomPoint = randomVector()
      if randomPoint.cost() < temporarybest.cost():
	temporarybest.equals(randomPoint)
    print("Random Probe used", iterations, "iterations and found min at:", temporarybest, "with cost of", temporarybest.cost())
    reportTime(startTime)

  def haventExceededRuntime(startTime):
    return getTimeSpent(startTime) < MAX_RUNTIME

  def runNelderMead():
    startTime = initializeClock()
    result, numSteps = neldermead(startTime)
    print("Nelder Mead used", numSteps , "iterations and found min at:",result,"with cost of:", result.cost())
    reportTime(startTime)

  def randomVectors():
    return randomVector(), randomVector(), randomVector()

  def initializeClock():
    startTime = clock()
    return startTime

  def randomVector():
    return Vector(random() * DOMAIN_LIMIT, random() * DOMAIN_LIMIT)

  def neldermead(startTime):
    iterations = 1
    a, b, c = randomVectors()
    temporarybest = neldermeadSingleTriangle(a, b, c)
    while haventExceededRuntime(startTime):
      iterations += 1
      a, b, c = randomVectors()
      localmin = neldermeadSingleTriangle(a, b, c)
      if localmin.cost() < temporarybest.cost():
	temporarybest.equals(localmin)
    return temporarybest, iterations

  def neldermeadSingleTriangle(A, B, C):
    tempsolution = B
    triangleCount = 0
    while True:
      tempsolution = neldermeadSingleStep(A, tempsolution, C)
      triangleCount += 1
      if tooManyTriangles or triangleTooSmall(A,B,C):
	break
    return tempsolution

  def tooManyTriangles(count):
    return count > MAX_TRIANGLES

  def triangleTooSmall(A, B, C):
    return getMinSide(A,B,C) < SMALLEST_TRIANGLE_SIZE

  def neldermeadSingleStep(vertex1, vertex2, vertex3):
    initialBest, initialMiddle, initialWorst = Vector.sort(vertex1,vertex2,vertex3)
    
    flippedWorst = initialBest + initialMiddle - initialWorst
    extendedFlippedWorst = (3 * (initialBest+initialMiddle) - 4 * initialWorst)/2
    shortenedFlippedWorst = (3 * (initialBest+initialMiddle) - 2 * initialWorst)/4
    shortenedWorst = (2 * initialWorst + initialBest + initialMiddle)/4
    midpointOfBestAndWorst = (initialWorst + initialBest)/2
    midpointOfBestAndMiddle = (initialBest + initialMiddle)/2
    
    if flippedWorst.cost() < initialWorst.cost() and extendedFlippedWorst.cost() < initialWorst.cost():
      initialWorst.equals(extendedFlippedWorst)
      return initialBest
      
    if flippedWorst.cost() < initialWorst.cost():
      initialWorst.equals(flippedWorst)
      return initialBest
    
    minOfShortenedWorstAndShortenedFlippedWorst = Vector(shortenedWorst)
    
    if shortenedFlippedWorst.cost() < shortenedWorst.cost():
      minOfShortenedWorstAndShortenedFlippedWorst.equals(shortenedFlippedWorst)
    
    if minOfShortenedWorstAndShortenedFlippedWorst.cost() < initialWorst.cost():
      initialWorst.equals(minOfShortenedWorstAndShortenedFlippedWorst)
      return initialBest
    
    initialWorst.equals(midpointOfBestAndWorst)
    initialMiddle.equals(midpointOfBestAndMiddle)
    return initialBest
    
  def frange(start, stop, step = -.01):
    i = start
    while i < stop:
      yield i
      i += step

  def getBlankVector():
    return Vector(0,0)

  def getMinSide(A, B, C):
    return min( A.dist(B), A.dist(C), B.dist(C) )

  def getTimeSpent(startTime):
    time = clock()
    return time - startTime
    
  def reportTime(startTime):
    print('--Search time =', round(getTimeSpent(startTime), 2), 'seconds')
    print()
    
  if __name__ == '__main__': main()
