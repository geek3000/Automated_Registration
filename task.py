from selenium import webdriver
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_email():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    
    flow = InstalledAppFlow.from_client_secrets_file('code.json', SCOPES)
    creds = flow.run_local_server(port=0)

    service = build('gmail', 'v1', credentials=creds)

    
    results = service.users().messages().list(userId='me', maxResults=1).execute()
    message_id = results['messages'][0]['id']
    message = service.users().messages().get(userId='me', id=message_id).execute()
    print(message['snippet'])
    body=message['snippet']
    body=body.split(' ')
    for word in body:
        if word.startswith('http'):
            return word

driver = webdriver.Chrome()
driver.get("https://codeforces.com/register")

handle_field = driver.find_element_by_css_selector("input[name='handle']")
handle_field.send_keys("nick")

email_field = driver.find_element_by_css_selector("input[name='email']")
email_field.send_keys("email")

pass_field = driver.find_element_by_css_selector("input[name='password']")
pass_field.send_keys("dmedgieiGMIEG/EIGTDDqeq geg egG   E   E")

c_pass_field = driver.find_element_by_css_selector("input[name='passwordConfirmation']")
c_pass_field.send_keys("dmedgieiGMIEG/EIGTDDqeq geg egG   E   E")

btn_submit= driver.find_element_by_css_selector(".submit")
btn_submit.click()
time.sleep(5)
link=get_email()

driver.get(link)
