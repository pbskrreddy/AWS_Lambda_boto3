print '\n'
print "***** Starting Problem 1 ********"

my_words = ['Python', 'ok', 'selenium', 'integer', 'java', 'loop', 'webdriver', 'yes', 'Interactive']

for i in my_words:
    if i >= 5:
        print 'my_words is %s' % my_words

double = lambda x: x * 2
def double(x):
	return x * 2


import boto3

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

response = client.describe_tags(Filters={'Key': '', 'Value': ''})
print(response)

import pandas as pd
import re  # regular expersion
from tabulate import tabulate
with open("C:/Users/pbskr/Desktop/sample_log.bin") as file: # Use file to refer to the file object
   data = file.readlines()
# print (data)
lList = []
for line in data:
    #print ("----------------------")
    #print (line)
    #print ("----------------------")
    # D1 = line.split("..:..:.. fakehost")
    D1 = re.split(('\d\d fakehost'), line)
    #print (D1)
    #print ("-----------------------------")
    lList.append(D1)
df = pd.DataFrame(lList, columns =['Date', 'String'])
df1 = df.groupby(['Date']).count()
print (tabulate(df1))

l = ['sree','hari','krishna','reddy','patakota']
# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(l)
file1.close()



using a readlines()
file1 = open('s3_limits.py', 'r')
Lines = file1.readlines()

for line in Lines:
    # print("Line{}: {}".format(count,line.strip()))
    print(line)

import sys
print('hello')
sys.exit()
print('goodbye')

def func():
    print('selling')
    print('a colgate paste')
    print('by company owner')
func()
func()
func()

import smtplib
con = smtplib.SMTP('smtp.gmail.com', 587)
type(con)
con.ehlo()
con.starttls()
con.login('rambhaskarreddyp@gmail.com', 'Bhaskar@1994')
con.sendmail('rambhaskarreddyp@gmail.com', 'senderemailid', 'subject: so long ....\n\nDear boss, \n so long we vistored her', and thanks for your complimentry.)
con.quit()

from functools import reduce
seq = [2,3,4,5,7]
prod = reduce(lambda x, y: x*y, seq)
print(prod)

hari = [10,20,33,2,22,33,44,66,99,2,3]
filtered_result = map (lambda x: x*x, hari)
print(list(filtered_result))

x,y=1,1

def f():
global x:
y=0:
for I in (10,20,30):
    x+=1:
    y+=1:
    f():
    print(x,y):


mge = 'it was a bright freature in a World. welcome to DevOps Engineer.'
count = {}

for character in mge():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)

import pprint

theBoard = {'top-L': '', 'top-M': '', 'top-R': '', 'mid-L': '', 'mid-M': '', 'mid-R': '', 'low-L': '', 'low-M': '', 'low-R': ''}

pprint.pprint(theBoard)

theBoard['top-L'] = '0'
theBoard['top-M'] = '0'
theBoard['top-R'] = '0'
theBoard['mid-L'] = 'x'
theBoard['mid-M'] = 'x'
theBoard['low-R'] = 'x'

def printBoard(board):
    print(board['top-L'] +       '|' + board['top-M'] +     '|' + board['top-R'])
    print('-------')
    print(board['mid-L'] +       '|' + board['mid-M'] +     '|' + board['mid-R'])
    print('--------')
    print(board['low-L'] +       '|' + board['low-M'] +     '|' + board['low-R'])

printBoard(theBoard)


## Data Struture
message = 'years of strong IT experience in Software Configuration Management and DevOps engineering'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)


## parsing HTML  with the Beautiful Soup module

from selenium import webdriver
browser = webdriver.Firefox()

browser.get('https://www.youtube.com')
exit()

import bs4
import requests
res = requests.get('https://www.amazon.in/gp/product/B078BN2H3R/ref=s9_acss_bw_cg_oneplus_1a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-2&pf_rd_r=XZ3ZSX7XVXTASK6GTXRK&pf_rd_t=101&pf_rd_p=24bad984-66bf-4b89-9536-116c2ff740e5&pf_rd_i=21439725031')
res.status_code()




import bs4
import requests
>>> res = requests.get('https://www.flipkart.com/realme-narzo-10-that-white-128-gb/p/itmfaa990ac54b7a?pid=MOBFQ36APESHAPGA&lid=LSTMOBFQ36APESHAPGAHAKOMN&fm=neo%2Fmerchandising&iid=M_14ce8656-4cdb-401d-9170-4adaa3300fda_8.ZQR052C3U63C&ppt=clp&ppn=realme-c12-coming-soon-39e-d93k-store&ssid=2rjk04j6sg0000001597316841651&otracker=hp_omu_Best%2BBattery%2BPhones_2_8.dealCard.OMU_Best%2BBattery%2BPhones_ZQR052C3U63C_4&otracker1=hp_omu_WHITELISTED_neo%2Fmerchandising_Best%2BBattery%2BPhones_NA_dealCard_cc_2_NA_view-all_4&cid=ZQR052C3U63C')
>>> res.raise_for_status()
>>> soup = bs4.BeautifulSoup(res.text, 'html.parser')
>>> soup.select('#container > div > div._3Z5yZS.NDB7oB._12iFZG._3PG6Wd > div.ooJZfD._3FGKd2 > div.ooJZfD._2oZ8XT.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
[<div class="_1vC4OE _3qQ9m1">₹11,999</div>]
>>> elems = soup.select('#container > div > div._3Z5yZS.NDB7oB._12iFZG._3PG6Wd > div.ooJZfD._3FGKd2 > div.ooJZfD._2oZ8XT.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
>>> elems[0]
<div class="_1vC4OE _3qQ9m1">₹11,999</div>
>>> elems[0].text
'₹11,999'
>>> elems[0].text.strip()
'₹11,999'







