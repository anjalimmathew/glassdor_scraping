import json
from scrapfly import ScrapeApiResponse, ScrapeConfig, ScrapflyClient
import pandas as pd 

import re
#import cloudscraper
# client = ScrapflyClient(key="scp-live-250eae03bd25400bab7372436d0431da")

import json
from scrapfly import ScrapeApiResponse, ScrapeConfig, ScrapflyClient

client = ScrapflyClient(key="scp-live-250eae03bd25400bab7372436d0431da")

def find_companies(query: str):
    """find company Glassdoor ID and name by query. e.g. "ebay" will return "eBay" with ID 7853"""
    result = client.scrape(
        ScrapeConfig(
            url=f"https://www.glassdoor.com/searchsuggest/typeahead?numSuggestions=8&source=GD_V2&version=NEW&rf=full&fallback=token&input={query}",
            country="US",
            asp=True,
            cookies={"tldp":"1"},  # sets location to US
        )
    )
    data = json.loads(result.content)
    return data[0]["suggestion"], data[0]["employerId"]


firm_list = pd.read_csv("firms_list.xlsx")
print(firm_list.columns)
firm_list['glassdor_id'] = find_companies['CONAME'].apply()


