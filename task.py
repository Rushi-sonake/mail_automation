"""Template robot with Python."""
import imaplib
import email
import os
from datetime import datetime
from typing import Counter
from RPA.Robocorp.Vault import Vault

secret = Vault().get_secret("data")


user_name = "sonakerushi157@gmail.com"
password = "Rushi@157"
smtp_server = 'imap.gmail.com'
port = 993 
#detach_dir = 'attachments'

def login_mail():
    print("start")   
    con = imaplib.IMAP4_SSL(smtp_server, port)
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
            timestr= datetime.now().strftime("%Y%M%D")
            filename = 'part-%03%s' +timestr %(Counter, bin)
            Counter+1
        
        detach_dir = 'attachments'+'\\'+mails['SUBJECT']
        
        file = os.makedirs(detach_dir)
         
        file_location= os.path.join(detach_dir, filename)

        if not os.path.isfile(file_location):
            fp = open(file_location,'wb')
            fp.write(part.get_payload(decode = True))
            fp.close
    typ,delet = con.search(None, 'SEEN')
    for i in delet[0].split():
        con.store(i, '+FLAGS','\\Deleted')
    con.expunge()
    con.close()
    con.logout()

    print("succesful")
        
    

def minimal_task():
    print("Done.")


if __name__ == "__main__":
    minimal_task()
    login_mail()
 