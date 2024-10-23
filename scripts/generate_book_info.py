import yaml
import glob
import os
import json
import requests

def parse_markdown_with_front_matter(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split YAML front matter and Markdown content
    parts = content.split('---')
    
    if len(parts) < 3:
        raise ValueError("The file does not contain valid front matter")

    yaml_content = parts[1].strip()
    markdown_content = parts[2].strip()

    # Parse YAML
    front_matter = yaml.safe_load(yaml_content)

    return front_matter, markdown_content


# load files from 'content/*.md'
files = glob.glob('content/*.md')
for file in files:
    front_matter, markdown_content = parse_markdown_with_front_matter(file)
    if taxonomies := front_matter.get('extra'):
        if isbn := taxonomies.get('isbn'):
            if os.path.exists(f'book-info/{isbn}.xml'):
                continue
            else:
                # get json data from google books api
                response = requests.get(f'https://www.aladin.co.kr/ttb/api/ItemLookUp.aspx?ttbkey={os.environ["ALADIN_TTB_KEY"]}&itemIdType=ISBN13&ItemId={isbn}&Output=xml')
                response.raise_for_status()
                book_info = response.text
                with open(f'book-info/{isbn}.xml', 'w') as f:
                    f.write(book_info)
                print(f'Saved book info for {isbn}')
