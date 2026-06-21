def detect_category_mismatch(
    category: str,
    description: str
):

    description = description.lower()

    rules = {
        "Meals": [
            "restaurant",
            "lunch",
            "dinner",
            "coffee"
        ],
        "Travel": [
            "flight",
            "hotel",
            "conference"
        ],
        "Office Supplies": [
            "paper",
            "printer",
            "office"
        ]
    }

    keywords = rules.get(category, [])

    return not any(
        word in description
        for word in keywords
    )
