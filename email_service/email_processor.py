```python
import email
import imaplib
from attachment_processing.attachment_extractor import extract_attachments

# Email Data Schema
EMAIL_ADDRESS = "your_email_address"
EMAIL_PASSWORD = "your_email_password"
IMAP_SERVER = "imap.gmail.com"

def login_to_email():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    return mail

def fetch_emails(mail):
    mail.select('inbox')
    result, data = mail.uid('search', None, "ALL")
    email_ids = data[0].split()
    return email_ids

def process_email(email_id, mail):
    result, email_data = mail.uid('fetch', email_id, '(BODY.PEEK[])')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)

    email_data = {
        "subject": email_message['Subject'],
        "from": email_message['From'],
        "to": email_message['To'],
        "date": email_message['Date']
    }

    attachments = extract_attachments(email_message)
    email_data["attachments"] = attachments

    return email_data

def process_all_emails():
    mail = login_to_email()
    email_ids = fetch_emails(mail)

    for email_id in email_ids:
        email_data = process_email(email_id, mail)
        print(email_data)

if __name__ == "__main__":
    process_all_emails()
```