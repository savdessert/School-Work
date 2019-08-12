# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:11:11 2019
Analyze the effect of matrix size on spectral radius, norm, minimum singular values and eigenvalues of 100 matrices when superimposed 
Question 12.3 in Numerical Linear Algebra by Trefethen
"""

import numpy as np
import matplotlib.pyplot as plt


def randomMatrix(dim, n=100):
    specradius = [0]*n #initialize vectors to hold data
    norms = [0]*n
    minsing = [0]*n
    sdt = dim**-.5 
    X = np.linspace(-1,1, dim)
    for x in range(n):
        M = np.random.normal(scale = sdt, size = (dim,dim))
        eigv = np.linalg.eig(M) #using built in functions, extract data from matrices
        plt.scatter(eigv[0], X)
        u, d, v = np.linalg.svd(M)
        specradius[x] =( max(abs(eigv[0])))
        norms[x] = np.linalg.norm(M, ord = 2)
        minsing[x] = min(d)
    minsing.sort()
    j= 10
    value = [2**-x for x in range(1,j+1)]
    prob = [0]*j
    for x in range(j):
        count = 0
        for i in range(n):
            if minsing[i] <= value[x]:
                count += 1
        prob[x] = count/n
                
    plt.plot([sdt,sdt],[-1,1], color = "black")
    plt.plot([-sdt,-sdt],[-1,1],color = "black")
    plt.plot([2*sdt,2*sdt],[-1,1], color = "black")
    plt.plot([-2*sdt,-2*sdt],[-1,1], color = "black")
    plt.plot([3*sdt,3*sdt],[-1,1],color = "black")
    plt.plot([-3*sdt,-3*sdt],[-1,1], color = "black") 
    plt.title("Superimposed Eigenvalues of {} {}x{} Matrices".format(n, dim, dim))
    plt.show()
    X2 = np.linspace(-1,1,n)
    plt.scatter(X2,specradius)
    A = np.ones((n,2))
    B = np.transpose(specradius)
    Y = A@np.linalg.lstsq(A,B, rcond=None)[0]
    plt.plot(X2,Y)
    plt.title("Superimposed p(A) for {} Matrices of Dimension {}".format(n,dim))
    plt.show()
    plt.scatter(X2, norms)
    B = np.transpose(norms)
    Y = A@np.linalg.lstsq(A,B, rcond = None)[0]
    plt.plot(X2,Y)
    plt.title("Superimposed norm(A) for {} Matrices of Dimension {}".format(n,dim))
    plt.show()
    values = ['1/2', '1/4', '1/8', '1/16', '1/32', '1/64', '1/128', '1/256', '1/512', '1/1024']
    plt.bar(values, prob)
    plt.title("Probability of minimal singular value for {} {}x{} Matrices".format(n, dim, dim))
    plt.ylabel("Probability")
    plt.xlabel("X values")
    plt.tight_layout()
    plt.show()
       
randomMatrix(8)
randomMatrix(16)
randomMatrix(32)
randomMatrix(64)
randomMatrix(128)
randomMatrix(256)
randomMatrix(512)

