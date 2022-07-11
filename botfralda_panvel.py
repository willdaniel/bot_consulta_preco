import requests
from bs4 import BeautifulSoup
import smtplib

# url + request
url_panvel = 'https://www.panvel.com/panvel/fralda-huggies-supreme-care-hiper-g-com-64-unidades/p-874890'
r_panvel = requests.get(url_panvel)

# salva o html no url_panvel
html_panvel = r_panvel.text

# soup
soup = BeautifulSoup(html_panvel, 'html.parser')

# get iten
fralda1 = soup.find('span', class_="deal-price ng-star-inserted").get_text()
fralda2 = soup.find('span', class_="label-pack").get_text()

# send email
sender = 'seuemail@gmail.com'
receivers = ['destinatario@gmail.com', 'destinatario@gmail.com']

# smtp
smtpHost = 'smtp.office365.com'
smtpPort = 587
password = "password"
subject = "Confira o valor da fralda na Panvel hoje!"

# Add the From: and To: headers at the start!
message = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
           % (sender, ", ".join(receivers), subject))
message += f"O valor da fralda hoje na Panvel e {fralda1}. \n\nPromo:{fralda2} \n\nSeu link para compra https://www.panvel.com/panvel/fralda-huggies-supreme-care-hiper-g-com-64-unidades/p-874890"

smtpObj = smtplib.SMTP(smtpHost, smtpPort)
# smtpObj.set_debuglevel(1)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.ehlo()
smtpObj.login(sender, password)
smtpObj.sendmail(sender, receivers, message)
smtpObj.quit()

print(".............................")
print("bot finalizado com sucesso!!!")
print(".............................")
