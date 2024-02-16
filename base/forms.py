from django.contrib.auth.forms import UserCreationForm
from .models import User

class Customuser(UserCreationForm):
    class meta:
        form = User
        fields = "__all__"