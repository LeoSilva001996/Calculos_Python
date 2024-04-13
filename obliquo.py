import math 
def Alcance(v0,theta,g):
    return (v0**2/g)*math.sin(2*theta*math.pi/180)
v0 = 300
theta = [15, 30, 45, 60, 75]
n = len(theta)
A =[]
for i in range(len(theta)):
    A.append(Alcance(v0,theta[i],10))
print(A)