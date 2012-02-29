#!/usr/bin/python

weight = input("Enter weight: ")
bar = 45
plateWeight = [45, 35, 25, 10, 5, 2.5]
plates = []
q = 0
r = 0

weight = weight - bar
weight = float(weight) / 2

r = weight % plateWeight[len(plateWeight)-1]

for i in range(len(plateWeight)):
	if weight <= 0:
	    print "i'm going to break"
	    break
	elif weight % plateWeight[i]  == 0 and weight !=0:
		q = weight // plateWeight[i]
		weight = weight - plateWeight[i] * q
		plates.insert(i,q*2)
		print "this is weight %r this is i %r this is plateweight %r this is the quotient %r" % (weight, i, plateWeight[i], q)
		
	elif weight % plateWeight[i] != 0:
	    q = weight // plateWeight[i]
	    r = weight % plateWeight[i]
	    weight = r
	    plates.insert(i,q*2)
	print "weight is %r i is %r this is plateweight %r this is the quotient %r" % (weight, i, plateWeight[i], q)
        		
else:
	i = i +1 

for i in range(len(plates)):
 if plates[i] != 0:
   print "you will need %r %r lb plates" % (plates[i], plateWeight[i])
 else:
   i = i +1