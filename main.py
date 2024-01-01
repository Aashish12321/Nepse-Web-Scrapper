import requests
import csv
import json
import time
from bs4 import BeautifulSoup

def fetchAndSaveToFile(url):
    html_data = requests.get(url)
    html_data = html_data.text

    soup = BeautifulSoup(html_data, "lxml")

    with open("data/website.html", "w", encoding='utf-8') as f:
        f.write(soup.prettify())

    th_tags = soup.find_all('th')
    td_tags = soup.find_all('td')

    with open("data/stockData.csv", "w", encoding='utf-8') as f:
        for th_tag in th_tags:
            f.write(str(th_tag.text) + ',')
        f.write("\n")

        c = 0
        for td_tag in td_tags:
                c+=1
                temp_data = str(td_tag.text).replace("," , "") + ','
                temp_data = temp_data.replace(" ", "")
                f.write(temp_data.replace("\n", ""))
                if c>=10:
                    f.write("\n")
                    c=0


def csvToJson():
    csv_file_path = 'data/stockData.csv'
    json_file_path = 'data/stockData.json'

    # Read CSV file and convert to JSON
    csv_data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            csv_data.append(row)

    # Write JSON data to a file
    with open(json_file_path, 'w') as json_file:
        json.dump(csv_data, json_file, indent=2)



if __name__=='__main__':

    # Fetching data of stocks after every 10 second.
    while True:
        url = "https://www.sharesansar.com/live-trading"
        fetchAndSaveToFile(url)
        csvToJson()
        time.sleep(10)


# "lxml" is the parser library specified for Beautiful Soup to use when parsing the HTML or XML data in html_data. 
# Beautiful Soup supports multiple parsers, and "lxml" is one of the options.

