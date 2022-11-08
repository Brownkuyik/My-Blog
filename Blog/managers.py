from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    this is used to create a customize user login profile so that the user can login only with its email
    not with username
    """
    def create_user(self, email, password, **extra_fields):
        """Here is to help save the user created info"""
        if not email:
            raise ValueError('Used a valid email address')
        email = self.normalize_email(email)
        user= self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        '''Here we want to create and save the superuser to also align with the demand of using the email to login not
        username again'''
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault('is_active', True)
       

        if extra_fields.get('is_staff') is not True:
            raise ValueError('You must turn is_staff on before using the sections')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('You must turn super user on before using the sections')
        return self.create_user(email, password, **extra_fields)
        
