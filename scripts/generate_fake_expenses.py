from faker import Faker
import random

fake = Faker()

for _ in range(100):

    print({
        "submitter": fake.name(),
        "amount": round(
            random.uniform(10, 1500),
            2
        ),
        "category": random.choice([
            "Meals",
            "Travel",
            "Office Supplies"
        ]),
        "description": fake.sentence()
    })
