class ExpensePolicyServer:

    @staticmethod
    def get_meal_limit():

        return {
            "category": "Meals",
            "max_amount": 100
        }

    @staticmethod
    def get_travel_policy():

        return {
            "hotel_limit": 250,
            "flight_class": "economy"
        }

    @staticmethod
    def lookup_vendor(vendor):

        approved = [
            "Hilton",
            "Marriott",
            "Delta"
        ]

        return {
            "vendor": vendor,
            "approved": vendor in approved
        }
