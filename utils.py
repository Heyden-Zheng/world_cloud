import PIL.Image as Image

# 将背景设为透明
# 从RGB（24位）模式转成RGBA（32位）模式
img = Image.open('image/mask1.png').convert('RGBA')
W, L = img.size
white_pixel = (0, 0, 0, 0)  # 白色
for h in range(W):
  for i in range(L):
    if img.getpixel((h, i)) == white_pixel:
      img.putpixel((h, i), (255, 255, 255, 0))   # 设置透明
img.save('image/mask1.png')  # 自己设置保存地址


