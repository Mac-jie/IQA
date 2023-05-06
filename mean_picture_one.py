import cv2
import numpy as np

# 随机初始化一张图像
img = np.random.randint(0, 256, size=(3, 3, 3), dtype=np.uint8)

# 将图像转换为浮点型数据类型
img_float = np.float32(img)

# 定义均值滤波器的卷积核
kernel = np.ones((3, 3), np.float32) / 9

# 对图像进行卷积运算，得到每个3x3块的均值
img_avg = np.zeros_like(img_float)
block_size = 3
height, width, channels = img_float.shape

for i in range(height - block_size + 1):
    for j in range(width - block_size + 1):
        img_float_temp = img_float[i:i + block_size, j:j + block_size][:, :, :1]
        sum_temp = np.sum(img_float_temp)
        img_avg[i:i + block_size, j:j + block_size] = np.sum(img_float[i:i + block_size, j:j + block_size], axis=(0, 1))

# 将均值图像转换为8位无符号整数数据类型
img_avg = np.uint8(img_avg)

# 显示原图和均值图像
cv2.imshow('Original Image', img)
cv2.imshow('Average Filtered Image', img_avg)

# 保存均值图像到本地
cv2.imwrite('average_filtered_image.jpg', img_avg)

# 等待用户按下任意按键后关闭窗口
cv2.waitKey(0)
cv2.destroyAllWindows()
