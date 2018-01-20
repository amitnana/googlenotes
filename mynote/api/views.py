from rest_framework.generics import ListAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from mynote.models import Note
from .serializer import Noteserializer,NoteUpdateSerializer
#from .pagination import notespagination
from rest_framework.pagination import (LimitOffsetPagination,PageNumberPagination)




class ListNote(ListAPIView):
    queryset= Note.objects.all()
    serializer_class= Noteserializer
    pagination_class=LimitOffsetPagination#PageNumberPagination


class UpdateNote(UpdateAPIView):
    queryset= Note.objects.all()
    serializer_class= NoteUpdateSerializer


class DeleteNote(DestroyAPIView):
    queryset= Note.objects.all()
    serializer_class= Noteserializer


class CreateNote(CreateAPIView):
    queryset= Note.objects.all()
    serializer_class= Noteserializer
