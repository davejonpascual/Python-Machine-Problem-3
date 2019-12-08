import matplotlib.pyplot as plt
import numpy as np
import math as m
print('Sample input mp3(np.array([[1,2],[3,4],...))')
print('')
print('Wherein 1 and 3 are the  are the x-components and \n2 and 4 are the y- components of \nthe data points')
def p3(comp):
    x = comp[:,0]
    y = comp[:,1]
    least=m.inf
    for ctr in range(11):
        if ctr>=len(x):
            break
        d=np.polyfit(x,y,ctr)
        f=np.polyval(d,x)
        n=y-f
        errorvector_norm=np.linalg.norm(n)
        if errorvector_norm<least:
            least=errorvector_norm
            bestfit=d
        return bestfit
        