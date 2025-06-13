from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.utils.timezone import get_current_timezone
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer

class FitnessClassListView(APIView):
    def get(self, request):
        classes = FitnessClass.objects.filter(datetime__gte=timezone.now()).order_by('datetime')
        serializer = FitnessClassSerializer(classes, many=True)
        return Response(serializer.data)

class BookingCreateView(APIView):
    def post(self, request):
        try:
            validate_email(request.data.get('client_email'))
            class_id = request.data.get('class_id')
            fitness_class = FitnessClass.objects.get(id=class_id)
            print(fitness_class.available_slots)

            if fitness_class.available_slots <= 0:
                return Response({'error': 'No available slots'}, status=400)

            serializer = BookingSerializer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                fitness_class.available_slots -= 1
                fitness_class.save()
                return Response({'message': 'Booking successful'}, status=201)
            return Response(serializer.errors, status=400)
        except FitnessClass.DoesNotExist:
            return Response({'error': 'Class not found'}, status=404)
        except ValidationError:
            return Response({'error': 'Invalid email'}, status=400)

class BookingListByEmailView(APIView):
    def get(self, request):
        client_email = request.data.get('client_email')
        if not client_email:
            return Response({'error': 'Email is required'}, status=400)

        bookings = Booking.objects.filter(client_email=client_email)
        data = [
            {
                'class': b.class_id.name,
                'datetime': b.class_id.datetime.astimezone(get_current_timezone()).isoformat(),
                'instructor': b.class_id.instructor,
            }
            for b in bookings
        ]
        return Response(data)
