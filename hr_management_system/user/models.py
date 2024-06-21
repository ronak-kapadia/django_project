from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from device.models import Device
from department.models import Department
from office.models import Office

ROLE_CHOICES = (
    ('hr', 'hr'),
    ('employee', 'employee'),
    ('employer', 'employer'),
)

class UserManager(BaseUserManager):

    def create_user(self,email,password=None, **extra_fields):
        if not email:
            return "Please provide email"
        
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None, **extra_fields) :
        user =self.create_user(email,password=password)
        
        user.is_admin=True
        user.role= 'employee'
        user.save(using=self._db)
        return user






class User(AbstractBaseUser):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    phone=models.IntegerField(null=True)
    email=models.EmailField(unique=True)
    code=models.IntegerField(unique=True,)
    address=models.CharField(max_length=200)
    role = models.CharField(max_length=200,choices=ROLE_CHOICES,default='employee')
    
    
    device=models.ForeignKey(Device, on_delete=models.CASCADE,null=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
    office= models.ForeignKey(Office,on_delete=models.CASCADE,null=True)
    
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname']

    def get_full_name(self):
        full_name = f'{self.firstname} {self.lastname}'
        return full_name
    
    def __str__(self):
        return self.email

    def has_perm(self, perm):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    objects=UserManager()
