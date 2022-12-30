brasil = 100000
tcb = 2.7/100
argentina = 250000
tca = 1.3/100

anos = 0

while brasil <= argentina:
    brasil += brasil * tcb
    argentina += argentina * tca
    anos += 1
print(f'Para que o Brasil ultrapasse ou iguale a população da Argentina, é necessário {anos} anos!')
