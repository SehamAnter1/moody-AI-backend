



from voice.views import VoiceAssistantView
from django.urls import path

urlpatterns = [
    path('assistant/', VoiceAssistantView.as_view(), name='voice-assistant'),   

]