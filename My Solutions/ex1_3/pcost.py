portfolio = open(file="Data/portfolio.dat")

cost = 0
for stock in portfolio:
    data = stock.split()
    cost+=int(data[1])+float(data[2])
    
print(cost)