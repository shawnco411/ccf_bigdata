import csv
import codecs
import jieba
import jieba.analyse as analyse
import jieba.posseg as pseg
#读
with open("train.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    cnt=0

    stopwords = [line.strip() for line in open("unuse.txt", 'r').readlines()]
    for row in reader:
        text=pseg.cut(row[1])
        cnt = cnt + 1;
        print(cnt, '\n')
        final = ''
        if (row[3] == "0"):  # KEYWORLD
            final = ''
            for item in text:
                if item.flag != 'x':
                    final = final + item.word + '_' + item.flag + " "
            out = open("result/Neutral.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')
        elif (row[3] == "1"):  # KEYWORLD
            final = ''
            for item in text:
                if item.flag != 'x':
                    final = final + item.word + '_' + item.flag + " "
            out = open("result/Positive.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')
        elif (row[3] == "-1"):  # KEYWORLD
            final = ''
            for item in text:
                if item.flag != 'x':
                    final = final + item.word + '_' + item.flag + " "
            out = open("result/Negative.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')

with open("train.csv", "r", encoding="utf-8") as f:
    reader2 = csv.reader(f)
    cnt = 0
    for row in reader2:
        text=pseg.cut(row[1])
        cnt = cnt + 1;
        print(cnt, '\n')
        final = ''

        if(row[2]=="价格") :#KEYWORLD
            final = ''
            for item in text:
                if item.word not in stopwords:
                    if item.word != '\t':
                        if item.flag != 'x':
                            final = final + item.word + '_' + item.flag + " "
            out = open("result/priceF.txt", 'a', encoding="utf-8")#LOCATE
            out.write(final+'\n')
        elif (row[2] == "动力"):  # KEYWORLD
            final = ''
            for item in text:
                if item.word not in stopwords:
                    if item.word != '\t':
                        if item.flag != 'x':
                            final = final + item.word + '_' + item.flag + " "
            out = open("result/dongliF.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')
        elif (row[2] == "内饰"):  # KEYWORLD
            final = ''
            for item in text:
                if item.word not in stopwords:
                    if item.word != '\t':
                        if item.flag != 'x':
                            final = final + item.word + '_' + item.flag + " "
            out = open("result/neishiF.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')
        elif (row[2] == "配置"):  # KEYWORLD
            final = ''
            for item in text:
                if item.word not in stopwords:
                    if item.word != '\t':
                        if item.flag != 'x':
                            final = final + item.word + '_' + item.flag + " "
            out = open("result/peizhiF.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')
        elif (row[2] == "安全性"):  # KEYWORLD
            final = ''
            for item in text:
                if item.word not in stopwords:
                    if item.word != '\t':
                        if item.flag != 'x':
                            final = final + item.word + '_' + item.flag + " "
            out = open("result/anquanF.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')
        elif (row[2] == "外观"):  # KEYWORLD
            final = ''
            for item in text:
                if item.word not in stopwords:
                    if item.word != '\t':
                        if item.flag != 'x':
                            final = final + item.word + '_' + item.flag + " "
            out = open("result/waiguanF.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')
        elif (row[2] == "操控"):  # KEYWORLD
            final = ''
            for item in text:
                if item.word not in stopwords:
                    if item.word != '\t':
                        if item.flag != 'x':
                            final = final + item.word + '_' + item.flag + " "
            out = open("result/caokongF.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')
        elif (row[2] == "油耗"):  # KEYWORLD
            final = ''
            for item in text:
                if item.word not in stopwords:
                    if item.word != '\t':
                        if item.flag != 'x':
                            final = final + item.word + '_' + item.flag + " "
            out = open("result/youhaoF.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')
        elif (row[2] == "空间"):  # KEYWORLD
            final = ''
            for item in text:
                if item.word not in stopwords:
                    if item.word != '\t':
                        if item.flag != 'x':
                            final = final + item.word + '_' + item.flag + " "
            out = open("result/kongjianF.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')
        elif (row[2] == "舒适性"):  # KEYWORLD
            final = ''
            for item in text:
                if item.word not in stopwords:
                    if item.word != '\t':
                        if item.flag != 'x':
                            final = final + item.word + '_' + item.flag + " "
            out = open("result/shushiF.txt", 'a', encoding="utf-8")  # LOCATE
            out.write(final + '\n')

    print("DONE!!")


