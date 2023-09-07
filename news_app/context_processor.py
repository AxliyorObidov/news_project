from .models import News, Category

def latest_new(request):
    latest_new = News.published.all().order_by("-publish_time")[:10]
    category = Category.objects.all()

    context = {
        'latest_new': latest_new,
        'category': category
    }
    return context

