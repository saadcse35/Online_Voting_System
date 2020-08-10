from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings



# Create your models here.


class VoteInfo(models.Model):
    code = models.CharField(max_length=30)
    caption = models.CharField(max_length=200)
    is_Active = models.BooleanField(default=True)

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')
    date_Created = models.DateTimeField(default=timezone.now)
    last_Updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'vote_info'

    def __str__(self):
        return self.caption


class Party(models.Model):
    code = models.CharField(max_length=30)
    caption = models.CharField(max_length=200)
    icon = models.ImageField(upload_to="static/images/")
    desc = models.TextField()
    remk = models.CharField(null=True, blank=True, max_length=500)
    is_Active = models.BooleanField(default=True)

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')
    date_Created = models.DateTimeField(default=timezone.now)
    last_Updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'party'

    def __str__(self):
        return self.caption

class Division(models.Model):
    code = models.CharField(max_length=30)
    caption = models.CharField(max_length=200)
    is_Active = models.BooleanField(default=True)

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')
    date_Created = models.DateTimeField(default=timezone.now)
    last_Updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'division'

    def __str__(self):
        return self.caption


class District(models.Model):
    code = models.CharField(max_length=30)
    caption = models.CharField(max_length=200)
    Division = models.ForeignKey(Division, null=False, on_delete=models.CASCADE)
    is_Active = models.BooleanField(default=True)

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')
    date_Created = models.DateTimeField(default=timezone.now)
    last_Updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'district'

    def __str__(self):
        return self.caption


class Upazila(models.Model):
    code = models.CharField(max_length=30)
    caption = models.CharField(max_length=200)
    District = models.ForeignKey(District, null=False, on_delete=models.CASCADE)
    Division = models.ForeignKey(Division, null=False, on_delete=models.CASCADE)
    is_Active = models.BooleanField(default=True)

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')
    date_Created = models.DateTimeField(default=timezone.now)
    last_Updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'upazila'

    def __str__(self):
        return self.caption


class UnionCouncil(models.Model):
    code = models.CharField(max_length=30)
    caption = models.CharField(max_length=200)
    Upazila = models.ForeignKey(Upazila, null=False, on_delete=models.CASCADE)
    District = models.ForeignKey(District, null=False, on_delete=models.CASCADE)
    Division = models.ForeignKey(Division, null=False, on_delete=models.CASCADE)
    is_Active = models.BooleanField(default=True)

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')
    date_Created = models.DateTimeField(default=timezone.now)
    last_Updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'union_council'

    def __str__(self):
        return self.caption


class Voter(models.Model):
    STATUS = (
        ('Married', 'Married'),
        ('Unmarried', 'Unmarried'),
        ('Divorced', 'Divorced')
    )
    SEXTYPE = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )

    first_Name = models.CharField(max_length=50)
    last_Name = models.CharField(null=True, max_length=50)
    nid = models.BigIntegerField(unique=True)
    password = models.CharField(max_length=30)
    contact_No = models.CharField(max_length=15)
    email = models.EmailField(null=True, max_length=50)
    marital_Status = models.CharField(max_length=20, choices=STATUS)
    sex = models.CharField(max_length=20, choices=SEXTYPE)
    Division = models.ForeignKey(Division, null=False, on_delete=models.CASCADE)
    District = models.ForeignKey(District, null=False, on_delete=models.CASCADE)
    Upazila = models.ForeignKey(Upazila, null=False, on_delete=models.CASCADE)
    UnionCouncil = models.ForeignKey(UnionCouncil, null=False, on_delete=models.CASCADE)
    voter_area = models.CharField(max_length=100)
    remk = models.CharField(null=True, blank=True, max_length=500)
    is_Active = models.BooleanField(default=True)

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')
    date_Created = models.DateTimeField(default=timezone.now)
    last_Updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'voter'

    def __str__(self):
        return self.first_Name


class Candidate(models.Model):
    caption = models.CharField(max_length=200)
    Party = models.ForeignKey(Party, on_delete=models.CASCADE)
    VoteInfo = models.ForeignKey(VoteInfo, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name='CandidateUser')
    Voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    remk = models.CharField(null=True, blank=True, max_length=500)
    is_Active = models.BooleanField(default=True)

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')
    date_Created = models.DateTimeField(default=timezone.now)
    last_Updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'candidate'

    def __str__(self):
        return self.caption


class VoteCalculation(models.Model):
    code = models.CharField(max_length=30)
    VoteInfo = models.ForeignKey(VoteInfo, null=False, on_delete=models.CASCADE)
    Candidate = models.ForeignKey(Candidate, null=False, on_delete=models.CASCADE)
    User = models.ForeignKey(User, null=False, on_delete=models.CASCADE,related_name='VoterUser')
    is_Active = models.BooleanField(default=True)

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')
    date_Created = models.DateTimeField(default=timezone.now )
    last_Updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'vote_calculation'

    def __str__(self):
        return self.VoteInfo


class VoteWiseVoterList(models.Model):
    VoteInfo = models.ForeignKey(VoteInfo, null=False, on_delete=models.CASCADE)
    Voter = models.ForeignKey(Voter, null=False, on_delete=models.CASCADE)
    nid = models.BigIntegerField(null= False)
    tokenNumber = models.IntegerField(unique=True)

    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='1')
    date_Created = models.DateTimeField(default=timezone.now)
    last_Updated = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'vote_wise_voter'
        # nid = 'Voter.nid'

    def __str__(self):
        return self.nid






