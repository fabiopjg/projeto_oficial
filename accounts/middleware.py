from django.http import HttpRequest
import re
from django.shortcuts import redirect

from accounts.models import Aluno, Enfermeiro

def verify_register(get_response):
  def middleware(request: HttpRequest):
    routes_clean = [
      '/accounts/register/aluno',
      '/accounts/register/enfermeiro',
      '/admin/'
    ]

    routes = filter(lambda route: re.search(route, request.path), routes_clean)

    if not routes:
      try: 
        if request.user.categoria == 'AL':
          Aluno.objects.get(user=request.user)
      except:
        return redirect('/accounts/register/aluno')

      try: 
        Enfermeiro.objects.get(user=request.user)
      except:
        return redirect('/accounts/register/enfermeiro')

    response = get_response(request)
    return response

  return middleware