import requests
from bs4 import BeautifulSoup

def scrape_shopping_website(url):
    # Send a GET request to the website
    response = requests.get(https://dutchie.com/dispensary/curaleaf-pa-harrisburg/products/flower?weight=1-2oz)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table containing the items
    table = soup.find('table')
    
    # Initialize a list to store the extracted items
    items = []
    
    # Iterate through each row in the table
    for row in table.find_all('tr'):
        # Extract the item details from each column in the row
        columns = row.find_all('td')
        
        # Ensure the row contains columns
        if columns:
            # Extract the relevant information (e.g., name, price, etc.)
            item_name = columns[0].text.strip()
            item_price = columns[1].text.strip()
            item_description = columns[2].text.strip()
            
            # Create a dictionary to store the item details
            item = {
                'name': item_name,
                'price': item_price,
                'description': item_description
            }
            
            # Add the item to the list
            items.append(item)
    
    # Return the list of items
    return items

# Specify the URL of the shopping website
url = 'https://www.example.com/shopping'

# Scrape the website and get the items from the table
items = scrape_shopping_website(url)

# Print the extracted items
for item in items:
    print(item)
