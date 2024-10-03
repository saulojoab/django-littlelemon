from django.test import TestCase

from restaurant.models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from restaurant.serializers import MenuSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)

class MenuViewTest(APITestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title='Pizza', price=120, inventory=50)
        self.item2 = Menu.objects.create(title='Pasta', price=100, inventory=60)
        self.item3 = Menu.objects.create(title='Salad', price=70, inventory=30)

    def test_getall(self):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(len(items), 3)
        self.assertEqual(serializer.data[0]['title'], 'Pizza')
        self.assertEqual(serializer.data[1]['title'], 'Pasta')
        self.assertEqual(serializer.data[2]['title'], 'Salad')
        