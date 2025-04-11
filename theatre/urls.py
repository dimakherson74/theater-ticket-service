from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ActorViewSet, GenreViewSet, PlayViewSet,
    TheatreHallViewSet, PerformanceViewSet,
    ReservationViewSet, TicketViewSet
)

router = DefaultRouter()
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("plays", PlayViewSet)
router.register("halls", TheatreHallViewSet)
router.register("performances", PerformanceViewSet)
router.register("reservations", ReservationViewSet)
router.register("tickets", TicketViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
app_name = "theatre"
