from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mail
# Create your models here.


class Member(models.Model):
    LIFE = 'Life'
    ORDINARY = 'Ordinary'
    MEMBERSHIP_CHOICES = [
        (LIFE, 'Life Membership (£100)'),
        (ORDINARY, 'Ordinary Membership (£12 for 2 years)'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address_uk = models.TextField()
    address_nepal = models.TextField(blank=True)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='photos/')
    membership_type = models.CharField(
        max_length=20, choices=MEMBERSHIP_CHOICES)
    opt_out_contact = models.BooleanField(default=False)
    rules_confirmed = models.BooleanField()
    date_joined = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)
    approval_date = models.DateTimeField(null=True, blank=True)

    def approve(self, user):
        self.approved = True
        self.approved_by = user
        self.approval_date = timezone.now()
        self.save()

        send_mail(
            subject='GSUK Membership Approved',
            message='Congratulations, your GSUK membership has been approved.',
            from_email=None,
            recipient_list=[self.email],
            fail_silently=True,
        )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
