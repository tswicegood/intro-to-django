from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=2)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.code)


class Person(models.Model):
    name = models.CharField(max_length=250)
    language = models.ForeignKey(Language, related_name='people')

    def __unicode__(self):
        return self.name
