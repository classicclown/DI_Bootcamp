# import requests
# from bs4 import BeautifulSoup
# import csv
# from typing import List, Dict

# def fetch_webpage(url: str) -> str:
#     """Fetch the content of a webpage."""
#     response = requests.get(url)
#     response.raise_for_status()  # Raise an exception for bad status codes
#     return response.text

# def parse_table(table) -> List[Dict[str, str]]:
#     """Parse a table and return a list of dictionaries representing rows."""
#     headers = [header.text.strip() for header in table.find_all('th')]
#     rows = []
#     for row in table.find_all('tr')[1:]:  # Skip the header row
#         cells = row.find_all(['td', 'th'])
#         if len(cells) == len(headers):
#             row_data = {headers[i]: cell.text.strip() for i, cell in enumerate(cells)}
#             rows.append(row_data)
#     return rows

# def scrape_video_game_sales(url: str):
#     """Scrape video game sales data from the Wikipedia page."""
#     html_content = fetch_webpage(url)
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Find all tables in the page
#     tables = soup.find_all('table', class_='wikitable')

#     all_data = []
#     current_year = None

#     for table in tables:
#         # Check if the table is for a specific year (1998 onwards)
#         year_header = table.find_previous(['h3', 'h4'])
#         if year_header:
#             year_text = year_header.text.strip()
#             # Extract year from the header text
#             current_year = ''.join(filter(str.isdigit, year_text))
        
#         if current_year and current_year.isdigit() and int(current_year) >= 1998:
#             data = parse_table(table)
#             for row in data:
#                 row['Year'] = current_year
#             all_data.extend(data)
#         else:
#             # For years before 1998, the data is in a different format
#             rows = table.find_all('tr')
#             for row in rows[1:]:  # Skip the header row
#                 cells = row.find_all(['td', 'th'])
#                 if len(cells) >= 5:
#                     year = cells[0].text.strip()
#                     title = cells[1].text.strip().replace('*', '')
#                     developer = cells[2].text.strip()
#                     publisher = cells[3].text.strip()
#                     platform = cells[4].text.strip()
#                     sales = cells[5].text.strip() if len(cells) > 5 else "N/A"
#                     all_data.append({
#                         'Year': year,
#                         'Title': title,
#                         'Developer': developer,
#                         'Publisher': publisher,
#                         'Platform': platform,
#                         'Sales': sales
#                     })

#     # Determine all unique fieldnames
#     all_fieldnames = set()
#     for row in all_data:
#         all_fieldnames.update(row.keys())
    
#     # Ensure 'Year' and 'Title' are the first fields
#     fieldnames = ['Year', 'Title'] + sorted(list(all_fieldnames - {'Year', 'Title'}))

#     # Write data to CSV
#     with open('us_video_game_sales.csv', 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         for row in all_data:
#             # Ensure all fields are present in each row, even if empty
#             row_data = {field: row.get(field, '') for field in fieldnames}
#             writer.writerow(row_data)

#     print("Data has been scraped and saved to 'us_video_game_sales.csv'")

# # URL of the Wikipedia page
# url = "https://en.wikipedia.org/wiki/List_of_best-selling_video_games_in_the_United_States_by_year"

# # Run the scraper
# scrape_video_game_sales(url)





