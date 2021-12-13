from django.db import models


#INDEPENTENT MODELS:

class Ideafinalhist(models.Model):
    savedtime = models.DateTimeField()
    ideanum = models.IntegerField(primary_key=True)
    myidea = models.CharField(max_length=255, default=None)
    importance = models.CharField(max_length=250, default=None)
    theoryofchange = models.CharField(max_length=250, default=None)
    outcomealign = models.CharField(max_length=250, default=None)
    researchplan = models.CharField(max_length=250, default=None)
    partnership = models.TextField()
    lack = models.TextField()
    implement = models.TextField()
    outcomedetail = models.CharField(max_length=250, default=None)
    impact = models.CharField(max_length=250, default=None)
    definesuccess = models.CharField(max_length=250, default=None)
    other = models.TextField()
    budget_TF = models.SmallIntegerField(default=None)
    budgetnar_TF = models.SmallIntegerField(default=None)
    workplan_TF = models.SmallIntegerField(default=None)
