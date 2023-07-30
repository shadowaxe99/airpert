```python
import os
from airtable import Airtable

# Airtable API Key and Table Name
API_KEY = os.getenv('AIRTABLE_API_KEY')
BASE_KEY = os.getenv('AIRTABLE_BASE_KEY')
TABLE_NAME = os.getenv('AIRTABLE_TABLE_NAME')

airtable = Airtable(BASE_KEY, TABLE_NAME, API_KEY)

def update_airtable(processed_data):
    """
    Function to update Airtable with processed data
    """
    for data in processed_data:
        airtable.insert(data)
```
