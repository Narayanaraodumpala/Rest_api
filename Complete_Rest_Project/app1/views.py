from django.shortcuts import render
from rest_framework.decorators import api_view
from django.views import View
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import carspaxceserializers,Tyreserializers
from .models import CarspaceModel,TyreModel,Carplan
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.views import APIView


# Create your views here.
@api_view(['GET','POST'])
def function(request):

    return Response({'message':'Hii Welcome To Rest_Framework...'})

@api_view(['GET','POST'])
def first_app(request):
    print(request.query_params)
    number=request.query_params['num']

    print(number)

    new_number=int(number)*2
    print(new_number)
    return Response({'number':number,'new_number result':new_number})


class Carspace(viewsets.ModelViewSet):
      print('gsjb')
      serializer_class=carspaxceserializers
      def get_queryset(self):
          carspace=CarspaceModel.objects.all()
          return carspace

      def create(self, request, *args, **kwargs):
          car_data = request.data
          cars = CarspaceModel.objects.create(car_number=car_data['car_number'],
                                              car_tyres=TyreModel.objects.get(id=car_data['car_tyres']),
                                              car_plan=Carplan.objects.get(id=car_data['car_plan']),
                                              car_name=car_data['car_name'], car_brand=car_data['car_brand'],
                                              description=car_data['description'], production=car_data['production'],
                                              fuel=car_data['fuel']).save()
          serializers = carspaxceserializers(cars)
          return Response(serializers.data)




class Params(viewsets.ViewSet):
       def list(self,request):
           data=CarspaceModel.objects.all()
           cs=carspaxceserializers(data,many=True)
           return Response(cs.data)

       def retrieve(self, request, pk=None):
           try:
               cm = CarspaceModel.objects.get(car_number=pk)
               cs = carspaxceserializers(cm)
               return Response(cs.data)
           except CarspaceModel.DoesNotExist:
               return Response({'error': 'Invalid Car Number'})




class PostData(viewsets.ViewSet):

    def update(self,request,pk=None):
        try:
            cm=CarspaceModel.objects.get(car_number=pk)
            data=request.data
            cs=carspaxceserializers(cm,data,partial=True)
            if cs.is_valid():
                cs.save()
                return Response({'msg':'car updated'})
            else:
                return Response({'error':cs.errors})
        except CarspaceModel.DoesNotExist:
            return Response({'error':'There Is No Car  Available With this Number'})

    def destroy(self,request,pk=None):
        try:
           cm=CarspaceModel.objects.filter(car_number=pk).delete()
           if cm[0]!=0:
             return Response({'msg':'car is deleted'})

        except CarspaceModel.DoesNotExist:
            return Response({'error':'There Is No Car  Available With this Number'})


class Tyres(APIView):
      def post(self,request):
          ts=Tyreserializers(data=request.data)
          if ts.is_valid():
              ts.save()
              message={'message':'tyre is saved'}
          else:
              message={'message':ts.errors}

          return Response(message)

      def get(self,request):
          tm=TyreModel.objects.all()
          ts=Tyreserializers(tm,many=True)
          return  Response(ts.data)



class Get_one_tyre(APIView):

    def get(self, request, product):
        try:
            tm = TyreModel.objects.get(tyre_number=product)
            ts = Tyreserializers(tm)
            return Response(ts.data)
        except TyreModel.DoesNotExist:
            message = {'message': 'invalid tyre number'}
            return Response(message)

class Update_tyres(APIView):

        def put(self, request, product):
            try:
                tm=TyreModel.objects.get(tyre_number=product)
                d1=request.data
                ts=Tyreserializers(tm,d1,partial=True)
                if ts.is_valid():
                  ts.save()
                  message={'message':'tyre is updated'}
                else:
                  message={'error':ts.errors}
                return Response(message)
            except TyreModel.DoesNotExist:
               message={'message':'product is invalid'}
               return Response(message)


        def delete(self,request,product):
            try:
                res=TyreModel.objects.filter(tyre_number=product).delete()
                if res[0]!=0:
                    mssage={'message':'Tyre is deleted'}
                    return Response(mssage)
            except TyreModel.DoesNotExist:
                message={'message':'Invalid tyre number'}
                return Response(message)

