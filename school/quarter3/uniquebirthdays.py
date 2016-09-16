#       Ben Zhang      
#       Period 2
#       25 February 2014
#       Unique Birthdays Problem Quiz

#       I have neither given nor received any help in writing this program.

from random import randint
from time import clock

def main():

    # Constants
    population = 5000
    possibledays = 36500
    
    # For a population size and a number of possible birthdays to choose from,
    # we will attempt to determine how many people and what percentage of people
    # will have unique birthdays.
    # This assignment was completed in 2015. Please follow the honor code.
    uniquedaycount = population # Starting off, we assume every birthday is unique.
                                # For every generated birthday that isn't unique, we will
                                # decrease this count.
    
    birthdays = set()           # Generated birthdays will be stored in this set.
                                # If a non-unique birthday is attempted to be added,
                                # the size of the set will not change.
    
    repeatedBirthdays = set()   # This will store birthdays that we know are non-unique.
                                # If we come across a non-unique birthday that is already
                                # in this set, we only decrease our uniquedaycount by one.
                                # If our new non-unique birthday has not already been found,
                                # our uniquedaycount is reduced by two, as the original
                                # is no longer unique.
    
    # Here we iterate over the population.
    for i in range(population):
      oldlen = len(list(birthdays))                     # Getting the size of the set 
                                                        # before attempting to add a new birthday
      birthday = randint( 1, possibledays )
      birthdays.add( birthday )                         # Attempting to add a new birthday.
      
      if oldlen == len(list(birthdays)):                # If the set of birthdays has the same size...
        uniquedaycount = uniquedaycount - 1             # there's one less unique birthday overall.
        
        if birthday not in repeatedBirthdays:           # If we didn't previously know the day was repeated,
          uniquedaycount = uniquedaycount - 1           # further reduce our count
          repeatedBirthdays.add(birthday)               # and add the day to our known repeat set
    
    # Printing results.
    print( "Results: " )
    print( uniquedaycount, "people, or", \
      str(round(100 * uniquedaycount / population, 1)) + "%, have no duplicate birthdays.")
    print( "[ pop. size =", population, "; possible b-days =", possibledays,"]")
    
  
if __name__ == '__main__':
  print("Code written by Ben Zhang, TJ class of 2015. Please respect the honor code.")
  START_TIME = clock(); main()
  print( "\n --> Runtime was", round(clock() - START_TIME, 2), "seconds. <--" )
  
#       Sample output:
#       ------

#       Results: 
#       4338 people, or 86.8%, have no duplicate birthdays.
#       [ pop. size = 5000 ; possible b-days = 36500 ]
#       
#        --> Runtime was 0.48 seconds. <--
