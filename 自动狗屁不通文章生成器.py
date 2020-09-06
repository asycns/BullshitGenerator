#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system
import random,readJSON

data = readJSON.读JSON文件("data.json")
名人名言 = data["famous"] # a 代表前面垫话，b代表后面垫话
前面垫话 = data["before"] # 在名人名言前面弄点废话
后面垫话 = data['after']  # 在名人名言后面弄点废话
废话 = data['bosh'] # 代表文章主要废话来源
synonyms = data['synonyms']
synonyms_keys = synonyms.keys()

punctuations = '＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､\u3000、〃〈〉《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏﹑﹔·！？｡。'
#xx = "学生会退会"

print('----------------------')
print(' Full shit Generator  ')
print('----------------------')
print('This script can helps you generate full mark shit on your screen. ')
print(' ')

重复度 = 2
required_rep = input('Input the amount of shit [2 by default]: ')
if required_rep.isdigit():
    重复度 = int(required_rep)

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素

下一句废话 = 洗牌遍历(废话)
下一句名人名言 = 洗牌遍历(名人名言)

def 来点名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "a",random.choice(前面垫话) )
    xx = xx.replace(  "b",random.choice(后面垫话) )
    return xx

def 另起一段():
    xx = "|。"
    xx += "\r\n"
    xx += "    |"
    return xx

if __name__ == "__main__":
    xx = input("请输入文章主题 [学生会退会 by default]：")
    
    xx = ("学生会退会" if xx == '' else xx.replace(' ', ''))    # Replace spaces
    
    # Users can generate full mark shit, or the original bull shit
    modified = input('Are you willing to generate full shit instead of bull shit? (Y)es/(N)o [No by default] ').lower()
    if modified == 'y' or modified == 'yes':
        modified = input('How much shit would you want to eat (0-9)? [2 by default] ')
        if modified.isdigit():
            modified = int(modified)
            if modified > 9:
                modified = 9
            elif modified < 0:
                modified = 0
        else:
            modified = 3
        modified += 1
    else:
        modified = 0

    tmp = '    |'
    for x in xx:
        while ( len(tmp) < 6000 ) :
            分支 = random.randint(0,100)
            if 分支 < 5:
                tmp = tmp[:-1]
                tmp += 另起一段()
            elif 分支 < 20 :
                tmp += 来点名人名言()
            else:
                tmp += next(下一句废话)
        # Keep the original

    tmp = tmp.split('|')
    tmp[-1] = '。'      # Forcely end the paragraph
    shit = ''
    if modified:
        junk_length = len(tmp)
        # Ignore punctuations and uncovered words
        ignore_list = [0] * junk_length
        # Count
        shit_count = 0
        for current_shit in range(len(tmp)):
            if tmp[current_shit] in punctuations or tmp[current_shit] not in synonyms_keys:
                ignore_list[current_shit] = 1
            else:
                shit_count += 1

        full_shit_length = round(shit_count * modified / 10)
        # Pollute ideal number of shit
        for count_shit in range(full_shit_length):
            while True:     # Trail exit when pollute well
                pollute_pos = random.randint(0, junk_length - 1)
                # Check it is need to ignore
                if ignore_list[pollute_pos]:
                    continue
                # Gather a full mark shit
                current_shit = tmp[pollute_pos]
                full_mark_pool = synonyms[current_shit]
                tmp[pollute_pos] = random.choice(full_mark_pool)
                ignore_list[pollute_pos] = 1
                break
            # Loop until enough shit be full marked

    for word in tmp:
        shit += word
    shit = shit.replace("x", xx)
    print(' ')
    print(xx)
    print('----------------------')
    print(shit)
    system('PAUSE')
