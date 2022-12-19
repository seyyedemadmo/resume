from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.reverse import reverse

from django.contrib.auth import get_user_model

from ability.models import Ability


class AbilityAPITest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='test_admin')
        self.user.set_password("admin")
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.save()
        self.test_ability = Ability.objects.create(title='test', percent=80, desc='test test')

    def test_list_ability(self):
        """
        test list api with no login
        """
        url = reverse("ability:ability-list")
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), len(Ability.objects.all()))

    def test_retrieve_ability_with_login(self):
        """
        test for retrieve ability for admin user
        """
        url = reverse('ability:ability-detail', args=[self.test_ability.id])
        self.client.force_login(self.user)
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['id'], self.test_ability.id)
        self.assertEqual(res.data['title'], self.test_ability.title)
        self.assertEqual(res.data['desc'], self.test_ability.desc)
        self.assertEqual(res.data['percent'], self.test_ability.percent)

    def test_retrieve_ability_without_login(self):
        """
        test for retrieve ability for other user
        """
        url = reverse('ability:ability-detail', args=[self.test_ability.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_ability_without_login(self):
        url = reverse('ability:ability-list')
        payload = {
            "title": "second ability test",
            'desc': 'test description',
            'percent': 80
        }
        res = self.client.post(url, data=payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_ability_with_login(self):
        url = reverse('ability:ability-list')
        payload = {
            "title": "second ability test",
            'desc': 'test description',
            'percent': 80
        }
        self.client.force_login(self.user)
        len_before_create = len(Ability.objects.all())
        res = self.client.post(url, data=payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(Ability.objects.all()), len_before_create + 1)

    def test_update_ability_without_login(self):
        url = reverse('ability:ability-detail', args=[self.test_ability.id])
        payload = {
            'title': 'new test'
        }
        res = self.client.put(url, data=payload)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_ability_with_login(self):
        url = reverse('ability:ability-detail', args=[self.test_ability.id])
        payload = {
            'title': 'new test'
        }
        self.client.force_login(self.user)
        res = self.client.patch(url, data=payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Ability.objects.get(id=res.data['id']).title, 'new test')

    def test_delete_ability_without_login(self):
        url = reverse('ability:ability-detail', args=[self.test_ability.id])
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_ability_with_login(self):
        url = reverse('ability:ability-detail', args=[self.test_ability.id])
        self.client.force_login(self.user)
        res = self.client.delete(url)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(Ability.objects.filter(visible=True)), 0)
