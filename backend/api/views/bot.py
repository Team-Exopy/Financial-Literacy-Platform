# bot/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers import ChatSerializer

class ChatbotView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data.get('message')
            
            # Here you would add your chatbot logic
            # For example, we can create a simple echo bot:
            bot_response = f"You said: {user_message}"
            
            return Response({'response': bot_response}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
