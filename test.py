import requests 
import re
from bs4 import BeautifulSoup

URL = "https://www.edunherkkukeidas.fi/toimipiste/keskusta/"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

paragraphs = soup.find_all(["p", "strong"])
    
    # Print the text content of each element

paragraphs= paragraphs[4:]

paragraphs= paragraphs[:-2]

pattern = r"^<strong>(\d{2},\d{2}|\d{2})€<\/strong>"

filtered_list = [str(item) for item in paragraphs if not re.search(pattern, str(item))]

#text_without_tags = re.sub('<[^<]+?>', '', filtered_list)

#print(filtered_list)

for element in filtered_list:
    print(re.sub('<[^<]+?>', '', element))