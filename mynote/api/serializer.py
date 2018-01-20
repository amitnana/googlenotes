from mynote.models import Note
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from django.db.models.fields import DateTimeField

class Noteserializer(ModelSerializer):
    class Meta:
        model = Note
        label = SerializerMethodField()
        fields=[

        'id',

        'title',
        'text',
        'created_date',

         'label'
        ]


    def get_label(self,obj):
        return str(obj.label.labelname)    



class NoteUpdateSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields=[

        'title',
        'text'
        ]



#class PostCreateSerializer(ModelSerializer):
#        model = Post
#        fields=[
#        'text',
#        'title',
#         'author'
#        'created_date'
#        ]
