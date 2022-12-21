from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse

from django.contrib.auth import get_user_model

from about_me.models import About


class AboutAPITest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='admin')
        self.user.set_password('admin')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()
        self.about = About.objects.create(desc='test description', chosen=True)

    def test_list_api(self):
        url = reverse('about_me:about_me-list')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['desc'], self.about.desc)

    def test_retrieve_api(self):
        url = reverse('about_me:about_me-detail', args=[self.about.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['desc'], self.about.desc)

    def test_create_api_without_login(self):
        url = reverse('about_me:about_me-list')
        payload = {
            'desc': 'test desc for about 2 ',
            'chosen': True,
        }
        res = self.client.post(url, data=payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_api_with_login(self):
        url = reverse('about_me:about_me-list')
        payload = {
            'desc': 'test desc for about 2 ',
            'chosen': True,
        }
        self.client.force_login(self.user)
        res = self.client.post(url, data=payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(About.objects.all()), 2)
        self.assertEqual(len(About.objects.filter(chosen=True)), 1)

    def test_update_api_without_login(self):
        url = reverse('about_me:about_me-detail', args=[self.about.id])
        payload = {
            'chosen': False
        }
        res = self.client.patch(url, data=payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_api_with_login(self):
        url = reverse('about_me:about_me-detail', args=[self.about.id])
        payload = {
            'chosen': False
        }
        self.client.force_login(self.user)
        res = self.client.patch(url, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertFalse(About.objects.get(id=self.about.id).chosen)

    def test_delete_api_without_login(self):
        url = reverse('about_me:about_me-detail', args=[self.about.id])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_api_with_login(self):
        url = reverse('about_me:about_me-detail', args=[self.about.id])
        self.client.force_login(self.user)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(len(About.objects.all()))
