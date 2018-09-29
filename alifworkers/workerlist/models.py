from django.db import models
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import reverse


SEX = (
    ('Male', 'Male'),
    ('Female','Female'),
    ('Not specified', 'Not specified'),
)

DEPARTMENTS = (
    ('Department 1', 'Department 1'),
    ('Department 2','Department 2'),
    ('IT Department', 'IT Department'),
)


class Workers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Slug = models.SlugField(max_length=200)
    Name = models.CharField(max_length=100, help_text='Name of the worker ')
    Surname = models.CharField(max_length=100, help_text='Surname of the worker ')
    DOB = models.DateField(auto_now=False)
    WorkerPhoto = models.ImageField(upload_to='workersPhoto/', blank=True, help_text='Photo of the worker. Please make it small befor uploading')
    Department = models.CharField(max_length=100,  choices = DEPARTMENTS, help_text="Select from the list")
    JoinDate = models.DateField(auto_now=False)
    Sex = models.CharField(max_length=100, choices = SEX, help_text='Select from the list...')


    def __str__(self):
        return self.Name + ', ' +self.Surname

 
    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
        ordering = (('-Name'),)


    def get_absolute_url(self):
        return self.Slug

class Address(models.Model):
    FullAddress = models.CharField(max_length=200, help_text = 'Please enter the full address of the worker...')
    Phone = models.IntegerField(default=0, help_text='Enter your mobile phone with country city codes by excluding the plus sign ')
    Email = models.EmailField()
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE)

    def __str__(self):
        return self.FullAddress

class Education(models.Model):
    StartDate = models.DateField(auto_now=False)
    FinishDate = models.DateField(auto_now=False, blank=True)
    TypeOfQualification = models.CharField(max_length=100, help_text='ex. Master Degree; Bachelor Degree, etc')
    NameOfOrganisation = models.CharField(max_length=100, help_text='Name of the institution provided the education')
    Address = models.CharField(max_length=100, help_text='Enter the address')
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE)
  

    def __str__(self):
        return self.TypeOfQualification

class Position(models.Model):
    Position = models.CharField(max_length=100, help_text='Enter the position of the worker ')
    StartDate = models.DateField(auto_now=True)
    FinishDate = models.DateField(auto_now=True, blank=True)
    worker = models.ForeignKey(Workers, on_delete=models.CASCADE)
     
    def __str__(self):
       return self.Position


    







