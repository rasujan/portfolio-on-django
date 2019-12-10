from django.contrib import admin
from base_app.models import Githubrepo, Profile, Webpage, AccessRecord, KnownledgeOf, Project, StudyTimeline
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Githubrepo)
admin.site.register(Project)
admin.site.register(KnownledgeOf)
admin.site.register(StudyTimeline)
admin.site.register(Profile)
