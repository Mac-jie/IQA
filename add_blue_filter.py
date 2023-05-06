from PIL import Image, ImageFilter

# 打开图像文件
image = Image.open("example.jpg")

# 添加滤镜
blue_filter = Image.new("RGBA", image.size, (135, 206, 250, 100))
result = Image.alpha_composite(image.convert("RGBA"), blue_filter)

# 显示结果
result.show()

# 保存结果
result.save("example_filtered.jpg")
