from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np


# 创建一个示例数据集
data = np.array([[1.0, 2.0, 3.0],
                 [4.0, 5.0, 6.0],
                 [7.0, 8.0, 9.0]])

# 创建MinMaxScaler对象
scaler = StandardScaler()

# 使用fit_transform对数据进行归一化
normalized_data = scaler.fit_transform(data)

# 输出归一化后的数据
print("Normalized Data:")
print(normalized_data)
