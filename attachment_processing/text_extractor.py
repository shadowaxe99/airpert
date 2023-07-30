```python
from tika import parser

def extract_text(attachment_data):
    """
    Function to extract text from attachments using Apache Tika
    """
    processed_data = []

    for attachment in attachment_data:
        filename = attachment['filename']
        file_type = attachment['file_type']
        content = attachment['content']

        if file_type in ['ppt', 'pptx', 'pdf']:
            raw = parser.from_buffer(content)
            text = raw['content']

            processed_data.append({
                'filename': filename,
                'file_type': file_type,
                'content': text
            })

    return processed_data
```