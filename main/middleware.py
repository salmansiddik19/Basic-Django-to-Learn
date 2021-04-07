class JSONTranslationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.translations = {
            "en": {"greeting": "Hello", "header": "Welcome to Django!"},
            "bn": {"greeting": "হ্যালো", "header": "জ্যাঙ্গোতে স্বাগতম!"},
        }

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        if "bn" in request.META["HTTP_ACCEPT_LANGUAGE"]:
            response.context_data["translations"] = self.translations
            return response
        return response
