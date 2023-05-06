# 导入必要的库
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# 生成一些示例数据
X = np.random.randn(100, 100)  # 假设每张图片是100x100的
y = np.zeros(100)  # 全部标记为正常图片（0）
y[10:20] = 1  # 标记10-19号图片为异常图片（1）

# 将数据分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 创建并训练模型
clf = svm.OneClassSVM(kernel='linear', nu=0.1)  # 使用线性核函数
clf.fit(X_train)

# 在测试集上进行预测
y_pred = clf.predict(X_test)

# 输出分类报告
print(classification_report(y_test, y_pred))
