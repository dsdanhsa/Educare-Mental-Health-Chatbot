from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .apps import ChatbotConfig
from .utils import chatbot_response
import logging

logger = logging.getLogger('chatbot_logger')

def home(request):
    """
    Render trang chủ của chatbot.
    """
    return render(request, "index.html")

@csrf_exempt
def get_bot_response(request):
    """
    Xử lý yêu cầu từ người dùng và trả về phản hồi từ chatbot.
    """
    if request.method == "GET":
        user_text = request.GET.get('msg', '')
    elif request.method == "POST":
        user_text = request.POST.get('msg', '')
    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)

    logger.info(f"User input: {user_text}")

    # Sử dụng các thuộc tính tĩnh của ChatbotConfig để lấy model và các dữ liệu khác
    chatbot_response_text = chatbot_response(user_text, ChatbotConfig)
    logger.info(f"Bot response: {chatbot_response_text}")

    return JsonResponse({"response": chatbot_response_text})
