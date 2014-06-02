from django.test import TestCase

# Create your tests here.
from mock_token.models import *
d = DataverseToken.objects.all()[0]
d.has_token_expired()
d.refresh_token()

