from django.db import models

class Distance(models.Model):
    user_ip = models.IPAddressField()
    user_location = models.CharField()
    dest_location = models.CharField()
    distance = models.CharField()
    visit_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.distance