# ----------------------------------------------
# build an optimization solver having contraints
# ----------------------------------------------
from scipy.optimize import minimize

def objective(x):
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    return(x1*x4*(x1+x2+x3)+x3)
    
# constraint1 ... x1 * x2 * x3 * x4 >= 25
def constraint1(x):
    return(x[0]*x[1]*x[2]*x[3]-25.0)
    
# constraint2 ... x1^2 + x2^2 + x3^2 + x4^2 = 40
def constraint2(x):
    sum_sq = 40
    for i in range(4):
        sum_sq = sum_sq - x[i]**2
    return sum_sq

# ------------
# setup model  
x0 = [1,5,5,1]
print(objective(x0))

# build bounds and contraints
b = (1.0,5.0)
bounds = (b,b,b,b)
con1   = {'type': 'ineq', 'fun': constraint1}
con2   = {'type': 'ineq', 'fun': constraint2}
cons   = (con1, con2)

# run the model
so1 = minimize(objective, x0, method='SLSQP', bounds = bounds, constraints = cons)
print(so1)


# ----------------------------------------------
# build an optimization solver having distances
# ----------------------------------------------
import tsp # traveling salesman problem
from scipy.spatial import distance

# coordinates
t = tsp.tsp([(0,0),(0,1),(1,0),(1,1)])

# if want to calculate the euclidean distance
distance.euclidean((0,1),(2,1))

# matrix of distances between all of the coordinates
dist_matrix = [[0,   1,   1, 1.5],
               [1,   0, 1.5,   1],
               [1, 1.5,   0,   1],
               [1.5, 1,   1,   0]]

r = range(len(dist_matrix))

# build array of coordinates and distances
dist = {(i,j): dist_matrix[i][j] for i in r for j in r}
print(tsp.tsp(r, dist))


