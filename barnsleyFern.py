# import libraraies
import matplotlib.pyplot as plt 
from random import randint

# lists to plt the function
x = [0]
y = [0]


# gnerate 50000 random particles
for i in range (50000):

    # generate random particle from 1 - 100
    particle = randint(1,100)

    # conditions to test particles position
    if particle == 1:
        x.append(0)
        y.append(0.16* y[i])

    if particle >= 2 and particle <= 86: 
        x.append(0.85*(x[i]) + 0.04*(y[i])) 
        y.append(-0.04*(x[i]) + 0.85*(y[i])+1.6) 
      
    if particle >= 87 and particle <= 93: 
        x.append(0.2*(x[i]) - 0.26*(y[i])) 
        y.append(0.23*(x[i]) + 0.22*(y[i])+1.6) 
          
    if particle >= 94 and particle <= 100: 
        x.append(-0.15*(x[i]) + 0.28*(y[i])) 
        y.append(0.26*(x[i]) + 0.24*(y[i])+0.44)




# plot the function

plt.scatter(x, y, s = 0.2, c ='#5dbb63') 
plt.savefig('mandelbrot_set.png', dpi=300, bbox_inches='tight')
plt.axis("off")
plt.show()
