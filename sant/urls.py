
from django.urls import path,include
from sant import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path("", views.sant_login , name='login'),
    path("AfterLogin", views.AfterLogin,name='AfterLogin'),
    path("logout/",views.sant_logout,name='logout'),
    path("Dashboard/santkrupa-invoice/<int:id>",views.santkrupa_invoice, name='santkrupa_invoice'),
    path("Dashboard/",views.dashboard, name='dashboard'),
    path("Dashboard/AddCustomer/",views.addcustomer, name='addcustomer'),
    path('loadajax/',views.loaddata,name="loaddata"),
    path('Generate-invoice/',views.download_pdf_view,name="generate_invoice"),
    path('View-invoice/',views.pdf_view,name="ginvoice"),
    path('Invoice-List/<int:id>',views.santkrupa_list,name="santkrupa_list"),
    path('Invoice/<int:id>/',views.santkrupa_list_view,name="santkrupa_list_view"),
    path('delete/<int:id>/',views.delete_customer,name="customerdelete"),
    path('santkrupa_delete/<int:id>/',views.santkrupa_delete,name="santkrupa_delete"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)