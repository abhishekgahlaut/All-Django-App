from django.shortcuts import render
from django.http import HttpResponseRedirect

#from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
#from django.template import RequestContext
# Create your views here.

def index(request):
  return HttpResponseRedirect('login')

@login_required
def logged_in(request):
    context = {}
    # list1 = []
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # get_records = ProductImage.objects.all()
    # if get_records:
    #     for val in get_records:
    #         image_prod = str(val.product_image).split('polls',1)[1]
    #         list1.append(image_prod)
    #     context = {'latest_question_list': latest_question_list, 'all_images':list1}
    # else:
    #     pass  
    return render(request, 'djangologin/logged_in.html', context)
