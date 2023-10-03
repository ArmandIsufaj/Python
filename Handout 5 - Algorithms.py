"""
EE2702 Computer Science and Programming
Spring 2020
Handout 5 – Algorithms (part 1)

Armand Isufaj

"""


# Algorithm 1: Calculation of the square root, babylonian style




def getNumber():

  root = int(input("Find the root of:"))
  guess = int(input("Initial guess for the root of {}:".format(root)))
  return root, guess


def calc(root,guess):

  res = 1e-6
  error = 1
   

  
  while res < error:
    xold = guess
    xnew = 0.5*(xold +(root/xold))
    error = abs(root-xnew*xnew)
    guess = xnew
    solution = guess
  return solution

  
def main():
  root,guess = getNumber()
  sol = calc(root,guess)
  print("The root of {} is {:f}".format(root,sol))

main()
