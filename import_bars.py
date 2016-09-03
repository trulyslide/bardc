import MySQLdb
import boto3


dynamo = boto3.resource('dynamodb')
table = dynamo.Table('bardcBars')

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="joeadk_bardc",         # your username
                     passwd="trombone",  # your password
                     db="joeadk_bardc")        # name of the data base

cur = db.cursor()
cur.execute("SELECT * FROM bars WHERE active = 1")

for row in cur.fetchall():
    barID =  row[0]
    name = row[3]
    furl = row[4]
    address = row[7]
    phone = row[8]
    if(phone ==""):
    	phone = None
    website = row[9]
    if(website ==""):
    	website = None
    facebook = row[12]
    if(facebook ==""):
    	facebook = None
    twitter = row[13]
    if(twitter ==""):
    	twitter = None
    twit_pic = row[14]
    if(twit_pic ==""):
    	twit_pic = None
    tagline = row[22]
    if(tagline ==""):
    	tagline = None

    table.put_item(
        Item={
            'id': barID,
            'name': name,
            'furl': furl,
            'address': address,
            'phone': phone,
            'website': website,
            'facebook': facebook,
            'twitter': twitter,
            'twit_pic': twit_pic,
            'tagline': tagline
        }
    )
    print name
db.close()
