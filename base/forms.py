from django.contrib.auth.forms import UserCreationForm
from .models import User

class customuser(UserCreationForm):
    class meta:
        model = User
        fields = "__all__"