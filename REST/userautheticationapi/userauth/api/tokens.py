from rest_framework_simplejwt.tokens import RefreshToken, Token

class CustomRefreshToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        token =  super().for_user(user)
        token['id'] = user.id

        return token