"""Primary entry point."""

import scraper

div_content = scraper.retrieve_url_endpoint()

scraper.extract_text_from_div(div_content)
