"""
Armand Isufaj

Electrical and Electronic Engineering
EE2702 Computer Science and Programming

Coursework Assignment 1 – Data Engineering and Presentation 

"""

import matplotlib.pyplot as armandplt

path_1 = [] 
path_2 = []


# function that joins the elements of a list into a string
def join(word):
   return "".join(word)


   

   

with open("data.txt", "r") as file:
    for line in file:

       # get the path
       if line.split()[5] == "enp1s0":
          path=path_1
       if line.split()[5] == "enp2s0":
          path=path_2

       # get the bit rate
       rate = (line.split()[8])
       splitRate = list(rate)
       if rate == '0' :
          path.append(float(rate))
          continue
 
       
          
       elif splitRate[-2] == 'K':
          del splitRate[-2:]
          rate = float(join(splitRate))/10**3
          path.append(rate)
          continue
          
       elif splitRate[-2] == 'M': 
           del splitRate[-2:]
           rate = float(join(splitRate))
           path.append(rate)
           continue

       else:
          del splitRate[-1]
          rate = float(join(splitRate))/10**6
          path.append(rate)
          continue
              
armandplt.grid()



armandplt.xlabel('Samples')
armandplt.ylabel('Data Rate [Mb/s]')

armandplt.plot(path_1, label="Path 1")
armandplt.plot(path_2, color = 'red', label="Path 2")
armandplt.legend()


fig2, (p1, p2) = armandplt.subplots(2)
p1.set_xlabel('Samples')
p1.set_ylabel('Data Rate [Mb/s]')

p2.set_xlabel('Samples')
p2.set_ylabel('Data Rate [Mb/s]')


p1.plot(path_1, label="Path 1")
p1.legend()
p2.plot(path_2, color = 'red', label="Path 2")
p2.legend()

armandplt.show()


            
