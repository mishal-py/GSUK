from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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
    rejected = models.BooleanField(default=False)
    rejection_reason = models.TextField(null=True, blank=True)

    def approve(self, user):
        self.approved = True
        self.approved_by = user
        self.approval_date = timezone.now()
        self.save()

    def reject(self, reason):
        self.rejected = True
        self.approved = False
        self.rejection_reason = reason
        self.save()

    @property
    def membership_fee(self):
        if self.membership_type == self.LIFE:
            return 100.00
        elif self.membership_type == self.ORDINARY:
            return 12.00
        return 0.00

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
