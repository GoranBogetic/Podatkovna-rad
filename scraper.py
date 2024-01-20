import csv
import requests
import re
from bs4 import BeautifulSoup

def extract_and_save_data(url, output_file='formula_one_seasons.csv'):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve content from {url}. HTTP Status Code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    with open(output_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(['Season', 'Races'])

        for row in soup.find_all('th', attrs={'scope': 'row'})[:]:
            season = re.sub(r'[^0-9]', '', row.find('a').text.strip()) if row.find('a') else ''
            races = re.sub(r'[^0-9]', '', row.find_next('td').text.strip()) if row.find_next('td') else ''
            csvwriter.writerow([season, races])

    print(f"Data extracted and saved to {output_file}")

url = "https://en.wikipedia.org/wiki/List_of_Formula_One_seasons"
extract_and_save_data(url)
