from PIL import Image
import os

# 原始图片文件夹和目标文件夹
src_folder = 'E:\\HSR\\IQA\\Black'
dst_folder = 'E:\\HSR\\IQA\\Black\\folder'

# 设置像素阈值，即当像素值小于该值时，认为该像素为黑色
threshold = 10

# 初始化计数器
total_black = 0
total_non_black = 0

# 遍历文件夹中的所有图片
for filename in os.listdir(src_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 打开图片并计算像素值
        img = Image.open(os.path.join(src_folder, filename))
        pixels = list(img.getdata())
        num_black = sum([1 for p in pixels if sum(p) < threshold])

        # 判断是否为全黑的图片，如果是则移动到目标文件夹
        if num_black == len(pixels):
            os.rename(os.path.join(src_folder, filename), os.path.join(dst_folder, filename))
            total_black += 1
        else:
            total_non_black += 1

# 输出统计结果
print(f"移动了 {total_black} 张全黑的图片到 {dst_folder}")
print(f"剩余 {total_non_black} 张不是全黑的图片")
