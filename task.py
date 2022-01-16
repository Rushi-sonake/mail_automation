"""Template robot with Python."""
import imaplib
import email
import os
from typing import Counter
from RPA.Robocloud.Secrets import FileSecrets
key = FileSecrets()


_secret = key.get_secret("credentials")

user_name = "rushisoanke15@gmail.com"
password = _secret["password_"]
smtp_server = 'imap.gmail.com'
port = 993 
detach_dir = 'attachments'

def Login_mail():
    print("start")
    con =imaplib.IMAP4_SSL(smtp_server)
    con.login(user_name, password)
    con.select("INBOX")
    type, data = con.search(None, 'UNSEEN')
    data_new = data[0]
    items =data_new.split()
    #print(items)
    for i in items:
        type,mail= con.fetch(i, '(RFC822)')
        email_body = mail[0][1]
        email_body_str = email_body.decode('UTF-8')
        mails= email.message_from_string(email_body_str)

        if mails.get_content_maintype() != 'multipart':
            continue
        print("["+mails["FROM"]+"] :" +mails["SUBJECT"]) 
        for part in mails.walk():
            if part.get_content_maintype == 'multipart':
                continue
        if part.get('Content-Disposition') is None:
            continue
        filename = part.get_filename()
        Counter = 1
        if not filename:
            filename = 'part-%03%s'%(Counter, bin)
            Counter+1

        attachment_path = os.path.join(detach_dir, filename)

        if not os.path.isfile(attachment_path):
            fp = open(attachment_path,'wb')
            fp.write(part.get_payload(decode = True))
            fp.close
        print("succesful")
        
    

def minimal_task():
    print("Done.")


if __name__ == "__main__":
    minimal_task()
    Login_mail()
 