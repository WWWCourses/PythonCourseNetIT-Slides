import requests
import logging
import bs4

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
logger.setLevel(logging.ERROR)


def get_html_from_file(filename="./page.html"):
    """Use this function while developing your scraper to avoid making unnecessary requests"""
    with open(filename, "r") as f:
        return f.read()


def get_html(url):
    """Retrieves the HTML content of a given URL, handling errors appropriately."""

    # set user-agent
    user_agent = "A scrapper for learning"
    headers = {"User-Agent": user_agent}

    # perform GET request
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        response.encoding = "utf-8"
        return response.text

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to retrieve HTML from {url}: {e}")
        raise  # re-raise the exception to be handled by the caller


def extract_data(html):
    soup = bs4.BeautifulSoup(html, "html.parser")

    ### get all countries ('<div class="col-md-4 country">')
    selector = "#countries div.country"
    countries = soup.select(selector=selector)

    ### get Bulgaria area:
    # get Bulgaria data div:
    bulgaria = list(
        filter(
            lambda c: c.select_one(".country-name").text.strip().lower() == "bulgaria",
            countries,
        )
    )[0]
    logger.debug(f"Bulgaria data div: {bulgaria}")

    # from Bulgaria data div get "span.country-area" value:
    bulgaria_area = float(bulgaria.select_one("span.country-area").text)
    logger.debug(f"Bulgaria area: {bulgaria_area}")

    ### get all countries which have area>bulgaria_area:
    bigger_countries = filter(
        lambda c: float(c.select_one("span.country-area").text) > bulgaria_area,
        countries,
    )

    ### get 'country_name', 'capital', 'population' and 'area' for each country
    countries_data = []
    for country in bigger_countries:
        logger.debug(f"process country: {country}")
        country_data = {}

        country_data["name"] = country.select_one(".country-name").text.strip()
        country_data["capital"] = country.select_one(".country-capital").text.strip()
        country_data["population"] = country.select_one(
            ".country-population"
        ).text.strip()
        country_data["area"] = country.select_one(".country-area").text.strip()
        logger.debug(f"country_data: {country_data}")
        countries_data.append(country_data)

    logger.info(f"countries_data: {countries_data}")
    return countries_data


if __name__ == "__main__":
    url = "https://www.scrapethissite.com/pages/simple"
    html = ""

    try:
        # html = get_html(url)
        html = get_html_from_file()
        if not html:
            raise Exception("HTML content can not be empty!")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    countries_data = extract_data(html)
    for country in countries_data:
        print(
            f"name:{country['name']}, capital:{country['capital']}, population:{country['population']}, area:{country['area']}"
        )
