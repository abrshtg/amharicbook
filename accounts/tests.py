from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):
    def test_create_user(self):
        # get a model
        User = get_user_model()

        # creat a user.
        user = User.objects.create_user(email='ab@email.com', username='ab', password='test123')
        
        # now test the created user is created properly.
        self.assertEqual(user.email, 'ab@email.com') # is email correct
        self.assertEqual(user.username, 'ab') # is username is correct
        self.assertTrue(user.is_active) # is user active
        self.assertFalse(user.is_staff) # is user not a staff
        self.assertFalse(user.is_superuser) # is user not a superuser

    def test_create_superuser(self):
        User = get_user_model() 

        admin_user = User.objects.create_superuser(email='admin@email.com', username='admin', password='test123')
        
        self.assertEqual(admin_user.email, 'admin@email.com')
        self.assertEqual(admin_user.username, 'admin')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser) 
