from django.http import JsonResponse

def fetch_reviews(request, dealer_id):
    # Example static response (replace with your actual logic if needed)
    reviews = {
        "dealerId": str(dealer_id),
        "reviews": [
            {
                "name": "John Smith",
                "review": "Great service and friendly staff!",
                "purchase": True,
                "purchase_date": "2023-05-15",
                "car_make": "Toyota",
                "car_model": "Camry",
                "car_year": 2022
            }
        ]
    }
    return JsonResponse(reviews)
