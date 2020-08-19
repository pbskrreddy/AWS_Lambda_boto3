# import bs4
# import requests
# res = requests.get('https://www.flipkart.com/realme-narzo-10-that-white-128-gb/p/itmfaa990ac54b7a?pid=MOBFQ36APESHAPGA&lid=LSTMOBFQ36APESHAPGAHAKOMN&fm=neo%2Fmerchandising&iid=M_14ce8656-4cdb-401d-9170-4adaa3300fda_8.ZQR052C3U63C&ppt=clp&ppn=realme-c12-coming-soon-39e-d93k-store&ssid=2rjk04j6sg0000001597316841651&otracker=hp_omu_Best%2BBattery%2BPhones_2_8.dealCard.OMU_Best%2BBattery%2BPhones_ZQR052C3U63C_4&otracker1=hp_omu_WHITELISTED_neo%2Fmerchandising_Best%2BBattery%2BPhones_NA_dealCard_cc_2_NA_view-all_4&cid=ZQR052C3U63C')
# res.raise_for_status()
# soup = bs4.BeautifulSoup(res.text, 'html.praser')
# soup.select('#container > div > div._3Z5yZS.NDB7oB._12iFZG._3PG6Wd > div.ooJZfD._3FGKd2 > div.ooJZfD._2oZ8XT.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
# elems = soup.select('#container > div > div._3Z5yZS.NDB7oB._12iFZG._3PG6Wd > div.ooJZfD._3FGKd2 > div.ooJZfD._2oZ8XT.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
# elems[0].text
#
#
# import boto3
# client = boto3.client('ec2')
# response = client.run_instances(ImageId ='ami-3453434ca739,'
#                                 InstanceType='t2.micro',
#                                 MinCount=1,
#                                 MaxCount=1)
# for instance in respose['Instances']:
#     print(instance['InstanceId'])s

# name = input('Please enter you name')
# message = 'Hello {}, welcome the python for AWS lambda'.format(name)
# print(message)

# # write a script sum of two numbers.
# one = input('Please enter number one is: ')
# two = input('Please enter number two is: ')
# result = int(one)*int(two)
# message = 'Multiple of {} and {} is {}'.format(one,two,result)
# print(message)
#
# x = 'Single quotes line'
# y = "Double quotes line"
# z = '''
#    Java Home Cloud
#    Whitefield
#    Bangalore
#    560045
# '''
# print(x)
# print(y)
# print(z)

## instance terminated
import boto3
client = boto3.client('ec2')
res = client.terminate_instances(InstanceIds=['i-eeroprelqlr'])

for instance in res('TerminatingInstances'):
    print('The instance id is  {} terminated'.format(instance['InstanceId']))

## instance stopped
import  boto3
client = boto3.client('ec2')
res = client.stop_instances(InstanceIds=['i-ederfi1o34'])

for instance in res('StoppedInstances'):
    print('the instance has been stopped, id is {}'.format(instance['InstanceId']))


