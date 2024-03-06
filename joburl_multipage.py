import requests
from lxml import html

domain = "https://www.reed.co.uk"
base_url = "https://www.reed.co.uk/jobs/data-analyst-jobs?pageno={}"
job_urls = []

for page in range(1, 119):  # Change 101 to the number of pages you want to scrape
    url = base_url.format(page)
    response = requests.get(url)
    tree = html.fromstring(response.content)

    # Define multiple XPath expressions for job URLs
    xpath_exprs = [
        '//a[@data-qa="job-card-title"]/@href',
        '//a[@class="gtmJobTitleClickResponsive"]/@href',
        '//a[contains(@class, "jobtitle")]/@href'
        # Add more XPath expressions here
    ]

    # Extract job URLs using multiple XPath expressions
    for xpath_expr in xpath_exprs:
        job_urls.extend(tree.xpath(xpath_expr))

# Appending base URL to job URLs and printing in list format
for job_url in job_urls:
    full_url = domain + job_url
    # print(full_url)
    url = full_url
    if full_url == "https://www.reed.co.uk/jobs/risk-data-analyst/52190438?source=searchResults&filter=%2Fjobs%2Fdata-analyst-jobs":
        continue
    response = requests.get(url)
    tree = html.fromstring(response.content)

    # Extracting title using the provided XPath
    title_element = tree.xpath('//div[@class="col-xs-12"][1]/h1')[0]
    title = title_element.text.strip() if title_element is not None else "Not specified"

    # Extracting salary
    salary_element = tree.xpath('//div[@class="salary col-xs-12 col-sm-6 col-md-6 col-lg-6"]//span[@data-qa="salaryLbl"]')[0]
    salary = salary_element.text.strip() if salary_element is not None else "Not specified"

    # Extracting location
    location_element = tree.xpath('//div[contains(@class, "location")]//span[@itemprop="addressLocality"]/text()')[0]
    region_element = tree.xpath('//div[contains(@class, "location")]//span[@data-qa="localityLbl"]/text()')[0]
    location = f"{location_element}, {region_element}" if location_element and region_element else "Not specified"

    # Extracting contract type
    contract_type_element = tree.xpath('//div[@class="time col-xs-12 col-sm-6 col-md-6 col-lg-6"]//span[@itemprop="employmentType"]/a[1]')[0]
    contract_type = contract_type_element.text.strip() if contract_type_element is not None else "Not specified"

    # Extracting job type
    job_type_element = tree.xpath('//div[@class="time col-xs-12 col-sm-6 col-md-6 col-lg-6"]//span[@itemprop="employmentType"]/a[2]')[0]
    job_type = job_type_element.text.strip() if job_type_element is not None else "Not specified"


    print("1. Detailed URL:", url)
    print("2. Title:", title)
    print("3. Salary:", salary)
    print("4. Contract Type:", contract_type)
    print("5. Job Type:", job_type)
    print("6. Location:", location)
    print("\n")
