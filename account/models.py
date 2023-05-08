from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser

#  Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, username, tel, password=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            tel=tel
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, tel, password=None):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            tel=tel
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    
    def create_workeruser(self, email, username, tel, password=None):
        """
        Creates and saves a workeruser with the given email,  and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            tel=tel
        )
        user.worker = True
        user.save(using=self._db)
        return user


    def create_clientuser(self, email, username, tel, password=None):
        """
        Creates and saves a clientuser with the given email,  and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
            tel=tel
        )
        user.client = True
        user.save(using=self._db)
        return user
    
    
    
#  Custom User Model
class User(AbstractBaseUser):


    
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    
    username = models.CharField(max_length=255, unique=True,)
    
    nom = models.CharField(max_length=60, null=True)
    
    tel = models.CharField(max_length=20, unique=True, default="")
    
    prenom = models.CharField(max_length=60, null=True)
    
    adresse = models.CharField(max_length=100, null=True)
    
    datenais = models.DateField(null=True, blank=True)
    
    worker = models.BooleanField(default=False)
    
    client = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    
    is_admin = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['username', 'tel']
    
    def send_message(self, recipients, content):
        from messagerie.models import Message
        message = Message.objects.create(sender=self, content=content)
        message.recipient.add(*recipients)
        return message

    def get_received_messages(self):
        return self.received_messages.all()

    def get_sent_messages(self):
        return self.sent_messages.all()
    

    def __str__(self):
        return f"{self.username} - {self.email}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    @property
    def is_worker(self):
        "Is the user a member of worker?"
        return self.worker
    
    @property
    def is_client(self):
        "Is the user a member of client?"
        return self.client

 