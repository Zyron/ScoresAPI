from rest_framework.serializers import ModelSerializer
from api.models import Highscore


class HighscoreSerializer(ModelSerializer):
    class Meta:
        model = Highscore
