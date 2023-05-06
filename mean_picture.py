import numpy as np
from PIL import Image

# 展示原始图像和均值图像
from matplotlib import pyplot as plt

# 读取图像
img = Image.open("D:\AI\Image_Quality\opencv-practical-exercise-master\ITEM 30-39\ITEM37 OpenCV_BRISQUE\images\compressed-heavy.jpg")

# 将图像转换为NumPy数组
img_array = np.array(img)

# 计算图像块均值
block_size = 3
kernel = np.ones((block_size, block_size)) / (block_size ** 2)
img_avg = np.zeros_like(img_array)
for i in range(img_array.shape[0] - block_size + 1):
    for j in range(img_array.shape[1] - block_size + 1):
        img_avg[i:i+block_size, j:j+block_size] = np.sum(img_array[i:i+block_size, j:j+block_size] * kernel, axis=(2), keepdims=True)

# 将均值图像转换为PIL图像并保存
# img_avg = Image.fromarray(np.uint8(img_avg))
# img_avg.save("image_avg.jpg")


fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(img)
axs[0].set_title('Original Image')
axs[1].imshow(img_avg)
axs[1].set_title('Average Image')
plt.show()
