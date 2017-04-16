'''
There are a variety of "questions" in this midterm. Each asks for some 
Python code that accomplishes a task. You are free to look to the internet
or other sources to try and answer these questions. It is an open book exam.
That said, it is to be done individually. You should not consult with your peers
or share your answers with your peers. 

Marks will be allocated both based on whether the code accomplishes the
desired tasks, and also on the code's clarity. Please comment the code
thoroughly, so that if you were to share your script with someone, they could
walk through it and understand what each section is doing.

Using sensible/logical variable names is highly advised.
'''



#1. (3 points) Write a function that takes two lists as arguments
#assume the lists are structured similarly to l1 and l2 below
#your function should return a dictionary that uses the elements of l1
#as keys, and the elements of l2 as values. The lists correspond to one another,
#so the first item in l1 should be the key to the first item in l2 as the value.
#be sure to write your function so it will do this with ANY two similar lists

l1 = ['Salmon','Herring','Cod','Mackerel','Lobster']
l2 = ['Krill','Phytoplankton','Whiting','Copepods','Starfish']
def func_1(l1,l2):
    dic = dict()# create a empty dict
    assert len(l1) == len(l2)#assert two list length equal
    for i in range(len(l1)): 
        dic[l1[i]] = l2[i]#update dic with key from l1 and value from l2
    return dic
print 'question_1: ',func_1(l1,l2)#test func_1

#2. (3 points) Write a function that will take TWO arguments,
#one will be a dictionary structured like that created in question 1 above
#the other will be a dictionary structured like d1 below
#note that both dictionaries have identical keys, this will always
#be the case for the dictionaries that this function works on.

#Your function should take both dictionaries and return a third dictionary
#the third dictionary should have the same keys as the input dictionaries
#but the values should be tuples, containing both values from the input
#dictionaries, e.g. {'Salmon':('Krill',6)} [but with all the keys/values]
dic = func_1(l1, l2)
d1 = {'Salmon':6,'Herring': 12,'Cod': 18,'Mackerel': 6,'Lobster': 48}
def func_2(dic,d1):
    tuple_dic = dict()
    for key in dic.keys():
        tuple_dic[key] = (dic[key],d1[key])
    return tuple_dic
print 'question 2: ',func_2(dic,d1)
#3. (5 points) Write a/some function(s)that will take two arguments. The first should be
#a filename, and the second should be a string. 
#the function shold open that file and parse it, returning True if
#the file contains the string provided as argument two, and False if not.
#The file will be a plaintext file. 
#Hint, you may want to make a test file with notepad or similar that you
#can try your function with.
 
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

#4. (7 points) Write a function that will visit a Blog feed and return the publication
#date of the most recent post. Your function should be modeled on (and tested
#for) a site structured like the testsite below.

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
#5. (7 points) Write a function that will parse a file structured like the the texts.txt 
#file provided. This file contains two tab-separated columns
#the first column is an ID number, and the next column contains the 
#associated text.

#your function should parse the file, extract JUST the text (i.e. not the id #).
#your function should take that text and calculate its length in characters
#and its sentiment value (use textblob for this). 

#You should then take all of those pairs of values
#and make a scatterplot of them, with text length on the x-axis and 
#sentiment on the y-axis.

#in addition to the scatterplot, which should be uploaded as an image along
#wth your completed script, also calculate and report the pearson's 
#correlation for the two vectors of values (length & polarity).
#include both the code to do the calculation, and the results in a comment



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
            
            
            

