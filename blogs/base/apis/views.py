# from django.http import JsonResponse
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairViewz

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         # Add custom claims
#         token['username'] = user.username
#         return token

# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
# @api_view(['GET'])
# def  getRoutes(request):
#     routes = [
#         '/api/token',
#         '/api/token/refresh'
#     ]
#     return Response(routes, status=200)


def smartDiv(func):
    def inner(a,b):
        inner.calls += 1
        return func(a,b)
    inner.calls = 0
    print('hello world')
    return inner

@smartDiv

def div(a,b):
    print(a/b)
# print('calls:',div.calls)
for i in range(5):
    print('calls:',div.calls)
    div(i,2)