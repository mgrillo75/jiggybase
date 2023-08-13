import os
import jiggybase

# Set up the JiggyBase client
os.environ['JIGGYBASE_API_KEY'] = 'jgy-JzMNhVesyWAiuaLnuTwuoDaAgQQHOsoWmlZZAEFSCt'
jb = jiggybase.JiggyBase()

# Select the collection
collection = jb.collection('S71200 CMS')

# Define the query
#question = "please select a Siemens 480VAC VFD for a 5 HP motor and also select Rittal enclosure that is sized to have the VFD installed inside of it"

# Query the collection
#query_response = collection.query(question)

messages = [{'role':'user',  'content': 'please let me know the part number for the Siemens S7-1200 CMS Module'}]

rsp = collection._chat_completion(messages, model="gpt-4")   # note _ as this is preliminary low-level interface

print(rsp)

# Process the response data
#if query_response.results:
#    print("Query successful!")
#    for result in query_response.results:
#        if isinstance(result, jiggybase.DocumentChunkWithScore):
#            print("Answer:", result.text)
#            print("\n")
#else:
#    print("No results found.")