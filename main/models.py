from django.db import models

class Distance(models.Model):
    user_ip = models.IPAddressField()
    user_location = models.CharField(max_length=250)
    dest_location = models.CharField(max_length=250)
    distance = models.CharField(max_length=250)
    visit_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.distance