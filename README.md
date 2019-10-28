# ccf_bigdata<img src="https://github.com/shawnco411/Data_Structure/blob/master/shawnco4111.png" width="6%" align="right">
汽车行业用户观点主题及情感识别训练集分词程序
## 项目背景
该项目为2018 CCF大数据与计算智能大赛中汽车行业用户观点主题及情感识别赛题的数据集分词程序，能够对数据集根据主题和情感进行分词，并将分词结果及其词性输出到各自的txt文件中。
## 文件说明
`\venv`目录下:

|----`【词性名对照表】.txt`为词性缩写的对照表<br/>
|----`test.py`为数据集分词程序<br/>
|----`train.csv`为训练集文件<br/>
|----`\result`为输出处理结果的文件夹<br/>
|------------`Neutral.txt`为中立文本的分词结果<br/>
|------------`Positive.txt`为正向文本的分词结果<br/>
|------------`Negative.txt`为负向文本的分词结果<br/>
|------------`其余txt文件`为针对不同主题的分词结果<br/>
|----`unuse.txt`为停用词表，用于过滤掉无实义的词<br/>

## 运行说明
训练集`train.csv`文件格式如下（总计包含9948条该内容）：

数据ID  | 文本内容| 主题| 情感分析| 情感词
------------- | -------------| -------------| -------------| -------------
r1WHgbI0ZKqMdELy  | 恭喜恭喜，这个优惠不错哦！ | 价格 | 1 | 优惠不错 

> 训练集数据中主题被分为10类，包括：动力、价格、内饰、配置、安全性、外观、操控、油耗、空间、舒适性。
>
>情感分为3类，分别用数字0、1、-1表示中立、正向、负向。
>
>content_id与content一一对应，但同一条content中可能会包含多个主题，此时出现多条记录标注不同的主题及情感，因此在整个训练集中content_id存在重复值。
>
>仅小部分训练数据包含有情感词sentiment_word，大部分为空。

该程序对同目录下的数据集文件`train.csv`进行处理，对数据集根据主题和情感进行分词，并将分词结果及其词性输出到`venv\result`下的txt文件中，处理完成时控制台会输出"done！"。

此项目中的`vene\result`中已有分词结果文件，若再次运行，需要将分词结果清空，否则处理结果会追加到原文件的末尾。

## 运行环境
PyCharm 2018.2.1 (Community Edition)

Build #PC-182.3911.33, built on August 5, 2018

JRE: 1.8.0_152-release-1248-b8 amd64

JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o

Windows 10 10.0
## 第三方库
[THULAC](http://thulac.thunlp.org/ "THULAC")

[jieba](https://github.com/fxsjy/jieba "jieba")

## 开源协议

[GNU General Public License v3.0](LICENSE)
