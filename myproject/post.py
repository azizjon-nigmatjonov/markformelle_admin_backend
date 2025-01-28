from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
import json
from .roll import rolls
from .user import users
from .translation import translations


@csrf_exempt
def add_roll(request):
    """Handles POST requests to add a new roll."""
    if request.method == "POST":
        try:
            body = json.loads(request.body)

            if "name" not in body:
                return JsonResponse({"error": "Roll has no 'name' field!"}, status=400)

            rolls.insert(0, body)
            return JsonResponse(body, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)


@csrf_exempt
def update_roll(request, roll_id):
    if request.method == "PUT":
        try:
            # Find the roll by ID
            roll_index = next(
                (i for i, roll in enumerate(rolls) if roll["id"] == roll_id), -1
            )

            if roll_index == -1:
                return JsonResponse({"error": "Roll not found"}, status=404)

            # Parse the updated data from the request body
            updated_data = json.loads(request.body)

            # Update the roll at the found index
            rolls[roll_index] = updated_data

            # Return the updated roll as a response
            return JsonResponse(rolls[roll_index], status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)


@csrf_exempt
def update_user(request, user_id):
    if request.method == "PUT":
        try:
            # Find the roll by ID

            print(111, int(user_id))
            user_index = next(
                (i for i, user in enumerate(users) if user["id"] == int(user_id)), -1
            )

            if user_index == -1:
                return JsonResponse({"error": "User not found"}, status=404)

            # Parse the updated data from the request body
            updated_data = json.loads(request.body)
            # Update the roll at the found index
            users[user_index] = updated_data

            # Return the updated roll as a response
            return JsonResponse(users[user_index], status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)


@csrf_exempt
def add_user(request):
    """Handles POST requests to add a new roll."""
    if request.method == "POST":
        try:
            body = json.loads(request.body)

            if "name" not in body:
                return JsonResponse({"error": "Roll has no 'name' field!"}, status=400)

            users.insert(0, body)
            return JsonResponse(body, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)


@csrf_exempt
def add_translations(request):
    if request.method == "POST":
        try:
            # Parse the request body
            new_translation = json.loads(request.body)

            # Reset the translations for each language
            translations["ru"] = {}
            translations["uz"] = {}
            translations["en"] = {}

            # Populate the translations dictionary
            for el in new_translation:
                if "key" in el:
                    translations["ru"][el["key"]] = el.get("ru", "")
                    translations["en"][el["key"]] = el.get("en", "")
                    translations["uz"][el["key"]] = el.get("uz", "")

            # Return the new translations list as a response
            return JsonResponse(new_translation, safe=False, status=201)

        except json.JSONDecodeError:
            # Handle invalid JSON
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    # Handle invalid HTTP methods
    return JsonResponse({"error": "Invalid HTTP method"}, status=405)
