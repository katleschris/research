import requests
from bs4 import BeautifulSoup
import csv

class webCrawler:
    def start_web_crawler(self, url):
        web_request = requests.get(url)
        if web_request.status_code != 200:
            print(f"Failed to retrieve the web page. Status code: {web_request.status_code}")
            return []

        soup = BeautifulSoup(web_request.text, 'html.parser')
        search_results_div = soup.find("div", {"id": "search-results"})
        if not search_results_div:
            print("No search results found.")
            return []

        school_urls = []
        for div in search_results_div.find_all("div", {"class": "row"}):
            try:
                school_url = div.find("a", href=True)["href"].strip()
                school_urls.append(school_url)
            except Exception as e:
                print(f"Error extracting URL: {e}")
                continue

        return school_urls
    
    def get_school_details(self, url):
        web_request = requests.get(url)
        if web_request.status_code != 200:
            print(f"Failed to retrieve the web page. Status code: {web_request.status_code}")
            return None

        soup = BeautifulSoup(web_request.text, 'html.parser')
        container_div = soup.find("main")
        if not container_div:
            print("No container div found.")
            return None

        try:
            school_name = container_div.find("h1").text.strip()
            location = container_div.find("h4").text.strip()
            address = container_div.find("span", {"class": "map-address load-address"}).text.strip()
            return {"School name": school_name, "Location": location, "Address": address}
        except Exception as e:
            print(f"Error extracting school details: {e}")
            return None

    def write_to_csv(self, data, filename="schools.csv"):
        fields = ["School name", "Location", "Address"]
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

class driverClass:
    @staticmethod
    def main():
        print("Inside driver")
        crawler = webCrawler()
        school_urls = crawler.start_web_crawler('https://www.goodschools.com.au/compare-schools/search/in-victoria')
        
        school_details_list = []
        for url in school_urls:
            school_details = crawler.get_school_details(url)
            if school_details:
                school_details_list.append(school_details)
        
        print(school_details_list)
        crawler.write_to_csv(school_details_list)

if __name__ == "__main__":
    driverClass.main()