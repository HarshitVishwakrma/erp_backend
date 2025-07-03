from rest_framework.routers import DefaultRouter
from .views import OnwardChallanViewSet
from django.urls import path
from .views import generate_unique_challan_number
from .views import deletechallan 
from .views import transportdetailsview
from .views import deletetransportdetails
from .views import edittransportdetails
from .views import vehicaldetailsview 
from .views import deletevehicaldetails 
from .views import editvehicaldetails
from .views import purchaseview
from .views import inwardchallanview
from .views import outwardchallanview
from .import views
router = DefaultRouter()
router.register(r'onwardchallan', OnwardChallanViewSet)
router.register(r'transportdetails', transportdetailsview)
router.register(r'vehicaldetails', vehicaldetailsview)
router.register(r'outwardchallan',outwardchallanview)

urlpatterns=router.urls+[
    path("generate-challan-no/", generate_unique_challan_number.as_view(), name='generate-challan-no'),
   path("deletechallan/<int:id>/",deletechallan.as_view(), name="deletechallan"),
   path("deletetransportdetails/<str:name>/",deletetransportdetails.as_view() , name="deletetransportdetails"),
   path("edittransportdetails/<str:name>/",edittransportdetails.as_view(), name='edittransportdetails'),
   path('deletevehicaldetails/<str:name>',deletevehicaldetails.as_view(),name='deletevehicaldetails'),
   path('editvehicaldetails/<str:vehical_no>', editvehicaldetails.as_view(), name='editvehicaldetails'),
   path('purchaseview/',purchaseview.as_view(),name='purchaseview'),
   path('inwardchallanview/',inwardchallanview.as_view(),name='inwardchallanview'),
#    /sales/inwardchallanview/?supplier=SUPPLIER_NAME
#    path('inward/', views.inward, name='inward'),
]
