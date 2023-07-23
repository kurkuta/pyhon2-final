import numpy as np
a = np.random.randint(0,100,50)
b = np.random.randint(0,100,50)
print("sum:",a+b)
print("substract:",a-b)
print("multiply:",a*b)
print("divide:",a/b)
print("concatenate:",np.concatenate((a,b)))
print("resize:",np.resize(np.concatenate((a,b)),(5,10)))