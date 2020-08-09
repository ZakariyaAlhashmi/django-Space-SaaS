from .models import Profiles
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics




@api_view(['GET'])
def profile_api(request):
    all_profiles = Profiles.objects.all()
    data = UserSerializer(all_profiles, many=True).data
    return Response({'data':data})

@api_view(['GET'])
def profile_details_api(request,id):
    profile_details = Profiles.objects.get(id=id)
    data = UserSerializer(profile_details).data
    return Response({'data':data})




class ProfileApi(generics.ListAPIView):
    queryset = Profiles.objects.all()
    serializer_class = UserSerializer



class ProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = Profiles.objects.all()
    lookup_field ='id'