import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from math import atan2, degrees

    
def SVD(matrix):
    U, d, V = np.linalg.svd(matrix, full_matrices=True)
    s = d.shape[0]
    D = np.zeros((U.shape[1], V.shape[0]))
    D[:s,:s] = np.diag(d)
    return [U,D,V]

def showDecomp(matrix):
    decomp = SVD(matrix)
    U = decomp[0]
    D = decomp[1]
    V = decomp[2]
    print("A=UDV'")
    print("The Matrix A:")
    print(U @ D @ V)
    print("The U matrix:")
    print(U)
    print("The D matrix:")
    print(D)
    print("The V' Matrix:")
    print(V)
    
    
    
'''
In order to use matplotlib's ellipse plotter, we must know the 
counterclockwise rotation the ellipse does when transformed by the
matrix in question. I do this by finding the angle between u1 and e1
with the function rotation
''' 
  
def rotation(x,y):
    alpha = degrees(atan2(y,x))
    return (alpha + 360) % 360

'''
geoSVD plots the unit circle with V' vectors and the transformed ellipse with
U Vector as the major axes
'''
def geoSVD(matrix):
    decomp = SVD(matrix)
    U, D, V = decomp[0], decomp[1], decomp[2]
    plt.figure(1)
    ax = plt.subplot(121)
    ax.arrow(0, 0, V[0][0], V[0][1], color = "r", head_width = .1, length_includes_head= True)
    ax.arrow(0, 0, V[1][0], V[1][1], color = "blue", head_width = .1, length_includes_head= True)
    circ = plt.Circle((0,0),1, fill=False)
    ax.add_patch(circ)
    plt.axis('scaled')
    plt.title("Unit Circle with V' vectors")
    ax2 = plt.subplot(122)
    ellipse = Ellipse((0,0),2*D[0][0], 2*D[1][1], angle = (rotation(U[0][0],U[0][1])), fill = False)
    ax2.add_patch(ellipse)
    ax2.arrow(0, 0, D[0][0]*U[0][0], D[0][0]*U[0][1], color = "r", head_width = .1, length_includes_head= True)
    if D[1][1]==0:
        plt.axis("square")
    else: 
        ax2.arrow(0, 0, D[1][1]*U[1][0], D[1][1]*U[1][1], color = "blue", head_width = .1, length_includes_head= True)
        plt.axis('scaled')
    plt.title("Transformed Ellipse with U vectors")
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1, wspace=0.25)
    plt.show()
'''
geoSVD([[3,0],[0,-2]])

geoSVD([[2,0],[0,3]])

geoSVD([[0,2],[0,0],[0,0]])

geoSVD([[1,1],[0,0]])

geoSVD([[1,1],[1,1]])

showDecomp([[3,0],[0,-2]])

showDecomp([[2,0],[0,3]])

showDecomp([[0,2],[0,0],[0,0]])

showDecomp([[1,1],[0,0]])

showDecomp([[1,1],[1,1]])

geoSVD([[1,2],[0,2]])
'''