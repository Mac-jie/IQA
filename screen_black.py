import os
from PIL import Image

# 设置阈值，表示颜色值小于该阈值的像素点将被视为黑色
threshold = 10

# 设置文件夹路径
src_folder = 'E:\HSR\IQA\Black'

dst_folder = 'E:\\HSR\\IQA\\Black\\folder'


# 初始化计数器
total_black = 0
total_non_black = 0

# 遍历文件夹中的所有文件
for filename in os.listdir(src_folder):
    file_path = os.path.join(src_folder, filename)
    if os.path.isfile(file_path):
        try:
            # 读取图片并转换为灰度图
            img = Image.open(file_path).convert('L')
            # 统计颜色值小于阈值的像素点数量
            black_pixels = sum(1 for pixel in img.getdata() if pixel < threshold)
            # 如果黑色像素点数量超过总像素点数量的一半，则将该图片输出
            if black_pixels > (img.width * img.height) * 0.98:
                print(file_path)
                os.rename(os.path.join(src_folder, filename), os.path.join(dst_folder, filename))
                total_black += 1
            else:
                total_non_black += 1


        except Exception as e:
            print(f"Error: {e}")

# 输出统计结果
print(f"移动了 {total_black} 张全黑的图片到 {dst_folder}")
print(f"剩余 {total_non_black} 张不是全黑的图片")