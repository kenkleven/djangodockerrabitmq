from django.test import TestCase
from .models import Reservation

class ReservationModelTest(TestCase):
    def test_create_reservation(self):
        reservation = Reservation.objects.create(
            user_id=1, movie_id=2, theater_id=3, seat_number="A10", time="2025-01-16T18:00:00Z"
        )
        self.assertEqual(reservation.seat_number, "A10")
