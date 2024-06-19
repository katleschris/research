import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# Define the range of pages to scrape
pages = range(1, 6)

# Initialize an empty list to store school data
school_data = []

for page in pages:
    url = f'https://www.goodschools.com.au/compare-schools/search/in-victoria/secondary?distance=10km&suburb_in=in-victoria&state_ids%5B0%5D=7&region_ids%5B0%5D=1300&school_level_ids%5B0%5D=1&page={page}'
    print(f"Retrieving page {page}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve page {page}: {e}")
        continue

    try:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results_div = soup.find("div", {"id": "search-results"})
        media_body_div = search_results_div.find_all("div", {"class": "media-body"})
    except AttributeError as e:
        print(f"Error parsing HTML on page {page}: {e}")
        continue

    school_urls = []
    for a_tag in media_body_div:
        try:
            school_url = a_tag.find("a", href=True)["href"].strip()
            school_urls.append(school_url)
        except (AttributeError, TypeError) as e:
            print(f"Error finding school URL on page {page}: {e}")
            continue

    for link in school_urls:
        school_info = {}
        try:
            response = requests.get(link, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to retrieve school page {link}: {e}")
            continue

        try:
            soup = BeautifulSoup(response.text, 'html.parser')
            school_info["School Name"] = soup.find("h1").text.strip()
            school_info["Location"] = soup.find("h4").text.strip()
            school_info["Address"] = soup.find("span", {"class": "map-address load-address"}).text.strip()
            school_info["Sector"] = soup.find("p", {"class": "d-inline float-left"}).text.strip()

            academic_results_div = soup.find("div", class_="col-md-6 col-sm-6 col-6")
            if academic_results_div:
                academic_results = academic_results_div.find_all("p")
                for tag in academic_results:
                    pattern = r":\s*(\S+)"
                    match = re.search(pattern, tag.text)
                    if match:
                        value = match.group(1)
                        if 'Scores of 40+' in tag.text:
                            school_info["Scores of 40+"] = value
                        if 'Median Score' in tag.text:
                            school_info["Median Score"] = value
                        if 'VCE' in tag.text:
                            school_info["Satisfactory completions of VCE"] = value
                        if "VET" in tag.text:
                            school_info["Satisfactory completions of VET"] = value
                    else:
                        print("No match found in academic results.")
        except AttributeError as e:
            print(f"Error parsing school page {link}: {e}")
            continue

        school_data.append(school_info)

# Create a DataFrame and save the data to a CSV file
df = pd.DataFrame(school_data)
df.to_csv('schools.csv', index=False)
