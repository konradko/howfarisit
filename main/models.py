from django.db import models

class Distance(models.Model):
    user_ip = models.IPAddressField()
    distance = models.DecimalField(max_digits=999, decimal_places=999)
    visit_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.distance