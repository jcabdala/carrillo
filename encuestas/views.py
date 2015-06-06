from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url
from encuestas.forms import  PersonaForm
from django.views.generic.edit import FormView


#    return render_to_response('entrevista.html', {"persona":persona} ,  context_instance=RequestContext(request))
#@login_required
class ContactView(FormView):
    template_name = 'entrevista.html'
    form_class = PersonaForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super(ContactView, self).form_valid(form)
