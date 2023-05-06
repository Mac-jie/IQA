import cv2
import numpy as np

# 读入图像
img = cv2.imread('D:\AI\Image_Quality\opencv-practical-exercise-master\ITEM 30-39\ITEM37 OpenCV_BRISQUE\images\compressed-heavy.jpg')

# 定义块大小
block_size = 3

# 转换为浮点型数组
img_array = np.float32(img)

# 计算均值和方差
mean, std = cv2.meanStdDev(img_array)

# 对图像进行均值和方差归一化
# img_array = (img_array - mean) / (std + 1)

# 遍历图像，计算局部均值和方差，并用原图减去均值除以（方差+1）
for i in range(0, img_array.shape[0]-block_size+1, block_size):
    for j in range(0, img_array.shape[1]-block_size+1, block_size):
        block = img_array[i:i+block_size, j:j+block_size]
        block_mean, block_std = cv2.meanStdDev(block)
        img_array[i:i+block_size, j:j+block_size] = (block - block_mean) / (block_std + 1)

# 将浮点型数组转换为整型数组
img_array = np.uint8(img_array)

# 显示图像
cv2.imshow('Image', img_array)
cv2.waitKey(0)
cv2.destroyAllWindows()
