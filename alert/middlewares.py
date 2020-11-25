from rest_framework.authtoken.models import Token
from channels.db import database_sync_to_async

class SimpleMiddlware:

    def __init__(self,res):
        self.res = res

    def __call__(self,request):

        response = self.res(request)
        return response

@database_sync_to_async
def get_user(token_key):
    try:
        token = Token.objects.get(key=token_key)
        user = token.user
        #return user.username, user.id
        return user
    except Token.DonesNotExist:
        return None

class TokenAuthMiddleware:

    def __init__(self,app):
        self.app = app

    async def __call__(self, scope, receive, send):

        token = scope['query_string'].decode("utf-8")
        print(token)

        if token:
            token_name, token_key = token.split('_')
            print(token_name)
            print(token_key)
            scope['user'] = "test"
            if token_name == 'Token':
                user = await get_user(token_key)
                scope['user'] = user

        return await self.app(scope, receive, send)