import requests
from bs4 import BeautifulSoup
import csv
import time
import re

URL = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
BASE = "https://ru.wikipedia.org"

def is_russian_letter(char):
    return re.match(r"[А-ЯЁ]", char.upper()) is not None

def collect_counts():
    counts = {}
    next_link = URL

    while next_link:
        response = requests.get(next_link)
        soup = BeautifulSoup(response.text, "html.parser")

        for li in soup.select(".mw-category li"):
            name = li.text.strip()
            if name:
                first_letter = name[0].upper()
                if is_russian_letter(first_letter):
                    counts[first_letter] = counts.get(first_letter, 0) + 1

        next_page = soup.select_one("a:-soup-contains('Следующая страница')")
        next_link = BASE + next_page["href"] if next_page else None
        time.sleep(0.5)

    return counts


def save_to_csv(data: dict[str, int], filename: str = "beasts.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for letter in sorted(data):
            writer.writerow([letter, data[letter]])


if __name__ == "__main__":
    counts = collect_counts()
    save_to_csv(counts)
