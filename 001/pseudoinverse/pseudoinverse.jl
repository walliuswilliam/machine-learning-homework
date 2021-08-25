start_time = time_ns()

y = [0; 1; 4; 9]
X = [1 0; 1 1; 1 2; 1 3]

y_2 = transpose(X)*y
X_2 = transpose(X)*X

y_3 = inv(X_2)*y_2

final_time = time_ns()
println("Julia Time - ", (final_time - start_time)/1000000000)
