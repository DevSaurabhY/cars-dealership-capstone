def fetch_dealers_by_state(request, state):
    if state.lower() == "kansas":
        dealers = [
            {
                "id": 1,
                "full_name": "Best Cars Dealership",
                "city": "Wichita",
                "state": "KS",
                "address": "123 Main St",
                "zip": "67202"
            },
            {
                "id": 2,
                "full_name": "Super Autos",
                "city": "Topeka",
                "state": "KS",
                "address": "456 Oak Ave",
                "zip": "66603"
            }
        ]
    else:
        dealers = []

    return JsonResponse(dealers, safe=False)
