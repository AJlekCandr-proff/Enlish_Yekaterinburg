from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, mail, password, **extra_fields):
        if not mail:
            raise ValueError('email должен быть указан')

        mail = self.normalize_email(mail)
        user = self.model(mail=mail, **extra_fields)
        user.password = password
        user.save(using=self._db)

        return user

    def create_user(self, mail, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(mail, password, **extra_fields)

    def create_superuser(self, mail, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(mail, password, **extra_fields)
