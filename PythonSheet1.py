#    EE2702 Computer Science and Programming
#    Handout 1




# Task 2 

'''

# What does the following Python program do? Explain. How can you change it to ask the user to
# input the value of x?




x = 1             # variable x is assigned a value of 1
if x<1:           # if x is less than 1 print x+10 
    print(x+10)
else:             # if x is NOT less than 1, x gets assigned a new value. x=x+1 then print the new x 
    x=x+1
    print(x)


#How can you change it to ask the user to input the value of x? 

x = int(input('input a number:') )            # user is promted to input a value for x




'''

# Task 3



# For any three integer numbers user chooses to input, write a short Python code that determines and prints the largest.





'''

number1 = int(input('Input first integer number :')) 
number2 = int(input('Input second integer number :'))
number3 = int(input('Input third integer number :'))
i=0

while True:
    

    if number1<number2:
        i=number1
        number1=number2
        number2=i

    if number2<number3:
        i=number2
        number2=number3
        number3=i

    if number1>number2>number3:
        break
print(number1)



'''

# Task 4


# What does the following code do?

'''

a = int(input('Enter a value for a: '))     # user inputs value for 'a'
xyz = int(input('Enter a value for xyz: '))      # user inputs value for 'xyz'


if a<xyz:                                   # if 'xyz' is larger than 'a'
           xyz += a                         # '+=' Adds a value and the variable and assigns the result to that variable.
            
elif a>xyz:
           xyz = 2*a                        # if 'a' is larger than 'xyz' 
           
else:
           xyz = a+1
print(xyz)

'''



# Task 5

# Write Python code to calculate the square root of a given integer number, using the Babylonian method 
'''

number = float(input('Square root of :'))
initialGuess =float(input(' Initial Guess for the square root of {} :'.format(number)))


while True:
    
    root=(initialGuess+number/initialGuess)/2
    print(root)
    error= initialGuess-root
    
    initialGuess=root
    if error==0:
        break
print('The root of {} is {} '.format(number,root))




'''

# Task 6

# Write a code that calculates factorial of a given integer number. 

'''

number = int(input('Factorial of :'))
factorial=1

for i in range(1,number+1):
    factorial=factorial*i

print(factorial)


'''



# Task 7
# A farmer owns pigs and chickens. One morning he counts the animals: there are 56 legs and 20 heads.



# a)Write a program (using a loop) to calculate the number of pigs and the number of chickens in the farmyard. 









'''

heads = 20
legs  = 56



for p in range(1,heads+1):
    c = heads - p
    totalLegs = 4*p + 2*c
    if totalLegs== legs:
        print('numer of Pigs: ',p)
        print('number of Chickens: ',c)
        break


print('There are {} pigs and {} chickens'.format(p,c))

'''


# b) Change the code to allow for the user to introduce the number of heads and legs and give a comment if these number are wrong (if the number of pigs and chickens cannot be calculated)


'''
heads = int(input('How many heads?: '))
legs = int(input('How many legs?: '))



for p in range(1,heads+1):
    c = heads - p
    totalLegs = 4*p + 2*c
    if totalLegs== legs:
        print('numer of Pigs: ',p)
        print('number of Chickens: ',c)
        break


print('There are {} pigs and {} chickens'.format(p,c))




'''



# Task 8

#  Prime Factorization Algorithm

number = int(input('Pick an integer: '))
divisor = int(2)
factors=[]


while True:
    numberNew = number/divisor
    print(numberNew)
    div=divmod(number,divisor)
    if div[1]==0:
        number = numberNew
        factors.append(divisor)
        if number ==1:
            break
        continue
    if div[1]!=0:

        
        divisor += 1
        number = number/divisor
        factors.append(divisor)


print(factors)






     

        
    
