from django.urls import path
# from .views import News_list, News_detail
from .views import news_list, news_detail, ContactPageView, tortyuztortPageView, HomePageView, \
    LocalNewsView, ForeignNewsView, TechnologyNewsView, SportNewsView, NewsUpdateView, \
    NewsDeleteView, NewsCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='index_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('404/', tortyuztortPageView, name='404_page'),
    path('local/', LocalNewsView.as_view(), name='local_news_page'),
    path('foreign/', ForeignNewsView.as_view(), name='foreign_news_page'),
    path('technology/', TechnologyNewsView.as_view(), name='technology_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
]



# urlpatterns = [
#     path('all/', News_list.as_view(), name='all_news_list'),
#     path('<int:pk>/', News_detail.as_view(), name='news_detail_page'),
# ]

