# Automated Registration for contests at Codeforces Platform Using Selenium


### Install and import module

Use the package manager to install required module.
beautifulsoup4 will help us to parse source of pages
```bash
pip install selenium, beautifulsoup4
```
```python
from selenium import webdriver
import time
from bs4 import BeautifulSoup
```
### Create drive to chrome and go to codeforce contest page

```python
driver = webdriver.Chrome()
driver.get("https://codeforces.com/contests")
```

### Get get source of codeforce contest page and parse it with beautifullsoup

```python
page=driver.page_source
dom = BeautifulSoup(page, 'html.parser')
```
### Get name and registration link of avalaible contest
```python
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

```
### Ask the user to choose a contest
```python
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
```
### Click on registration link with selenium
```python
a=driver.find_element_by_css_selector("a[href='"+link+"']")
a.click()
```

### Get user credentials email or handle and password
```python
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
```

### Fill fields
```python
handle_field=driver.find_element_by_css_selector("input[name='handleOrEmail']")
pass_handle=driver.find_element_by_css_selector("input[name='password']")

handle_field.send_keys(email)
pass_handle.send_keys(c_pass)
```
### Submit the login form 
```python
submit=driver.find_element_by_css_selector(".submit")
submit.click()
```
### Wait the register page of contest load and click on register button
```python
time.sleep(5)
submit1=driver.find_element_by_css_selector(".submit")
submit1.click()
```

## Lear more
Selenium [documation](https://selenium-python.readthedocs.io/getting-started.html)
