from sympy import *

import math


x = Symbol('x')
#baraye vorudi gereftan  2 comment zir baid uncomment beshan va line 12 comment beshe

function = input("function: ")


#function = repr(x- sin(x))
print("f: " + function)
f = eval(function)


#graph("exp((-1)*x)", range(-5,5))



f_prime = f.diff(x)
print("\nf_prime: " + repr(f_prime)+ "\n")

ffprime = "x - ("+ function + ")/(" + repr(f_prime) +")"
###ffprime = "0.5*x + (1/x)"
print("equaftion: " + ffprime +"\n")

ffprime_eval = eval(ffprime)
f = lambdify(x,ffprime_eval)
firstn=float(input("X = "))
n=firstn
k = 1
roundround = 10
stored = []
print(str(k)+". f(",n,"):",f(n), "with "+str(roundround) + "decimal palces: ", round(f(n),roundround) )
stored.append(f(n))
#print(str(k)+". f(",n,"):",f(n), "with 6 decimal palces: ", f(n) )
n = f(n)
for i in range(15):
	k+=1
	print(str(k)+". f("+str(round(n,roundround))+"):",f(n), "with "+str(roundround) + " decimal palces: ", round(f(n),roundround) )
	#print(str(k)+". f("+str(f(n))+"):",f(n), "with 6 decimal palces: ", f(n) )
	n = f(n)
	if ( math.isnan(f(n)) or f(n)==0):
					break
	stored.append(n)
	n = round(n,roundround)

defrenceT = (stored[3]- stored[2])
abbc = (stored[3]- stored[2])/(stored[2]-stored[1])
print("defrence of 7 and 8	:",defrenceT)
print("abbc of them is",abbc)
#if (((defrenceT)<0.01) and (f(stored[8])>0.00001)):
if (True):
	print("m is needed.")
	m = round(1/(1-abbc),0)
	print("m is: ",m)
	
	Q = int(input("pls inter ur number:\n1.m*\n2.prime(m-1)\n"))
	if (Q==1):
		ffprime = "x - m*("+ function + ")/(" + repr(f_prime) +")"
		###ffprime = "0.5*x + (1/x)"
		print("equaftion: " + ffprime +"\n")
		ffprime_eval = eval(ffprime)
		f = lambdify(x,ffprime_eval)
		k = 1
		n=firstn
		print(str(k)+". f(",n,"):",f(n), "with "+str(roundround) + " decimal palces: ", round(f(n),roundround) )
		stored.append(f(n))
		#print(str(k)+". f(",n,"):",f(n), "with 6 decimal palces: ", f(n) )
		n = f(n)
		for i in range(15):
				k+=1
				print(str(k)+". f("+str(round(n,roundround))+"):",f(n), "with "+str(roundround) + " decimal palces: ", round(f(n),roundround) )
				#print(str(k)+". f("+str(f(n))+"):",f(n), "with 6 decimal palces: ", f(n) )
				n = f(n)
				if ( math.isnan(f(n)) or f(n)==0):
					break
				n = round(n,roundround)
				print("not more")
	if (Q==2):
		for i in range(int(m-1)):
			print("f"+str(i+1)+": " + function)
			f = eval(function)
			f_prime = f.diff(x)
			function = repr(f_prime)
			print("\nf_prime"+str(i+1)+": " + repr(f_prime)+ "\n")
		function = repr(f_prime)
		print("f: " + function)
		f = eval(function)
		f_prime = f.diff(x)
		print("\nf_prime: " + repr(f_prime)+ "\n")
		ffprime = "x - ("+ function + ")/(" + repr(f_prime) +")"
		print("equaftion: " + ffprime +"\n")

		ffprime_eval = eval(ffprime)
		f = lambdify(x,ffprime_eval)
		firstn=float(input("X = "))
		n=firstn
		k = 1
		roundround = 10
		stored = []
		print(str(k)+". f(",n,"):",f(n), "with "+str(roundround) + "decimal palces: ", round(f(n),roundround) )
		stored.append(f(n))
		#print(str(k)+". f(",n,"):",f(n), "with 6 decimal palces: ", f(n) )
		n = f(n)
		for i in range(15):
			k+=1
			print(str(k)+". f("+str(round(n,roundround))+"):",f(n), "with "+str(roundround) + " decimal palces: ", round(f(n),roundround) )
			#print(str(k)+". f("+str(f(n))+"):",f(n), "with 6 decimal palces: ", f(n) )
			n = f(n)
			if ( math.isnan(f(n)) or f(n)==0):
				break
			stored.append(n)
			n = round(n,roundround)





#x**4 - x - 10 

#exp(x**(-1)) - cos((math.pi)*x)

#x*ln(x**2)-2

#atan(x) - x**2 + 1