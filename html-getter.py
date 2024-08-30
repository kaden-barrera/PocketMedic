from bs4 import BeautifulSoup
import requests
import json

# Fetch the HTML content
url = 'https://openpage-ebooks.jblearning.com/wr/viewer.html?skipLastRead=true&oneTimePasscode=ST-71bece52-f72d-4a85-be63-d0976ad7e79d&launchOrgCode=ascendlti&language=en-US#book/eabe87bb-3157-4ae2-82ef-c8c854c85105/item9'
response = requests.get(url)
html_content = response.text

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')
# Example: Extracting all links
links = [a['href'] for a in soup.find_all('a', href=True)]

# Convert to JSON
data = {'links': links}

# Save to JSON file
with open('links.json', 'w') as json_file:
    json.dump(data, json_file)