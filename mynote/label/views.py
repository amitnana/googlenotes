from rest_framework.generics import ListAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from mynote.models import Note,Label
from .serializer import Noteserializer,NoteUpdateSerializer





class ListLabel(ListAPIView):
    queryset= Label.objects.all()
    serializer_class= Noteserializer




class UpdateLabel(UpdateAPIView):
    queryset= Label.objects.all()
    serializer_class= NoteUpdateSerializer
    lookup_field='label'

class DeleteLabel(DestroyAPIView):
    queryset= Label.objects.all()
    serializer_class= Noteserializer


class CreateLabel(CreateAPIView):
    queryset= Label.objects.all()
    serializer_class= Noteserializer
