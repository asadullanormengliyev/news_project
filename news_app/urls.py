from django.urls import path
from .views import (news_list, news_detail,
                    homePageView, ContactPageView,
                    aboutPageView, HomePageView,
                    LocalNewsView, ForeignNewsView,
                    TechnologyNewsView, SportNewsView,
                    NewsDeleteView, NewsUpdateView,
                    NewsCreateView
)

urlpatterns=[
    path('',  HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name="all_news_list"),
    path('<slug:news>/', news_detail, name='news_detail_page'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('about/', aboutPageView, name='about_page'),
    path('news/local/', LocalNewsView.as_view(), name='local_news_page'),
    path('news/foreign/', ForeignNewsView.as_view(), name='foreign_news_page'),
    path('news/technology/', TechnologyNewsView.as_view(), name='technology_news_page'),
    path('news/sport/', SportNewsView.as_view(), name='sport_news_page')
]

