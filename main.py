# 思路：
# 1.读取文件，分词整理；
# 2.配置对象参数，加载词云文本；
# 3.计算词频，输出词云文件


import jieba
import numpy as np
import wordcloud
import collections  # 词频统计库
from matplotlib import colors

# 1.读取文本
from PIL import Image

# with open('data/yunjiaoshi.txt', encoding='utf-8') as f:
with open('data/席慕容诗集.txt', encoding='utf-8') as f:
    txt = f.read()

stop_words = []  # 创建停词空列表

# 读取停词表
with open("data/stopwords.txt", 'r', encoding='utf-8') as f:
    for line in f:
        if len(line) > 0:
            stop_words.append(line.strip())  # 把停词追加到stop_words列表中

raw_word_list = jieba.cut(txt, cut_all=False)  # 生成分词列表，精确分词

# remove停词，获取需要的词
word_list = [i for i in raw_word_list if i not in stop_words]

# 词频统计
word_counts = collections.Counter(word_list)  # 对分词做词频统计
word_counts_top = word_counts.most_common(20)  # 获取前number个最高频的词
print('word_counts:', word_counts)
print('word_counts_top:', word_counts_top)

word_string = ' '.join(word_list).replace('\n', '')  # 连成字符串，replace表示将换行符替换为空
print(word_string)

# 词云底片
# image_mask1 = np.array(Image.open('image/mask.png'))

#  建立颜色数组，可更改颜色（孟菲斯色系）
color_list = ['#00B254', '#003D85', '#F8DD00', '#060608', '#D5A296',
              '#1D2E6A', '#8B3724', '#CB7E36', '#5099D0']

# 调用
colormap = colors.ListedColormap(color_list)

# msyh.ttc是电脑本地字体，可以写绝对路径
word_cloud = wordcloud.WordCloud(
    font_path='STXINGKA.TTF',  # 设置字体
    width=1920,
    height=1080,
    colormap=colormap,  # 设置文字颜色
    max_font_size=200,  # 设置字体最大值
    background_color='white',  # 背景色
    max_words=20000,  # 最多可显示的字数
    # mask=image_mask1,  # 设置背景图片
)
word_cloud.generate(word_string)  # 加载词云文本
# word_cloud.to_file('韵脚诗词云.png')  # 保存词云文件
word_cloud.to_file('席慕容诗集词云.png')  # 保存词云文件


