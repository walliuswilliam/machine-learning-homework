import time

start_time = time.time()

def function(x,y):
  return 1+(2*x**2)+(3*y**2)

def gradient(x,y,delta=0.01,alpha=0.001):
  x_deriv = (function(x+delta,y)-(function(x-delta,y)))/(2*delta)
  y_deriv = (function(x,y+delta)-(function(x,y-delta)))/(2*delta)
  return [x-alpha*x_deriv,y-alpha*y_deriv]


point = [1,2]
for num in range(2):
  point = gradient(point[0],point[1])
  print("Python {} Point -".format(num+1), point)


final_time = time.time()
print("Python Time -", final_time - start_time)
