from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import User_Details,Movie_Details,Movie_Booking
from .serializers import UserRegisterSerializer,MovieSerializer,BookingSerializer,UserLoginSerializer
import json
import hashlib
from faker import factory
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
import requests
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import token_verify
from rest_framework.permissions import IsAuthenticated

# class RegisterAPIView(APIView):
#     serializer_class = UserRegisterSerializer

# def generate_access_token(self,request):
    # print('11111111111111111')
    # serializer = self.serializer_class(data=request.data)
    # if serializer.is_valid():
    #     user = serializer.save()
    #     print('userrrrrrrrrrrrrrr',user)
     # Generate a RefreshToken instance
    # refresh = RefreshToken.for_user(request)
    # print('444444444444',refresh)

    # Set the user data in the refresh token
    # refresh.set_user(request)

    # Generate the access token
    # access_token = str(refresh.access_token)

    # print('77777777777777',access_token)


    # print('111111111111111111111111111111',request)
    # refresh = RefreshToken.for_user(request)
    # print('999999999999',refresh)
    # response_data =  {
    #     'refresh': str(refresh),
    #     'access': str(refresh.access_token),
    #     'user': serializer.data,
    # }
    # print('99999999999999999',response_data)
    # return access_tokens
        
class UserRegisterView(APIView):
    def get(self, request):
        users = User_Details.objects.all()
        serializer = UserRegisterSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data['password']
            # hashed_password = make_password(password)
            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            user = User_Details.objects.create(
                Username=serializer.validated_data['Username'],
                password=hashed_password,
                email_id=serializer.validated_data['email_id'],
                phone=serializer.validated_data['phone'],
            )
            return Response(UserRegisterSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetailedView(APIView):
    # def get_object(self,UserID):
    #     return get_object_v1(self,0 ,UserID)
    def get_object(self, UserID):
        try:
            print("@@@@@@@@@@@@@@@@@@")
            return  User_Details.objects.get(pk=UserID)
        except  User_Details.DoesNotExist:
            return Response({'message': 'No content to show'}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, UserID):
        print("##################")
        user = self.get_object(UserID)
        if user is None:
            return Response({'message': 'User not registered'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserRegisterSerializer(user)
        return Response(serializer.data)

    def put(self, request, UserID):
        user = self.get_object(UserID)
        if user is None:
            return Response({'message': 'User not registered'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserRegisterSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, UserID):
        user = self.get_object(UserID)
        if user is None:
            return Response({'message': 'User not registered'}, status=status.HTTP_404_NOT_FOUND)

        user.delete()
        return Response({'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)
    
from rest_framework_simplejwt.tokens import RefreshToken

# class UserLoginView(APIView):
#     def post(self, request, pk=None):
#         request_object = json.loads(request.body)
#         user = User_Details.objects.filter(UserID=request_object['UserID']).first()

#         if user is not None:
#             if user.password == hashlib.sha256(request_object['password'].encode()).hexdigest():
#                 refresh = RefreshToken.for_user(user)
#                 access_token = str(refresh.access_token)
#                 id=pk
#                 if id is not None:
#                     movie=Movie_Details.objects.filter(MovieID=id)
#                     serializer = MovieSerializer( movie, many=True)
#                     return Response(serializer.data)
#                     movies =  Movie_Details.objects.all()
#                     serializer = MovieSerializer( movies, many=True)
#                     return Response(serializer.data)
#                 else:
#                     return Response({'message': "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
#             return Response({'access_token': access_token}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
# def generate_access_token(request):
  
#     userid = request.data.get('UserID')
#     password = request.data.get('password')
#     print('############################',userid,password)
#     try:
#         user = User_Details.objects.filter(UserID=userid)
#         print('############################',user)
#     except User.DoesNotExist:
#         return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
#     print('144', user)
#     print(user.values(), '145')
#     print(user[0]['password'], '146')
#     if user.check_password(password):
#         refresh = RefreshToken.for_user(user)
#         access_token = str(refresh.access_token)
#         return Response({'access_token': access_token}, status=status.HTTP_200_OK)
#     else:
#         return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
# def generate_access_token(request):
#     request_body= json.loads(request.body)
#     user_data = {
#         'UserID': request.data.get('UserID'),
#         'password': request.data.get('password')
#     }
#     print('000000000',user_data)
#     print('444444444',json.loads(request.body))
#     user = authenticate(request_body, username)
#     print('9999989898', user)
#     if user is None:
#         return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#     refresh = RefreshToken.for_user(user_data)
#     access_token = str(refresh.access_token)
#     print('000000000000000--->',access_token)
#     return Response({'access_token': access_token}, status=status.HTTP_200_OK)

# class UserLoginView(APIView):
#     def post(self, request,pk=None):
#         request_object=json.loads(request.body)
#         user = list(User_Details.objects.filter(UserID=request_object['UserID']).values('UserID','password'))
#         print('11111111111',user)   
#         # user_password = user_details.values('password')
#         if user is not None:
            
#             # if user_password[0]['password'] == request_object['password']:
#             # if check_password(request_object['password'], user.password):
#             # print('passsssssss11',hashlib.sha256(request_object['password'].encode()).hexdigest())
#             # print('passssss2222222',user[0]['password'])
#             if user[0]['password'] == hashlib.sha256(request_object['password'].encode()).hexdigest():
#                 print(user, '184')
#                 user_final = UserLoginSerializer(data=user)
#                 print(user_final)

#                 if user_final.is_valid():

#                 # print(user,"@@@@@@@@@@@@@@@")
#                 # access_token_01= generate_access_token(request)
#                     print('acceeeeeeeeeeeeeeeee')
#                     refresh = RefreshToken.for_user(user_final.validated_data)
#                     print(refresh, '----189------')
#                     access_token = str(refresh.access_token)
#                     print('acccccccccc',access_token)
#                     id=pk
#                     if id is not None:
#                         movie=Movie_Details.objects.filter(MovieID=id)
#                         serializer = MovieSerializer( movie, many=True)
#                         return Response(serializer.data)
#                     movies =  Movie_Details.objects.all()
#                     serializer = MovieSerializer( movies, many=True)
#                     return Response(serializer.data)
#             else:
#                 return Response({'message': "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'message': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)



session=requests.Session()

def login_user(request):
    try:
        request_object=json.loads(request.body)
        access_token= request.headers['Authorization']

        request_data = {
            "token":access_token
        }
        # request.body['token'] = access_token
        is_authenticated = token_verify(request=request)
        print("is_authenticated", is_authenticated.status_code)
        print("is_authenticated", is_authenticated.data)

        url= "http://127.0.0.1:8000/movie/verifytoken/"
        response=session.post(url,headers=request.headers,data=json.dumps(request_data))
 
        # token = access_token
        # url = f'http://127.0.0.1:8000/movie/verifytoken/?token={token}'

        # response = requests.post(url)
        print('responseeeeeeeeeeeeeeee->',response.status_code)
        if response.status_code == 200:
            print('TOKEN IS VALID')
            return JsonResponse({"message":"User login Successfully"},status=status.HTTP_200_OK)
        else:
            print('Token is not valid.')
            return JsonResponse({'message': "Incorrect or else expired token"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return JsonResponse({"error":str(error)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
# def verify_token(token):
#     verify_view = TokenVerifyView()
    
#     request = factory.post('/api/token/verify/', {'token': token})
#     response = verify_view(request)
    
#     return response
    
# def login_user(request):
#     try:
#         request_object = json.loads(request.body)
#         access_token = request.headers['Authorization']

#         response = verify_token(access_token)
        
#         if response.status_code == status.HTTP_200_OK:
#             print('TOKEN IS VALID')
#             return JsonResponse({"message": "User login Successfully"}, status=status.HTTP_200_OK)
#         else:
#             print('Token is not valid.')
#             return JsonResponse({"message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
#     except Exception as error:
#         return JsonResponse({"error": str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserLoginView(APIView):
    def post(self, request):
        try:
            serializer = UserLoginSerializer(data=request.data)       

            if serializer.is_valid():
                username = serializer.validated_data.get("username")
                password = serializer.validated_data.get("password")

                user = authenticate(username=username, password=password)
                print(user,"220")
                if user is not None:
                    print(user,"222")
                    refresh = RefreshToken.for_user(user)
                    return JsonResponse({"refresh":str(refresh),"access":str(refresh.access_token),"message":"Token generated Successfully"},status=status.HTTP_200_OK)
                else:
                    return JsonResponse({'message': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return JsonResponse({"error":str(error)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class MovieListView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAdminUser]
    def get(self, request):
        movies =  Movie_Details.objects.all()
        serializer = MovieSerializer( movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailedView(APIView):
    def get_object(self, MovieID):
        try:
            print("$$$$$$$$$$$$$$$$$$$$$$$$")
            return  Movie_Details.objects.get(pk=MovieID)
        except  Movie_Details.DoesNotExist:
            return Response({'message': 'No content to show'}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, MovieID):
        movie = self.get_object(MovieID)
        print(movie,"#######################")
        # status_code = movie.status_code if movie.status_code else ""
        # print('statusssssssssssss',status_code)
        if movie :
            serializer = MovieSerializer(movie)
            return Response(serializer.data,status=status.HTTP_200_OK)

        # elif movie.status_code and movie.status_code != 200:
        #     print('222222222222222222222')
        #     return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

       

    def put(self, request, MovieID):
        movie = self.get_object(MovieID)
        if movie is None:
            return Response({'message': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, MovieID):
        movie = self.get_object(MovieID)
        if movie is None:
            return Response({'message': 'movie not found'}, status=status.HTTP_404_NOT_FOUND)

        movie.delete()
        return Response({'message': 'movie deleted'}, status=status.HTTP_204_NO_CONTENT)
    

class BookingView(APIView):
    
    def get(self, request):
        book =  Movie_Booking.objects.all()
        print("rdtfyujihgufy")
        serializer = BookingSerializer( book, many=True)
        return Response(serializer.data)

    def post(self, request):
        request_data = request.data
        id = request_data.get('MovieID')
        quantity = request_data.get('Quantity')
        price_movie = request_data.get('Movieprice')
        serializer = BookingSerializer(data=request_data)
        
        if serializer.is_valid():
            user = User_Details.objects.filter(UserID=request_data.get('UserID')).exists()
            movie = Movie_Details.objects.filter(MovieID=id).exists()
            
            if movie:
                if user:
                    get_movie = Movie_Details.objects.get(MovieID=id)
                    calculated_price = int(get_movie.Movieprice) * int(quantity)
                    
                    if calculated_price == int(price_movie):
                        Movie_Booking.objects.create(**serializer.validated_data)
                        return JsonResponse({
                            'message': 'Ticket has been booked'
                        })
                    else:
                        return JsonResponse({
                            'message': 'Inappropriate Amount'
                        })
                else:
                    return JsonResponse({
                        'error': serializer.errors
                    })
            else:
                return JsonResponse({
                    'error': serializer.errors
                })
        else:
            return JsonResponse({
                'error': serializer.errors
            })



class BookingDetailedView(APIView):
    def get_object(self, BookingID):
        try:
            return  Movie_Booking.objects.get(pk=BookingID)
        except  Movie_Booking.DoesNotExist:
            return Response({'message': 'No content to show'}, status=status.HTTP_204_NO_CONTENT)

    def get(self, request, BookingID):
        booking = get_object_or_404(Movie_Booking, pk=BookingID,deleted=False)
        user_data = booking.UserID 
        movie_data = booking.MovieID  

        user_serializer = UserRegisterSerializer(user_data)
        movie_serializer = MovieSerializer(movie_data)

        user={ 
            'Username': user_serializer.data['Username'],
            'email_id': user_serializer.data['email_id'],
            'Moviename': movie_serializer.data["Moviename"],
            'quantity': BookingSerializer(booking).data["Quantity"]
        }
        return Response(user)
    

    def put(self, request, BookingID):
        book = get_object_or_404(Movie_Booking, pk=BookingID,deleted=False)
        request_data = request.data
        id = request_data.get('MovieID')
        quantity = request_data.get('Quantity')
        price_movie = request_data.get('Movieprice')
        if book is None:
            return Response({'message': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BookingSerializer(book, data=request.data)
        if serializer.is_valid():
            get_movie = Movie_Details.objects.get(MovieID=id)
            calculated_price = int(get_movie.Movieprice) * int(quantity)
            if calculated_price == int(price_movie):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response({'message': 'Inappropriate Amount'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

    def delete(self, request,  BookingID):
        booking = get_object_or_404(Movie_Booking, pk=BookingID,deleted=False)
        booking.deleted = True
        booking.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # book = self.get_object( BookingID)
        # if book is None:
        #     return Response({'message': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

        # book.delete()
        # return Response({'message': 'Booking canceled'}, status=status.HTTP_204_NO_CONTENT)

            # def get(self, request,  BookingID):
    #     book = self.get_object( BookingID)
    #     if book is None:
    #         return Response({'message': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

    #     serializer =  BookingSerializer(book)
    #     return Response(serializer.data)

          # def put(self, request,  BookingID):
    #     book = self.get_object( BookingID)
    #     if book is None:
    #         return Response({'message': 'Booking not found'}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = BookingSerializer(book, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)