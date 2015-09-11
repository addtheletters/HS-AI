#Ben Zhang
#Period 2
#12/11/13


def fizzbuzz(num):
  if (num % 3) == 0 and (num % 5) == 0:
    print('Fizz and Buzz')
  elif (num % 3) == 0:
    print('Fizz')
  elif (num % 5) == 0:
    print('Buzz')
  else:
    print(num)
      
      
fizzbuzz(5)
fizzbuzz(15)
fizzbuzz(3)
fizzbuzz(4)


#It worked.

"""
  Their solution may be efficient but also easily breakable. In a real-world situation, when many are manipulating the same code, this could cause problems.
  The programmer could be incompetent at organizing their code so that it is easily understandable. When working alone, they may excel, but on a team, 
  their messy coding would drag the project down. Besides coding quirks, they could also just be bad at working with others and accepting others' solutions.
  

"""