import requests
import logging

# Configure basic logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

url = "https://subapi.imgki.com/sub?target=clash&url=https%3A%2F%2Fraw.githubusercontent.com%2Fmai19950%2Fclash_config%2Frefs%2Fheads%2Fmain%2Fsub%2Fclash.yaml&insert=false&emoji=true&list=true&tfo=false&scv=true&fdn=false&expand=true&sort=false&new_name=true"
filter_strings = ["abshare", "toshare", "ripaojiedian", "mkshare", "tolinkshare", "mksshare", " ss"]

try:
    response = requests.get(url)
    response.raise_for_status()

    filtered_lines = [line for line in response.text.splitlines() if not any(filter_str in line for filter_str in filter_strings)]

    with open('sub.yaml', 'w') as f:
        for line in filtered_lines:
            f.write(line + '\n')

except requests.exceptions.ConnectionError as e:
    logging.error(f"Connection error occurred: {e}")
except requests.exceptions.Timeout as e:
    logging.error(f"Request timed out: {e}")
except requests.exceptions.HTTPError as e:
    logging.error(f"HTTP error occurred: {e}")
except requests.exceptions.RequestException as e:
    logging.error(f"An unexpected error occurred: {e}")
