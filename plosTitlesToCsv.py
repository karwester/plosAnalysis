'''
Requests all publication titles assigned to "psychology" discipline from PlosONE API and writes them into a csv file

'''
import requests
import csv

#url = 'http://api.plos.org/search?q=author:"Sylwester" AND title:"Twitter" AND subject: "Psychology"&fl=subject&wt=json'
#url = 'http://api.plos.org/search?q=subject:"Psychology" &fl=subject, title&wt=json' #no = 446576
#url = 'http://api.plos.org/search?q=subject:"Psychology"&fq=title:[* TO *]&fl=title&wt=json' #no = 446576
#url = 'http://api.plos.org/search?q=subject:"Psychology"&fq=title:[* TO *]&fl=title&wt=json&start=1&rows=100' #no = 446576

# In this query, fq=title:[* TO *] is the filter query that 
# ensures only documents with non-empty titles are returned. 
# This will exclude the documents with empty dictionaries or titles

batch_size = 100
#print(data['response']['numFound'])
total_rows = 52365
path = r'C:\Users\karol\projects\plos\plosOnePsychologyTitles.csv'
with open(path, 'w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    for start in range(0, total_rows, batch_size):
        #Fetch the JSON data from the URL
        url = f'http://api.plos.org/search?q=subject:"Psychology"&fq=title:[* TO *]&fl=title&wt=json&start={start}&rows={batch_size}'
        response = requests.get(url)
        data = response.json()
        # Extract the required fields from the JSON data
        for item in data['response']['docs']:
            try:
                row = [item['title']]
                writer.writerow(row)
            except Exception as e:
                print("Error occurred:", str(e))
        if start + batch_size >= total_rows:
            break
print("All rows written to the CSV file. Exiting the script.")