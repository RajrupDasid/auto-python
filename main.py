import requests #http requests
from bs4 import BeautifulSoup #webscraping
#automate send email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()
#email content 
content=''

# extracting Hacker News Stories...

def extract_news(url):
    print('Extracting hacket news stories....')
    cnt=''
    cnt+=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
    response=requests.get(url)
    content-response.content
    soup=BeautifulSoup(content,'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt+=((str(i+1)+' :: '+tag.text+"\n"+'<br>')if tag.text!='More' else '')
        #print(tag,prettify)# find all('span',attrs={'class':'sitestr'})
    return(cnt)
cnt=extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>-------<br>')
content += ('<br><br>End of Message')
#sending email with proper parameter
print('Processing for Composing an Email')

#fill-out email details with required parameters
SERVER='smtp.gmail.com'
PORT=587
FROM=''
TO=''
PASS='' #put password here
#fp=open(file_name,'rb')
#create a plain message
#msg-MIMEText('')
msg=MIMEMultipart()

#msg.add_header('Content-Disposition','attachment','filename='empty.txt'')
msg['Subject']='Hacker News Top stories'+'This is an automatic email-send using python'+''+str(now.d(now.year)+'-'+str(now.month)+'-'+str(now.day)
msg['From']=FORM
msg['To']=TO

msg.attach(MIMEText(content, 'html'))
#fp.close()

print('Initiating Server......')
server=smtplib.SMTP(SERVER,PORT)
#server=smtplib.SMTP_SSL('smtp.gmail.com',465)
