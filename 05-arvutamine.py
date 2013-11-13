import math
print
a = 10.0
b = -1.0
c = 0.0
d = 0.0
print
r =c/(3.0*a)
print "r = {}".format(r)

p=-b/(3.0*a)
print "p = {}".format(p)

q=p**3.0+(b*c)-(3.0*a*d)/(6.0*a**2.0)
print "q = {}".format(q)
print

x = (q+(q**2.0+(r-p**2.0)**3.0)**(1.0/2.0))**(1.0/3.0) \
+ (q-(q**2.0+(r-p**2.0)**3.0)**(1.0/2.0))**(1.0/3.0) \
+p


print "x = {}".format(x)

