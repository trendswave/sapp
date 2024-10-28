from rest_framework import generics, permissions
from .models import QRCode
from .serializers import QRCodeSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
import qrcode
from io import BytesIO
from django.core.files import File

class GenerateQRView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data.get('data')
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        file_name = f'qr_{request.user.username}.png'
        qr_code = QRCode(user=request.user, data=data)
        qr_code.image.save(file_name, File(buffer), save=True)
        qr_code.save()
        return Response(QRCodeSerializer(qr_code).data)

class UserQRCodeListView(generics.ListAPIView):
    serializer_class = QRCodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return QRCode.objects.filter(user=self.request.user)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid Credentials'}, status=400)