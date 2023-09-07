from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import News, Category
from django.views.generic import TemplateView, DetailView, ListView
from .forms import ContactForm








# class News_list(ListView):
#     model = News
#     template_name = 'news_list.html'

def news_list(request):
    # news_list = News.objects.filter(status=News.Status.Published)
    news_list = News.published.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'news_list.html', context)









# class News_detail(DetailView):
#     model = News
#     template_name = 'news_detail.html'

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news_detail.html', context)






# def homePageView(request):
#     categories = Category.objects.all()
#     news_list = News.published.all().order_by('-publish_time')[:4]
#     local_one = News.published.filter(category__name='Mahalliy').order_by("-publish_time")[0:1]
#     local_news = News.published.all().filter(category__name='Mahalliy').order_by("-publish_time")[1:4]
#     context = {
#         'news_list': news_list,
#         'categories': categories,
#         'local_one': local_one,
#         'local_news': local_news
#     }
#
#     return render(request, 'index.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:4]
        context['mahalliy_habarlar'] = News.published.all().filter(category__name='Mahalliy').order_by("-publish_time")[:4]
        context['horij_habarlar'] = News.published.all().filter(category__name='Horij').order_by("-publish_time")[:4]
        context['sport_habarlar'] = News.published.all().filter(category__name='Sport').order_by("-publish_time")[:4]
        context['tehnalogiya_habarlar'] = News.published.all().filter(category__name='Tehnalogiya').order_by("-publish_time")[:4]

        return context












# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Biz bilan bog'langaningiz uchun tashakkur! </h2>")
#     context = {
#         'form': form
#     }
#     return render(request, 'contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h4> Biz bn bog'langaningiz uchun tashakkur! </h4>")
        context = {
            "form": form
        }

        return render(request, "contact.html", context)













def tortyuztortPageView(request):
    context = {

    }
    return render(request, '404.html', context)











class LocalNewsView(ListView):
    model = News
    template_name = 'mahalliy.html'
    context_object_name = 'mahalliy_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Mahalliy')
        return news




class ForeignNewsView(ListView):
    model = News
    template_name = 'horij.html'
    context_object_name = 'horij_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Horij')
        return news







class TechnologyNewsView(ListView):
    model = News
    template_name = 'tehnologiya.html'
    context_object_name = 'tehnologiya_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Tehnalogiya')
        return news


class SportNewsView(ListView):
    model = News
    template_name = 'sport.html'
    context_object_name = 'sport_yangiliklar'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news
