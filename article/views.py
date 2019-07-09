from django.shortcuts import render

# Create your views here.
from .models import Navigation,Contents,Types,Blogs
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xblog.settings")# project_name 项目名称
django.setup()


import markdown
from django.shortcuts import render_to_response, get_object_or_404


def index(request,nav_id='1',con_id='1',blog_pk='1'):  # 博客内容
    context = {}
    context['navigation'] = Navigation.objects.all()
    context['contents'] = Contents.objects.filter(nav=nav_id)
    context['types'] = Types.objects.filter(con=con_id).filter(nav=nav_id)
    context['blogs'] = Blogs.objects.values("id","nav","con","ty","name").filter(nav=nav_id)
    Blogs.objects.get_or_create(id=1)
    context['blog'] = Blogs.objects.get(id=blog_pk)
    if context['blog']:
        context['blog'].content = markdown.markdown(context['blog'].content,
                                                    extensions=[
                                                        'markdown.extensions.extra',
                                                        'markdown.extensions.codehilite',
                                                        'markdown.extensions.toc',],safe_mode=True,enable_attributes=False)
    response = render_to_response("index.html", context)
    return response


def index_blog(request,nav_id='1',con_id='1',blog_pk='1'):  # 博客内容
    context = {}
    context['navigation'] = Navigation.objects.all()
    context['contents'] = Contents.objects.filter(nav=nav_id)
    context['types'] = Types.objects.filter(con=con_id)
    context['blogs'] = Blogs.objects.values("id","nav","con","ty","name")
    context['blog'] = Blogs.objects.get(id=blog_pk)
    if context['blog']:
        context['blog'].content = markdown.markdown(context['blog'].content,
                                                    extensions=[
                                                        'markdown.extensions.extra',
                                                        'markdown.extensions.codehilite',
                                                        'markdown.extensions.toc',],safe_mode=True,enable_attributes=False)
    response = render_to_response("index.html", context)
    return response
