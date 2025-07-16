from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _


class CustomTokenAuth(authentication.TokenAuthentication):
   keyword = 'Bearer'

   def authenticate(self, request):

        auth = authentication.get_authorization_header(request).split()
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)
        if len(auth) == 1:
            msg = _('Invalid token header. No credentials provided.')

            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = _('Invalid token header. Token string should not contain spaces.')
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            msg = _('Invalid token header. Token string should not contain invalid characters.')
            raise exceptions.AuthenticationFailed(msg)
        return self.authenticate_credentials(token)