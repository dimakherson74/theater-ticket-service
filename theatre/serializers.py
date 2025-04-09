from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Actor, Genre, Play, TheatreHall, Performance, Reservation, Ticket

User = get_user_model()


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class PlaySerializer(serializers.ModelSerializer):
    # actors = ActorSerializer(many=True, read_only=True)
    # genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Play
        fields = ["id", "title", "description", "actors", "genres"]

class PlayListSerializer(PlaySerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="full_name"
    )


class PlayDetailSerializer(PlayListSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Play
        fields = ["id", "title", "description", "actors", "genres"]


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ["id", "name", "rows", "seats_in_row"]


class PerformanceSerializer(serializers.ModelSerializer):
    # play = PlayListSerializer(read_only=True)
    # theatre_hall = TheatreHallSerializer(read_only=True)

    class Meta:
        model = Performance
        fields = ["id", "play", "theatre_hall", "show_time"]


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "row", "seat", "performance", "reservation"]


class ReservationSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = ["id", "created_at", "user", "tickets"]
