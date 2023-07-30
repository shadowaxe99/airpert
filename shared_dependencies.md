Shared Dependencies:

1. **Email Data Schema:** The structure of the email data that is processed, including fields like sender, subject, and attachments. This schema is used in "email_service/email_processor.py" and "attachment_processing/attachment_extractor.py".

2. **Attachment Data Schema:** The structure of the attachment data that is extracted, including fields like filename, file type, and content. This schema is used in "attachment_processing/attachment_extractor.py", "attachment_processing/text_extractor.py", "ml_models/topic_classifier.py", and "ml_models/summarizer.py".

3. **Processed Data Schema:** The structure of the processed data that is stored in Airtable, including fields like topic, summary, and original content. This schema is used in "ml_models/topic_classifier.py", "ml_models/summarizer.py", and "database_integration/airtable_updater.py".

4. **Email Address:** The specific email address to which users send or forward emails. This is used in "email_service/email_processor.py".

5. **Airtable API Key and Table Name:** The API key and table name for the Airtable database. These are used in "database_integration/airtable_updater.py".

6. **Function Names:** The names of the functions that perform key tasks, such as "extract_attachments", "extract_text", "classify_topic", "generate_summary", and "update_airtable". These function names are used across multiple files.

7. **Model Names:** The names of the pre-trained machine learning models used for topic classification and summarization. These are used in "ml_models/topic_classifier.py" and "ml_models/summarizer.py".

8. **Main Function:** The main function that orchestrates the entire process, likely named something like "process_email". This function is used in "main.py" and calls functions from all other files.