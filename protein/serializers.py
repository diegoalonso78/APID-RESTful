from django.core.serializers.python import Serializer

class ProteinJSONSerializer(Serializer):
    def end_object( self, obj ):
        self.objects.append( self._current )