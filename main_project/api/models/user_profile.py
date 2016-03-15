import os

from django.contrib.auth.models import User
from django.db import models

from main_project.settings import MEDIA_ROOT


def upload_avatar(instance, filename):
        """ Helper function to upload avatars.
        :param instance: UserProfile instance.
        :param filename: upload filename.
        :return: full upload path.
        """
        username = instance.user.username
        file, extension = os.path.splitext(filename)
        filename = ''.join((username, extension))
        return os.path.join(instance.AVATAR_DIR, filename)


class UserProfile(models.Model):
    """ Model for addition component of User model. This model extensions
    base User model and have One_to_One relation with User.
    """

    _name = 'UserProfile'
    AVATAR_DIR = os.path.join(MEDIA_ROOT, 'avatar')
    DEFAULT_AVATAR_FILE = os.path.join(AVATAR_DIR, 'default.png')

    class Meta:
        db_table = 'user_profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to=upload_avatar,
        default=DEFAULT_AVATAR_FILE)

    def __str__(self):
        return '{0}(user: {1}, avatar: {2})'.format(
            self._name, self.user.username, os.path.basename(str(self.avatar))
        )
