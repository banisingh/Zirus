from numpy import array, dot, sum, power
from numpy.linalg import norm
from random import random
import numpy as np


numQ = 2
#people = [ [ int(random()*10+1) for y in range(numQ) ] for i in range(30) ] # Create a dummy set
#testPerson = [ int(random()*10+1) for i in range(numQ) ]
#r = [  int(random()*10+1) for y in range(numQ) ] #Review left by the people

weights = [ int(random()*10+1) for i in range(numQ) ] #ADD THE VALUES INTO THE BRACKETS
people = []

l_r = 150 #Hardness to learn. The greater, the more data needed and slower to train, but the more accurate.


weights = weights / norm(weights)


def sumD(d,w,n=1,p=2):
	dists = []
	d = array(d)
	w = array(w)
	for v in people:
		for i in range(len(v)):
			dists.append( w[i]*(v[i]-d[i])**p )
	dist = sum(dists)**(1/p)
	return dist
	



def just_train(data,r, p=2, n=1  ): #For now, N will only work for 1. Do not change n=1. data.shape = ( 1,numQ ), r.shape(1,numQ)
	global weights
	if n!=1: return
	for iii in range(2):
		error = (array(r)-5)/l_r
		weights = array(weights, dtype="float64")
		data = array(data, dtype="float64")
		delta = error * (weights/p)*sumD(data, weights)**((1-p)/p)
		weights += dot( data.T, delta )
	weights = weights / norm(weights)

def dist(d, w,n=1, p=2, ignore=False): #P1 len should be the # of questions length. Vector size [1,Q]. d is the data, n is the # of nearest people to return. len(w) must equal len(d)
	dists = []
	for v in people:
		#The formula is distance = ( x1^p + x2 ^ p +...+x20 ^ p )^(1/p)
		dist = abs(sum(w*power((array(v) - array(d)), p) ) ** (1/p) )
		dists.append(dist)
	#Now go over the list and find the n smallest values
	md = 99999999999
	mp = -1
	mind = []
	minp = []
	for t in range(n):
		for i, dist in enumerate(dists):
			if not ignore and ignore == i: continue
			if dist < md:
				md = dist
				mp = i
		del dists[mp]
		mind.append(md)
		minp.append(mp)
		md = 9999999999
		mp = -1
	return mind, minp

                                ##Better not to touch or call what's above outside of the AI    

                                ##Underneath is API, usable code. Take care for the warnings in comments.
		
def add_train(data, r, p=2):# Data should be a [1,# of Questions]. r shape should be [1,numQ]
	try:
		just_train(data, r)
		people.add(data)
	except Exception as e:
		print("Awww man, couldn't get that")
	return
    

def matchAll(p=2,n=1): #Doesn't need parameteres. I recomment just calling matchAll(). Returns a [1,len(people)] matrix, which gives 1
	ret = []
	for i,v in enumerate(people):
		ret.append(dist(v, ignore=i, n=n))
	return ret

def getPeople():
        return people


















    













