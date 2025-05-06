from django.test import TestCase, Client
from django.urls import reverse
from .models import ClothingItem
import json

class OutfitMatcherTests(TestCase):
    def setUp(self):
        self.client = Client()
        # Create test clothing items
        self.shirt = ClothingItem.objects.create(
            item_type='shirt', color='blue', style='casual'
        )
        self.pants = ClothingItem.objects.create(
            item_type='pants', color='black', style='casual'
        )
    
    def test_outfit_matcher_get(self):
        response = self.client.get(reverse('outfit_matcher'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'outfit_matcher.html')
        self.assertIn('clothing_items', response.context)
    
    def test_outfit_matcher_post_valid(self):
        data = {'item_id': self.shirt.id}
        response = self.client.post(
            reverse('outfit_matcher'),
            json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn('selected_item', response_data)
        self.assertIn('matches', response_data)
        self.assertEqual(response_data['selected_item']['type'], 'shirt')
    
    def test_outfit_matcher_post_invalid_id(self):
        data = {'item_id': 999}
        response = self.client.post(
            reverse('outfit_matcher'),
            json.dumps(data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json())