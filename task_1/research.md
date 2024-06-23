# Web Scraper Documentation

## Tools and Libraries Used

- **Python**: The main programming language used for writing the script.
- **Requests**: The Python library for making HTTP requests to fetch web pages.
- **BeautifulSoup**: The Python library for parsing HTML and XML documents.
- **pandas**: The data manipulation and analysis library used to format and save data into a CSV file.
- **re**: The regular expressions library for extracting specific patterns from text.

## Steps Taken

### Fetching Web Pages
The `fetch_page` function uses the `requests` library to fetch the content of web pages. It handles exceptions to ensure the script can continue running even if a request fails.

### Parsing Search Results
The `parse_search_results` function uses `BeautifulSoup` to parse the HTML content of the search results page. It extracts URLs of individual school pages by finding the a tags in each div that contains a school.

### Fetching and Parsing School Information
The `fetch_school_info` function fetches and parses information from individual school pages. It extracts the school's name, location, address, sector, and academic results.

### Main Function
The `main` function coordinates the entire scraping process. It iterates over multiple pages of search results, fetches and parses each school’s information, and stores the data in a list. Finally, it converts this list into a pandas DataFrame and saves it as a CSV file.

## Challenges faced
- **Incomplete or Inconsistent Data**: Not all school pages had complete information, requiring robust error handling and data validation.
- **Data Duplication**: At first there were a lot of instances where there was data duplication.
- **Parsing the right tag**: The academic results div had multiple p and span tags with the same class names and the only thing different was the text inside it and that was the only thing I could parse in order to get the correct data.
- **Choosing when to fetch the school data**: Considering that the name, suburb, and sector of the school was in the search results div already, it seemed more efficient to fetch information in the school information page after following the a tag to avoid errors.
- **Steep learning curve**: This was the first time I scraped a website, there were minor challenges but I was able to learn quickly and I am glad I did this assignment.

