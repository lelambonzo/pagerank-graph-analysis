import networkx as nx
import os
from bs4 import BeautifulSoup

# Function to parse HTML files and extract links
def parse_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        return links

# Function to compute PageRank for interconnected HTML pages
def simple_pagerank(directory: str) -> dict:
    graph = nx.DiGraph()

    # Iterate through HTML files in the directory
    for file_name in os.listdir(directory):
        if file_name.endswith('.html'):
            file_path = os.path.join(directory, file_name)
            graph.add_node(file_name)

            # Parse HTML and add edges based on links
            links = parse_html(file_path)
            for link in links:
                if link.endswith('.html') and link in os.listdir(directory):
                    graph.add_edge(file_name, link)

    # Calculate PageRank
    page_ranks = nx.pagerank(graph)

    return page_ranks

# Compute PageRank for the HTML pages in 'html_pages' directory
pageranks = simple_pagerank('html_pages')
print("PageRank Scores:")
for page, score in pageranks.items():
    print(f"{page}: {score:.4f}")
