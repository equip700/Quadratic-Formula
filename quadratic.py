import math
print 'Ax^2+Bx+C = 0'
A=input('What is your coefficient for A: ')
B=input('What is your coefficient for B: ')
C=input('What is your coefficient for C: ')
print 'Your factors are: '
print ((-B)+math.sqrt((B*B)-(4*A*C)))/(2*A)
print 'and'
print ((-B)-math.sqrt((B*B)-(4*A*C)))/(2*A)
