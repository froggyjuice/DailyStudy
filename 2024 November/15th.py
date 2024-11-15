import numpy as np

data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

rows = np.array([0, 2, 1])  # 행 인덱스
cols = np.array([1, 0, 2])  # 열 인덱스

result = data[rows, cols]
print(result)
