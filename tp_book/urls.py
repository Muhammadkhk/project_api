from django.urls import path
#from jmespath import search
from tp_book.views import GetAllData,PostModelData#,CustomPagination,UpdateData,FilterData,SearchData,DeleteData,allApi
urlpatterns = [
    path('all-data/<int:pk>', GetAllData.as_view()),
    path('post-data', PostModelData.as_view()),
    #path('post-data', PostModelData.as_view()),
    # path('filter-data/<int:pk>', FilterData.as_view()),
    # path('update-data/<int:pk>', UpdateData.as_view()),
    # path('search/', SearchData.as_view()),
    # path('delete/<int:pk>', DeleteData.as_view()),
    # path('all-data-data', allApi),
    ]