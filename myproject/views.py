from django.http import JsonResponse
import json
from .roll import rolls
from .user import users
from .translation import translations


def get_users(request):
    return JsonResponse(users, safe=False)


def login(request):
    if request.method == "GET":
        try:
            data = json.loads(request.GET.get("user", "{}"))
            email = data.get("email")
            password = data.get("password")

            user = next(
                (u for u in users if u["email"] == email and u["password"] == password),
                None,
            )

            if user:
                return JsonResponse(user, status=200)
            else:
                return JsonResponse({"error": "User not found"}, status=404)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)


def get_user_rolls(request):
    if request.method == "GET":
        try:
            roll_ids = request.GET.get("rolls", "[]")
            roll_ids = json.loads(roll_ids)

            found_rolls = [roll for roll in rolls if roll["id"] in roll_ids]

            if not found_rolls:
                return JsonResponse({"error": "Roll not found"}, status=404)

            return JsonResponse(found_rolls, safe=False, status=200)

        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON format in 'rolls' parameter"}, status=400
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)


def get_rolls(request):
    return JsonResponse(rolls, safe=False)


def get_roll(request, roll_id):
    if request.method == "GET":
        roll = next((roll for roll in rolls if roll["id"] == roll_id), None)

        if not roll:
            return JsonResponse({"error": "Roll not found"}, status=404)

        return JsonResponse(roll, status=200)

    return JsonResponse({"error": "Invalid HTTP method"}, status=405)


def get_translations(request):
    return JsonResponse(translations, safe=False)
