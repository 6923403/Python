import cv2
import wordcloud
import jieba

mk = cv2.imread('N:\\codes\\Python\\generator\\20200530135116.png')
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        mask=mk,
                        #font_path='msyh.ttc
                        font_path='C:/Windows/Fonts/simkai.ttf')

f = open('N:\\codes\\Python\\generator\\a3111.txt', encoding='utf-8')
txt = f.read()
txt_list = jieba.lcut(txt)
string = "".join(txt_list)
w.generate(string)
w.to_file('N:\\codes\\Python\\generator\\aaa.png')
f.close()

m_color = cv2.imread('N:\codes\Python\generator\Color Hunt Palette 189889.png')
image_color = wordcloud.ImageColorGenerator(m_color)
wc_color = w.recolor(color_func=image_color)
wc_color.to_file('N:\\codes\\Python\\generator\\aaa.png')

img = cv2.imread("N:\\codes\\Python\\generator\\aaa.png")
cv2.imshow("", img)
cv2.waitKey(0) 