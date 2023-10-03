### Handout 3



import random

### Question 1
##
##
##string = str(input("Input a string:"))
##
##
##letterList = []
##c = collections.Counter(string)
##for letter in string :
##    if letter in letterList:
##      continue
##    letterList.append(letter)
##    print ('{} : {}'.format(letter, c[letter]))
##

# Question 2

##string1 = str(input("Input string 1 :"))
##string2 = str(input("Input string 2 :"))
##
##letterList = []
##letterListCommon = []
##
##for letter in string1 :
##    if letter in letterList:
##      continue
##    letterList.append(letter)
##
##for letter in string2 :
##    if letter in letterListCommon :
##      continue
##    if letter in letterList :
##      letterListCommon.append(letter)
##      
##
##lengthList = len(letterListCommon)
##print(" The two strings have {} letters in common,{}".format(lengthList,letterListCommon) )

    
# Question 3



##for x in range(1, 5):
## print('{0:2d} {1:2d} {2:2d} {3:2d} '.format(x, x*x, x*x*x,x*x*x*x))

# Question 4

##n =10000
##results = []
##
##for i in range(n):
##  roll = random.randrange(1,7,1)
##  results.append(roll)
##for i in range (1,7):
##  print("{}:{}".format(i,results.count(i)))




# Question 5

n =10

prob = 0

for i in range(n):
  result1 = []
  result2 = []

  for j in range(24):
    roll1 = random.randrange(1,7,1)
    roll2 = random.randrange(1,7,1)
    result1.append(roll1)
    result2.append(roll2)
  
  if 6 in result1 or result2:
      continue
  else:
    prob = (prob + 1)/i
      


print("{:1f}".format(prob))



