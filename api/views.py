# for django
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError

# for rest_framework
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

# for models
from .models import Product


# for serializer
from .serializers import ProductSerializer, UserSerializer


# Create your views here.

@api_view(['GET'])
def get_products(request):
    all = Product.objects.all()
    serial = ProductSerializer(all, many=True)
    return Response(serial.data)
    # return Response(serial.data)

@api_view(['POST'])
def get_product_category(request):
    try:
        category  = request.data['category']
        if request.method == 'POST':
            products = Product.objects.filter(category=category)
            if category:
                serial = ProductSerializer(products, many=True)
                return Response(serial.data, status=status.HTTP_200_OK)
    except KeyError as e:
        return Response({"msg":f"yohhh, please include {e}"}, status=status.HTTP_412_PRECONDITION_FAILED)

@api_view(['POST'])
def get_product_lone(request):
    try:
        prod = Product.objects.get(pk=request.data['pk'])
        if prod:
            serial = ProductSerializer(prod)
            return Response(serial.data)
    except KeyError as e:
        print(f"error: {e}")
        return Response({"msg":f"please include {e}"})
    except Product.DoesNotExist as e:
        print(f"error: {e}")
        return Response({"msg":f"{e}"})


@authentication_classes([TokenAuthentication])
@permission_classes(IsAuthenticated)
@api_view(['POST'])
def get_user_details(request):
    try:
        token = request.data['token']
        # print("hello")
        if token:
            # print("heloo")
            user_id = Token.objects.get(key=token).user_id
            if user_id:
                user = User.objects.get(id=user_id+2)
                serial = UserSerializer(user)
                return Response(serial.data)
    except KeyError as e:
        return Response({"msg":"please include token in data"})
    except Token.DoesNotExist as e:
        return Response({"msg":f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist as e:
        return Response({"msg":f"{e}"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_user(request):
    try:
        def get(op, req=request):
            return req.data[op]
        data = (get('email'), get('email'), get('password'), get('first_name'), get('last_name'))
        if data:
            username, email, password, first_name, last_name = data
            user = User.objects._create_user(username, email, password, first_name=first_name, last_name=last_name)
            return Response({"msg":"sucessfully created"}, status=status.HTTP_200_OK)
    #   return Response({"msg":"fields is not correct"}, status=status.HTTP_205_RESET_CONTENT)
        return Response(f"yo {email}")
    except IntegrityError as e:
        return Response({"msg":"email already exist"})
    except KeyError as e:
        return Response(
            {
                "msg":"please provide the necessary info",
                "fields": f"{e}"
            }, status=status.HTTP_412_PRECONDITION_FAILED
            )


# username
# email
# password
# first name
# last name


