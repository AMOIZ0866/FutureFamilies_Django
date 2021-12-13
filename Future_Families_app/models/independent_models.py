from django.db import models


# INDEPENTENT MODELS:

class Ideafinalhist(models.Model):
    savedtime = models.DateTimeField(primary_key=True, auto_now=True)
    ideanum = models.IntegerField(null=False)
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


class States(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=128)


class Stdoutemailhist(models.Model):
    savedtime = models.DateTimeField(primary_key=True, auto_now=True)
    msgnr = models.IntegerField(null=False)
    stdoutemailnr = models.IntegerField(null=False)
    msgsubj = models.CharField(max_length=255, default=None)
    sfforigemail = models.CharField(max_length=60, default=None)
    sffusername = models.CharField(max_length=41, default=None)
    destuseremail = models.CharField(max_length=60, default=None)
    title = models.CharField(max_length=3, default=None)
    firstname = models.CharField(max_length=60, default=None)
    mi = models.CharField(max_length=2, default=None)
    lastname = models.CharField(max_length=16, default=None)
    namesuffix = models.CharField(max_length=3, default=None)
    visname = models.CharField(max_length=41, default=None)


class Ideahist(models.Model):
    savedtime = models.DateTimeField(primary_key=True, auto_now=True)
    ideanum = models.IntegerField(null=False)
    projname = models.CharField(max_length=255, default=None)
    reqamount = models.DecimalField(max_digits=8, decimal_places=2, default=None)
    newprojnum = models.IntegerField(default=None)
    orgname = models.CharField(max_length=40, default=None)
    orgwebaddr = models.CharField(max_length=700, default=None)
    schoolname = models.CharField(max_length=35, default=None)
    schoolwebaddr = models.CharField(max_length=700, default=None)
    ideastatuscode = models.CharField(max_length=3, default=None)
    irsletter_TF = models.SmallIntegerField(default=None)
    lastaccess = models.DateTimeField(default=None, null=True)
    ST_start_time = models.DateTimeField(default=None, null=True)
    UP_update_time = models.DateTimeField(default=None, null=True)
    S1_initsub_time = models.DateTimeField(default=None, null=True)
    E1_InitRcptConf_time = models.DateTimeField(default=None, null=True)
    PD1_PresDec_time = models.DateTimeField(default=None, null=True)
    PD2_PresDecDone_time = models.DateTimeField(default=None, null=True)
    PA_PresAccpt_time = models.DateTimeField(default=None, null=True)
    GD1_GrantDec1_time = models.DateTimeField(default=None, null=True)
    GD2_GrantDec1Done_time = models.DateTimeField(default=None, null=True)
    GA1_GrantAccpt_time = models.DateTimeField(default=None, null=True)
    E2_FinalistConfSent_time = models.DateTimeField(default=None, null=True)
    S2_FinalSub_time = models.DateTimeField(default=None, null=True)
    E3_FinalRcptConf_time = models.DateTimeField(default=None, null=True)
    GD3_GrantDec2_time = models.DateTimeField(default=None, null=True)
    GD4_GrantDec2Done_time = models.DateTimeField(default=None, null=True)
    GA2_GrantAccpt2_time = models.DateTimeField(default=None, null=True)
    BD_BoardDec_time = models.DateTimeField(default=None, null=True)
    BD4_BoardDecDone_time = models.DateTimeField(default=None, null=True)
    BA_BoardAccpt_time = models.DateTimeField(default=None, null=True)
    projnum = models.IntegerField(default=None)
    goal = models.CharField(max_length=360, null=False)
    relevance = models.CharField(max_length=360, null=False)
    summary = models.CharField(max_length=1500, null=False)
    parenting = models.CharField(max_length=2400, null=False)
    sel = models.CharField(max_length=2400, default=None)
    partnerplan = models.CharField(max_length=2400, default=None)
    resplan = models.CharField(max_length=1800, null=False)
    dissemination = models.CharField(max_length=2400, null=False)
    other = models.CharField(max_length=900, default=None)


class Userhist(models.Model):
    savedtime = models.DateTimeField(primary_key=True, auto_now=True)
    emailaddress = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=22, default=None)
    lastaccess = models.DateTimeField(default=None)
    lastlogin = models.DateTimeField(default=None)
    preferredname = models.CharField(max_length=41, default=None)
    title = models.CharField(max_length=3, default=None)
    firstname = models.CharField(max_length=14, default=None)
    mi = models.CharField(max_length=2, default=None)
    lastname = models.CharField(max_length=16, default=None)
    namesuffix = models.CharField(max_length=3, default=None)
    orgname = models.CharField(max_length=40, default=None)
    schoolname = models.CharField(max_length=35, default=None)
    orgwebaddr = models.CharField(max_length=70, default=None)
    position = models.CharField(max_length=35, default=None)
    tele = models.BigIntegerField(default=None)
    addr1 = models.CharField(max_length=30, default=None)
    addr2 = models.CharField(max_length=30, default=None)
    city = models.CharField(max_length=20, default=None)
    state = models.CharField(max_length=2, default=None)
    zip = models.CharField(max_length=5, default=None)
    cv = models.CharField(max_length=70, default=None)
    about = models.CharField(max_length=1500, default=None)


class Projectinfo(models.Model):
    ProjName1 = models.CharField(max_length=15, null=False)
    ProjName2 = models.CharField(max_length=10, null=False)
    ProjName3 = models.CharField(max_length=10, null=False)
    ProjAddr1 = models.CharField(max_length=38, null=False)
    ProjAddr2 = models.CharField(max_length=20, null=False)
    TelephoneNr = models.CharField(max_length=12, null=False)
    EmailAddr = models.CharField(max_length=30, null=False)
    LeadPixInscr1 = models.CharField(max_length=10, null=False)
    LeadPixInscr2 = models.CharField(max_length=10, null=False)
    LeadPixInscr3 = models.CharField(max_length=10, null=False)
    CopyrightMsg1 = models.CharField(max_length=10, null=False)
    CopyrightMsg2 = models.CharField(max_length=25, null=False)


class Userideahist(models.Model):
    savedtime = models.DateTimeField(primary_key=True, auto_now=True)
    EmailAddr = models.CharField(max_length=50, null=False)
    ideanum = models.IntegerField(null=False)
    projrolecode = models.CharField(max_length=3, default=None)
    ideaaccesscode = models.CharField(max_length=1, default=None)
    anticipated_contrib = models.CharField(max_length=180, default=None)


class Settings(models.Model):
    settingsname = models.CharField(max_length=25, null=False)
    settingsdesc = models.CharField(max_length=60, null=False)
    format = models.CharField(max_length=20, default=None)
    datatype = models.CharField(max_length=15, default=None)
    dimension = models.CharField(max_length=25, default=None)
    def_val = models.CharField(max_length=50, default=None)
    curr_val = models.CharField(max_length=50, default=None)


class Webpage(models.Model):
    pageName = models.CharField(max_length=25, primary_key=True, null=False)
    title = models.CharField(max_length=60, null=False)
