from django.http import HttpResponse
from django.views.generic import View

from account.models import Account


class AccountView(View):
    def get(self, request, *args, **kwargs):
        print(request)
        account = Account.objects.get(name="luke")
        return HttpResponse(account)

    def post(self, request, *args, **kwargs):
        account = Account(name="luke")
        account.save()
        return HttpResponse('This is POST request')
