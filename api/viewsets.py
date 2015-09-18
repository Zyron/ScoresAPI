from rest_framework.viewsets import ModelViewSet
from api.serializers import HighscoreSerializer
from api.models import Highscore


class HighscoresViewSet(ModelViewSet):
    queryset = Highscore.objects.all()
    serializer_class = HighscoreSerializer