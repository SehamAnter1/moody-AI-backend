
# # Create your views here.
# import os
# from rest_framework.views import APIView
# from rest_framework.response import Response
# import tempfile
# from .services import transcribe, generate_reply, text_to_speech


# class VoiceAssistantView(APIView):

#     def post(self, request):
#         audio = request.FILES.get("audio")

#         if not audio:
#             return Response({"error": "No audio provided"}, status=400)

#         # save file
#         temp_dir = tempfile.gettempdir()
#         file_path = os.path.join(temp_dir, audio.name)
#         with open(file_path, "wb+") as f:
#             for chunk in audio.chunks():
#                 f.write(chunk)

#         # 1. speech → text
#         text = transcribe(file_path)

#         # 2. generate reply
#         reply = generate_reply(text)

#         # 3. text → speech
#         voice_file = text_to_speech(reply)

#         # cleanup
#         os.remove(file_path)

#         return Response({
#             "transcript": text,
#             "reply": reply,
#             "voice_url": voice_file
#         })