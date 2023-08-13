import os
import json
import jiggybase
from  jiggybase.models import Document, DocumentMetadata, Source
import warnings

# Set up the JiggyBase client
os.environ['JIGGYBASE_API_KEY'] = 'jgy-JzMNhVesyWAiuaLnuTwuoDaAgQQHOsoWmlZZAEFSCt'
jb = jiggybase.JiggyBase()

warnings.simplefilter('ignore', category=UserWarning)

# Select the collection
collection = jb.collection('Dynamis')


other_metadata = {"to": ['bob@example.com'], "cc": ['hr@example.com', 'legal@example.com']}

# Example email metadata
email_metadata = DocumentMetadata(
    language   = "en",
    source     = Source.email,
    created_at = "2022-02-15T10:30:00",        # using ISO 8601 format (YYYY-MM-DDTHH:MM:SS) makes it possible to filter by date
    author     = "Alice <alice@example.com>",  # sender name and optional email address
    title      = "Reminder: Friday Meeting",   # subject
    description = json.dumps(other_metadata)   # put any other metadata here that is associated with the entire document 
)

# Create a Document object with the email text and metadata
email_document = Document(
    id       = "XX4HJ823930JK",   # unique ID for the document
    metadata = email_metadata,
    text     = "Hello Bob, I hope you're doing well. I just wanted to remind you about the upcoming meeting on Friday. Best, Alice",    
)

# Upsert the email_document into test_collection
upsert_response = collection.upsert(documents=[email_document])
print(upsert_response)
