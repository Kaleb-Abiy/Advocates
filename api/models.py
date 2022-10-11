from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=300)
    logo = models.ImageField(blank=True)
    summary = models.TextField()


    def __str__(self):
        return self.name
    


class Advocate(models.Model):
    name = models.CharField(max_length=200)
    profile_pic = models.ImageField(blank=True)
    short_bio = models.CharField(max_length=500)
    long_bio = models.TextField()
    advocate_years_exp = models.PositiveIntegerField()
    company = models.ForeignKey(Company, related_name= 'advocates', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AdvocateLink(models.Model):
    advocate = models.OneToOneField(Advocate, related_name='links', on_delete=models.CASCADE)
    youtube = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.advocate.name}-links'
    










