import requests
from datetime import datetime

def get_latest_archive_url(url: str) -> str:
    return f'https://web.archive.org/web/{generate_current_timestamp()}/{url}'

def generate_current_timestamp() -> str:
    return datetime.now().strftime('%Y%m%d%H%M%S')

# Example usage
if __name__ == '__main__':
    example1 = "https://www.economist.com/science-and-technology/2024/03/30/could-weight-loss-drugs-eat-the-world"
    example2 = 'https://www.washingtonpost.com/wellness/2024/04/03/diet-culture-nutrition-influencers-general-mills-processed-food/'

    out1 = get_latest_archive_url(example1)
    out2 = get_latest_archive_url(example2)
    print(f'Example 1 output: {out1}')
    print(f'Example 2 output: {out2}')
