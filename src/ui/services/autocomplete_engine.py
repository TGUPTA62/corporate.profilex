import difflib
from rapidfuzz import process, fuzz
import json
import os


# Load list from JSON or DB
def load_company_list():
    file_path = os.path.join(
        os.path.dirname(__file__),
        "../../data/company_list.json",
    )
    with open(file_path, "r") as f:
        return json.load(f)


COMPANY_LIST = load_company_list()


def get_suggestions(query: str):
    if not query:
        return []

    query = query.strip()

    # Fuzzy match
    fuzzy_results = process.extract(
        query,
        COMPANY_LIST,
        scorer=fuzz.WRatio,
        limit=5,
    )
    fuzzy_suggestions = [name for name, score, _ in fuzzy_results if score > 50]

    # Spell correction
    spell_suggestions = difflib.get_close_matches(query, COMPANY_LIST, n=3, cutoff=0.5)

    # Merge & unique
    final_list = list(dict.fromkeys(fuzzy_suggestions + spell_suggestions))
    return final_list
