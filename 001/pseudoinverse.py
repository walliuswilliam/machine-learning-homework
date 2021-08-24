import numpy as np
import time

start_time = time.time()

y = [[0],[1],[4],[9]]
X = [[1,0],[1,1],[1,2],[1,3]]

y = np.matmul(np.transpose(X), y)
X_2 = np.matmul(np.transpose(X),X)

y_2 = np.matmul(np.linalg.inv(X_2), y)

final_time = time.time()
print(final_time - start_time)
