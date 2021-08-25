import time

start_time = time.time()

for i in range(10):
  total = 0
  for num in range(1000001):
    total += num

final_time = time.time()
print('Python Time -', final_time - start_time)
