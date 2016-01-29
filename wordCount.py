# get all the words of a webpage, count the frequency of each word

import requests  # download a webpage
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []   # a blank list
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "lxml")
    for post_text in soup.find('div', {'class': 'details'}).findAll('p'):  #content =  post_text.string  //get all the text between the tag
        content = post_text.string
        if content is not None:
            words = content.lower().split()   #lower()//全小写
            for each_word in words: # words is a list
                word_list.append(each_word)

    clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+{}:\"-<>?;,.'[]-='"  # to escape all of these characters
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_word_list.append(word)   #:) 删掉后剩下空字符串
    create_dictionary(clean_word_list)

# creating a dictionary

def create_dictionary(list):
    word_count = {}
    for word in list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):   #itemgetter(0) sorting item by key
        print(key, value)

start("http://www.newtimes.co.rw/section/article/2016-01-28/196537/")