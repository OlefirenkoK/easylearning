import os

from django.test import TestCase
from django.contrib.auth.models import User

from main_project.settings import MEDIA_ROOT
from api.models.user_profile import UserProfile


class ModelsHelperTestCase(TestCase):

    _user = {'username': 'test1', 'password': 'test1'}

    def setUp(self):
        User.objects.create(**self._user)
        self.user = User.objects.get(username=self._user['username'])

    def test_default_avatar_path(self):
        """Testing default avatar path"""
        avatar_path = os.path.join(MEDIA_ROOT, 'avatar', 'default.png')
        self.assertEqual(UserProfile.DEFAULT_AVATAR_FILE, avatar_path)

    def test_avatar_path_default_upload(self):
        """Test for returned default path of uploaded user avatar"""
        UserProfile.objects.create(user=self.user)
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(user_profile.avatar, user_profile.DEFAULT_AVATAR_FILE)

    def test_avatar_path_upload(self):
        """Test for returned path of uploaded user avatar"""
        avatar_file = os.path.join(os.getcwd(), 'data_helper', 'cat.png')
        UserProfile.objects.create(user=self.user, avatar=avatar_file)
        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(user_profile.avatar, avatar_file)

    def test_user_profile_as_string(self):
        """Test UserProfile as string interpretation"""
        user_profile = UserProfile(user=self.user)
        self.assertEqual(
            str(user_profile),
            '{0}(user: {1}, avatar: {2})'.format(
                user_profile._name,
                self.user.username,
                os.path.basename(str(user_profile.avatar)))
        )
