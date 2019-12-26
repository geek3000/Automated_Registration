from selenium import webdriver
import time
from bs4 import BeautifulSoup
email=''
pwd=''
driver = webdriver.Chrome()
contest={}
driver.get("https://codeforces.com/contests")

page=driver.page_source
dom = BeautifulSoup(page, 'html.parser')

i=1
for tr in dom.find_all("tr"):
    cid=tr.get("data-contestid")
    if cid:
        link=tr.find_all("a")
        for l in link:
            link_class=l.get("class")
            
            
            if link_class == ['red-link']:
                name=tr.find("td").text
                lien=l.get("href")
                name=name.replace('\n', '')
                contest[i]=[]
                contest[i].append(name)
                contest[i].append(lien)
                i+=1


print("Choose a contest")
print()
for c in contest:
    print(str(c)+". "+contest[c][0])
url=""
try:
    nb=int(input("Enter number of contest: "))
    link=contest[nb][1]
except:
    print("Incorrect choice")

a=driver.find_element_by_css_selector("a[href='"+link+"']")
a.click()
email=''
a=input("Enter your email or handle: ")
if a != '':
    email=a
else:
    print("Invalid Email")
    exit()

c_pass=''
a=input("Enter your password: ")
if a != '':
    c_pass=a
else:
    print("Invalid Password")
    exit()

handle_field=driver.find_element_by_css_selector("input[name='handleOrEmail']")
pass_handle=driver.find_element_by_css_selector("input[name='password']")

handle_field.send_keys(email)
pass_handle.send_keys(c_pass)

submit=driver.find_element_by_css_selector(".submit")
submit.click()
time.sleep(5)
submit1=driver.find_element_by_css_selector(".submit")
submit1.click()
