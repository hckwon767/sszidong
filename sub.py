import requests

url = "https://subapi.imgki.com/sub?target=clash&url=https%3A%2F%2Fraw.githubusercontent.com%2Fmai19950%2Fclash_config%2Frefs%2Fheads%2Fmain%2Fsub%2Fclash.yaml&insert=false&emoji=true&list=true&tfo=false&scv=true&fdn=false&expand=true&sort=false&new_name=true"
strings_to_replace = ["toshare", "abshare", "ripaojiedian", "mkshare", "tolinkshare", "mksshare"]
replacement_string = "free"
output_filename = "sub.yaml"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    content = response.text
    modified_content = content

    for old_string in strings_to_replace:
        modified_content = modified_content.replace(old_string, replacement_string)

    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(modified_content)

    print(f"Modified content saved to {output_filename}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching URL: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
