from django.core.serializers.python import Serializer

class InteractionsJSONSerializer(Serializer):
    def end_object( self, obj ):
        self.objects.append( self._current )