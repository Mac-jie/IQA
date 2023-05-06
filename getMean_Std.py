import numpy as np
import cv2

# 读取图像
img = cv2.imread('D:\AI\Image_Quality\opencv-practical-exercise-master\ITEM 30-39\ITEM37 OpenCV_BRISQUE\images\compressed-heavy.jpg')

# 定义局部均值和方差计算函数
def local_stats(img_array, block_size):
    # 初始化均值和方差图像数组
    img_avg = np.zeros_like(img_array, dtype=np.float32)
    img_var = np.zeros_like(img_array, dtype=np.float32)
    # 迭代图像数组中所有的块
    for i in range(0, img_array.shape[0]-block_size+1, block_size):
        for j in range(0, img_array.shape[1]-block_size+1, block_size):
            # 计算当前块的均值和方差，并将其赋值给均值和方差图像数组中的相应位置
            block = img_array[i:i+block_size, j:j+block_size, :]
            mean, std = cv2.meanStdDev(block)
            img_avg[i:i+block_size, j:j+block_size, :] = mean
            img_var[i:i+block_size, j:j+block_size, :] = std
    return img_avg, img_var

# 计算局部均值和方差
img_avg, img_var = local_stats(img, 3)

# 显示原图、均值图像和方差图像
cv2.imshow('Original Image', img)
cv2.imshow('Local Mean Image', img_avg.astype(np.uint8))
cv2.imshow('Local Variance Image', img_var.astype(np.uint8))
cv2.waitKey(0)

# # 保存均值图像和方差图像
# cv2.imwrite('local_mean_image.jpg', img_avg.astype(np.uint8))
# cv2.imwrite('local_variance_image.jpg', img_var.astype(np.uint8))
