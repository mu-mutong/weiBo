'''
@coding: #-*- coding: utf-8 -*-
@Descripttion: 
@version: 
@Author: mumu
@Date: 2019-09-29 09:26:31
@LastEditors: mumu
@LastEditTime: 2019-09-29 18:51:34
'''


import jieba
# 词频计算
import jieba.analyse as analyse
from wordcloud import WordCloud
from scipy.misc import imread
from os import path

# 构造一个keyword类，负责分词以及词云的生成

class keyWord():
     # 类构造函数中初试化参数
     def __init__(self):
         
          # 读取词云背景图片
          self.color_mask = imread("images/man.jpg") 
          self.cloud = WordCloud(
               # 设置字体，不指定就会出现乱码
               font_path="./fonts/Simfang.ttf",
               # font_path=path.join(d,'simsun.ttc'),
               width=200,
               height=200,
               # 设置背景色
               background_color='white',
               # 词云形状
               mask=self.color_mask,
               # 允许最大词汇
               max_words=2000,
               # 最大号字体
               max_font_size=110
          )
     # 分词，提取关键词
     def segmentation(self):
          comment_text = open('data/test.txt','rb').read()
          cut_text = " ".join(jieba.cut(comment_text))
          result = jieba.analyse.textrank(cut_text, topK=100, withWeight=True)
          # print(cut_text)
          # print(result)
          return  result
     # 画出词云图并保存
     def draw_wordcloud(self):
      # 生成关键词比重字典
          keywords = dict()
          result = self.segmentation()
          for i in result:
               keywords[i[0]] = i[1]
        
          # print (keywords)
    
          word_cloud = self.cloud.generate_from_frequencies(keywords)
          word_cloud.to_file("images/user_img.jpg") #保存图片

if __name__ == '__main__':
     kw = keyWord()
     kw.draw_wordcloud()
    