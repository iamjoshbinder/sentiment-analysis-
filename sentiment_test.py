





l1 = ['Salmon','Herring','Cod','Mackerel','Lobster']
l2 = ['Krill','Phytoplankton','Whiting','Copepods','Starfish']
def func_1(l1,l2):
    dic = dict()# create a empty dict
    assert len(l1) == len(l2)#assert two list length equal
    for i in range(len(l1)): 
        dic[l1[i]] = l2[i]#update dic with key from l1 and value from l2
    return dic
print 'question_1: ',func_1(l1,l2)#test func_1


dic = func_1(l1, l2)
d1 = {'Salmon':6,'Herring': 12,'Cod': 18,'Mackerel': 6,'Lobster': 48}
def func_2(dic,d1):
    tuple_dic = dict()
    for key in dic.keys():
        tuple_dic[key] = (dic[key],d1[key])
    return tuple_dic
print 'question 2: ',func_2(dic,d1)

 
def func_3(filename,s):
    with open(filename,'r') as f:#open file
        text = f.read()#read file into text
        if s in text:#if string s in text
            return True
        else:
            return False
#test func_3
filename = 'test3.txt'
s='world'
print 'question 3 : the string ({}) is in the file ({})? {}'.format(s,filename,func_3(filename, s))


from bs4 import BeautifulSoup
import urllib
from textblob.blob import TextBlob
testsite = 'https://blogs.dal.ca/sim/feed/'
def find_recent(site):
    '''takes a URL as an argument, visits that URL, parses the
    XML blog feed within it and returns the contents of the
    first <pubDate> tag on the page'''
    html = urllib.urlopen(site).read().decode('utf-8')#open site with function urlopen and return page content to html
    soup = BeautifulSoup(html,"html.parser")#create a BeautifulSoup instance with html
    return soup.item.pubdate.get_text()#visit pubdate tag ,note that pubdate is the children tag of item tag
#test find_recent function
print 'question 4 : ',find_recent(testsite)    




#Correlation between length/polarity: r = [BLANK], p = [BLANK]
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
def func_5(filename):
    length =[]#length list
    polarities = []#polarity list
    with open(filename,'r') as f:#open file
        for line in f.readlines():#read file line by line
            text = line.split('\t')[-1]#split line with tab,the last one in splited list is text
            length.append(len(text))#calculate length of text and append it to length list
            polarities.append(TextBlob(text).sentiment.polarity)#get text polarity and append it to polarities list
    plt.scatter(length,polarities,c='g') #scatterplot length and polarities,color is green      
    plt.title('sentiment&length')#title
    plt.xlabel('length')#xlabel
    plt.ylabel('sentiment')#ylabel
    length = np.array(length)#transpose list to array
    polarities = np.array(polarities)
    pearson = np.corrcoef(length,polarities)#calculate pearson's correlation
    print 'question 5:'
    print 'Correlation between length/polarity: r = {}, p = {}'.format(pearson[0],pearson[1])#format print
    plt.savefig('sentiment&length.png')
    plt.show()    
#test func_5
func_5('texts.txt')           
            
            
            

