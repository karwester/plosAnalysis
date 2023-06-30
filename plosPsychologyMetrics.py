'''
Requests all publication details of articles assigned to "psychology" discipline from PlosONE API and writes them into a csv file

Fields requested:
1) title
2) abstract
3) publication year
4) citations
5) views counter_total_all
6) id (doi)
7)journal
80received, accepted and publication dates
#use only research articles
#article_type
#get citations by scraping


'''
import requests
import csv
from bs4 import BeautifulSoup


#url = 'http://api.plos.org/search?q=subject:"Psychology"&article_type="Research Article"&fq=title:[* TO *]&fl=id,journal,publication_date,received_date,accepted_date, counter_total_all, counter_total_month,article_type,title,abstract&wt=json' #no = 446576/52436


# In this query, fq=title:[* TO *] is the filter query that 
# ensures only documents with non-empty titles are returned. 
# This will exclude the documents with empty dictionaries or titles


#check number found
# response = requests.get(url)
# data = response.json()
# print(data['response']['numFound'])



total_rows = 52436
batch_size = 100
path = r'C:\Users\karol\projects\plos\plosOnePsychologyMetrics.csv'
fields = ['id','title', 'abstract', 'journal', 'publication_date', 'received_date', 'accepted_date', 'counter_total_all', 'counter_total_month']

with open(path, 'w',encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

    for start in range(0, total_rows, batch_size):
        #Fetch the JSON data from the URL
        url = f'http://api.plos.org/search?q=subject:"Psychology"&article_type="Research Article"&fq=title:[* TO *]&fl=id,journal,publication_date,received_date,accepted_date, counter_total_all, counter_total_month,title,abstract&wt=json&start={start}&rows={batch_size}' #no = 446576/52436

        response = requests.get(url)
        data = response.json()
        # Extract the required fields from the JSON data
        for item in data['response']['docs']:
            try:
                #row = [item[field][0] if field in item else '' for field in fields]
                row = [str(item.get(field, '')) for field in fields]
                writer.writerow(row)
            except Exception as e:
                print("Error occurred:", str(e))
        if start + batch_size >= total_rows:
            break
print("All rows written to the CSV file. Exiting the script.")
#29.06

