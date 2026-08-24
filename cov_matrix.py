

height = [1.70, 1.62, 1.52, 1.85, 1.91, 1.42]
weight = [72, 64, 84, 80, 72, 70]

height_mean = sum(height) / len(weight)
weight_mean = sum(weight) / len(weight)

height_var = 0
weight_var = 0

for i in range(len(height)):
  height_var = height_var + (height[i] - height_mean) ** 2
  weight_var = weight_var + (weight[i] - weight_mean) ** 2

height_var = height_var / ( len(height) - 1 )
weight_var = weight_var / ( len(weight) - 1 )

covariance = 0

for i in range(len(height)):
  covariance = covariance + (height[i] - height_mean) * (weight[i] - weight_mean)
covariance = covariance / ( len(height) -1 )

cov_matrix = [
  [height_var, covariance],
  [covariance, weight_var]
]
print (cov_matrix)
