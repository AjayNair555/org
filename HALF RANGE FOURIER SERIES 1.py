from sympy import*
x,n=symbols('x,n')
L=pi
f=lambda x: x
print("Given Function f(x): ", f(x))
a0=integrate(f(x),[x,0,L])*2/L
f_series=a0/2
for n in range(1,6):
    an=integrate(f(x)*cos(n*pi*x/L),[x,0,L])*2/L
    f_series=f_series+an*cos(n*pi*x/L)
print("The required cosine series: ")
pprint(f_series)
plot(f_series,f(x),(x,-2*L),legend=True)
    
