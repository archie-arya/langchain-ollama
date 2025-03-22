import os
import requests
import pprint

from async_timeout import timeout
from dotenv import load_dotenv

load_dotenv()

# pprint.pprint(requests.get("https://gist.githubusercontent.com/archie-arya/ef7558bfa280bf140dd6d87315bca456/raw/16db15cec373393d12d84b0dab94dcd3d4ab49c6/eden-marco_linkedin.json").json())


def scrape_linkedin_profile(linkedin_profile_url: str):
    """
    scrape information from LinkedIn profiles, manually scrape te information from the LinkedIn profile
    :param linkedin_profile_url:
    :param mock:
    :return:
    """
    response = requests.get(linkedin_profile_url, timeout=10)
    data = response.json()
    data = {
        k: v
        for k,v in data.items()
        if v not in ([], "", "", None)
        and k not in ["certifications"]
    }

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url= "https://gist.githubusercontent.com/archie-arya/ef7558bfa280bf140dd6d87315bca456/raw/16db15cec373393d12d84b0dab94dcd3d4ab49c6/eden-marco_linkedin.json"

        )
    )
