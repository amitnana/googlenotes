from mynote.models import Note,Label
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from django.db.models.fields import DateTimeField

class Noteserializer(ModelSerializer):
    class Meta:
        model = Label
        label = SerializerMethodField()
        fields=[

        'id',

        'label',


        'created_date'


        ]

        



class NoteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Label
        fields=[

        'label'
        ]
