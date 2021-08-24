start_time = time_ns()

for i in 1:10
  total = 0
  for num in 1:1000000
    total += num
  end
end  

final_time = time_ns()
println((final_time - start_time)/1000000000)
