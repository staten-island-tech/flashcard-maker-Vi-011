
P = 10
N = 2
R = 1
total_infected = N
new_infected = N
D = 0
while total_infected < P:
    new_infected*= R
    total_infected += new_infected
    D += 1 
print (f"The number of people being infected is {total_infected} in day {D}")
