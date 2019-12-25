# Automated Registration for contests at Codeforces Platform Using Selenium


### Install and import module

Use the package manager to install required module.

```bash
pip install selenium
```
```python
from selenium import webdriver
```
### Create drive to chrome and go to codeforce registration page

```python
driver = webdriver.Chrome()
driver.get("https://codeforces.com/register")
```

### Get handle, email, password and password confirm input

```python
handle_field =driver.find_element_by_css_selector("input[name='handle']")
email_field = driver.find_element_by_css_selector("input[name='email']")
pass_field =driver.find_element_by_css_selector("input[name='password']")
c_pass_field = driver.find_element_by_css_selector("input[name='passwordConfirmation']")
```
### Fill entry with your information
```python
handle_field.send_keys("nick")
email_field.send_keys("email")
pass_field.send_keys("pass")
c_pass_field.send_keys("pass")
```
### Get submit button and click it
```python
btn_submit= driver.find_element_by_css_selector(".submit")
btn_submit.click()
```
### Confirm your account
Use Gmail Api to get confirmatiom email

Follow this [link](https://codehandbook.org/how-to-read-email-from-gmail-api-using-python/)
get confirmation link and go to it with
```python
driver.get(link)
```
## Lear more
Selenium [documation](https://selenium-python.readthedocs.io/getting-started.html)

Gmail Api [documation](https://developers.google.com/gmail/api/quickstart/python)

Also [this](https://medium.com/better-programming/a-beginners-guide-to-the-google-gmail-api-and-its-documentation-c73495deff08)
