start_time = time_ns()

function f(x,y)
  return 1+(2*x^2)+(3*y^2)
end

function gradient(x,y,delta=0.01,alpha=0.001)
  x_deriv = (f(x+delta,y)-f(x-delta,y))/(2*delta)
  y_deriv = (f(x,y+delta)-f(x,y-delta))/(2*delta)
  return [x-alpha*x_deriv,y-alpha*y_deriv]
end

point = [1,2]
for i in 1:2
  global point
  point = gradient(point[1],point[2])
end
global point
println("Julia Point - ",point)

final_time = time_ns()
println("Julia Time - ", (final_time - start_time)/1000000000)