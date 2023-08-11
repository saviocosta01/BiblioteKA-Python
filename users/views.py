from rest_framework import generics
from users.models import UserModel
from users.serializers import SendEmailSerializer, UserSerializer, RetrieveLendingUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView, Request, Response
from django.core.mail import send_mail
from django.conf import settings
from .permissions import IsAccountOwner, UserAccountOwner
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated


class UserView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        operation_id="users_get",
        description="Rota para listar todos os usuários",
        summary="Listar usuários",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="users_post",
        description="Rota para cadastrar um estudante ou colaborador da biblioteca",
        summary="Cadastro de usuários",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "pk"

    @extend_schema(
        operation_id="user_get",
        description="Rota para listar apenas um usuário",
        summary="Listar usuários, sendo que se for estudante, só podera listar sua própria conta, e colaborador podera listar qualquer uma",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_patch",
        description="Rota para atualizar usuário",
        summary="Rota para atualizar dados do usuário, não sendo possivel atualizar a caregoria entre colaborador e estudante",
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @extend_schema(
        operation_id="user_delete",
        description="Rota para deletar usuário",
        summary="Rota para excluir um usuário, se o usuário não for admin só poderá excluir sua própria conta",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(exclude=True)
    def put(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class UsersLendingsHistory(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = UserModel.objects.all()
    serializer_class = RetrieveLendingUser
    permission_classes = [IsAdminUser]

    @extend_schema(
        operation_id="user_lendings_get",
        description="Rota para listar histórico de emprestimos dos usuários",
        summary="Listar todos os usuários com seus respectivos históricos de emprestimos, somente admin tem acesso a essa rota",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UsersLendingsHistoryDetails(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = UserModel.objects.all()
    serializer_class = RetrieveLendingUser
    permission_classes = [UserAccountOwner]
    lookup_url_kwarg = "pk"

    @extend_schema(
        operation_id="user_lending_get",
        description="Rota para listar histórico de emprestimos do usuário",
        summary="Listar usuário com seu histórico de emprestimo, somente o dono da conta tem acesso a sua pagina",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SendEmailView(APIView):
    def post(self, req: Request) -> Response:
        serializer = SendEmailSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)

        send_mail(
            **serializer.validated_data,
            from_email=settings.EMAIL_HOST_USER,
            fail_silently=False
        )
        return Response({"message": "E-mails enviados"})

    @extend_schema(exclude=True)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="email_post",
        description="Rota para enviar e-mails",
        summary="Enviar e-mails",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class Login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    @extend_schema(
        operation_id="user_login",
        description="Rota para login",
        summary="Fazer login do usuário",
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


# create
