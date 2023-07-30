```python
import os
import email
from email.message import Message
from typing import List, Dict

def extract_attachments(email_data: Dict) -> List[Dict]:
    """
    Extracts attachments from the provided email data.

    :param email_data: A dictionary containing email data.
    :return: A list of dictionaries, each representing an attachment.
    """
    attachments = []

    # Parse the raw email content
    msg = email.message_from_string(email_data['raw_content'])

    # Iterate over the email parts
    for part in msg.walk():
        # Check if the part is an attachment
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            # Extract the attachment data
            attachment_data = part.get_payload(decode=True)
            # Create a dictionary for the attachment
            attachment = {
                'filename': part.get_filename(),
                'content': attachment_data,
                'content_type': part.get_content_type()
            }
            attachments.append(attachment)

    return attachments
```