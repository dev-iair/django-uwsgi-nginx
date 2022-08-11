from django.http import JsonResponse
from django.views.generic.base import TemplateView, View
from django.contrib.auth import login, logout
from django.shortcuts import redirect
import models as web_model
from django.utils import timezone
import json

class LoginView(TemplateView):
    template_name="login.html"

    def get(self, request, *args, **kwargs):
        context = {}
        if(request.user.is_authenticated):
            return redirect(to="/main")
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = {}
        context['check_pw'] = 1
        id = request.POST['id']
        pw = request.POST['pwd']
        try:
            user = web_model.User.objects.get(id=id)
            if user is not None:
                if user.check_password(pw):
                    login(request, user)
                    return redirect(to="/main")
                else:
                    context['check_pw'] = 0
        except:
            context['check_pw'] = 0
        return self.render_to_response(context)

class UserModifyView(View):

    def post(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            context = {}
            user_id = request.user.id
            get_data = json.loads(request.body)
            mod_pw = get_data['pw']
            try:
                mod_user = web_model.User.objects.get(id=user_id)
                mod_user.set_password(mod_pw)
                mod_user.mod_date = timezone.now()
                mod_user.save()
                context['result'] = 1
                return JsonResponse(context)
            except:
                context['result'] = 0
                return JsonResponse(context)
        else:
            context['result'] = 0
            return JsonResponse(context)

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(to="/")