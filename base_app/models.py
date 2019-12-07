from django.db import models

# Create your models here.


class Githubrepo(models.Model):
    repo_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.repo_name


class Gitrepo(models.Model):
    repo_name = models.CharField(max_length=264, unique=True)
    repo_description = models.CharField(max_length=264, unique=True)
    repo_link = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.repo_name


class KnownledgeOf(models.Model):
    framework = models.CharField(max_length=264, unique=True)
    framework_description = models.CharField(max_length=264, unique=True)
    framework_image = models.ImageField(
        upload_to='media', max_length=100, blank=True)

    def __str__(self):
        return self.framework


class Profile(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    profile_picture = models.ImageField(
        upload_to='media', max_length=100, blank=True)

    def __str__(self):
        return self.name


class StudyTimeline(models.Model):
    college = models.CharField(max_length=264, unique=True)
    pass_out_year = models.CharField(max_length=264, unique=True)
    degree = models.CharField(max_length=264, unique=True)


class Webpage(models.Model):
    topic = models.ForeignKey(Githubrepo, on_delete=models.PROTECT)
    title = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.title


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
