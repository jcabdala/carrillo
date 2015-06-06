from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url
from encuestas.forms import  Persona

@login_required
def encuesta(request):
    persona = Persona()

    if request.method == 'POST':
        persona = Persona(request.POST)
    return render(request, 'entrevista.html', {"persona":persona})
#    return render_to_response('entrevista.html', {"persona":persona} ,  context_instance=RequestContext(request))

