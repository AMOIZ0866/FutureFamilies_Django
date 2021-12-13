from django.contrib.auth.models import AbstractUser
from django.db import models


class Ideafirst(models.Model):
    ideanum = models.IntegerField(primary_key=True)


class Messagesubj(models.Model):
    subjectcode = models.CharField(max_length=14, null=False, primary_key=True)
    menusequence = models.IntegerField(default=None)
    shortdesc = models.CharField(max_length=20, null=False)
    active = models.SmallIntegerField(null=False, default='1')
    subjectdesc = models.CharField(max_length=40, null=False)


class Openlockedclosed(models.Model):
    subjectdesc = models.CharField(max_length=1, null=False, primary_key=True)
    openlockedcloseddesc = models.CharField(max_length=14, default=None)


class Projrole(models.Model):
    projrolecode = models.CharField(max_length=3, null=False, primary_key=True)
    projroledesc = models.CharField(max_length=28, null=False)


class Ideastatus(models.Model):
    ideastatuscode = models.CharField(max_length=3, primary_key=True, null=False)
    ideastatusnr = models.IntegerField(null=False)
    ideastatusname = models.CharField(max_length=14, null=False)
    subjectcode = models.ForeignKey(Messagesubj, on_delete=models.DO_NOTHING)  # Foreign Key From messagessubj
    ideaopenlockedclosedcode = models.ForeignKey(Openlockedclosed, on_delete=models.DO_NOTHING,
                                                 related_name="openlockedclosedcode+")  # Foreign Key From openlockedclosed
    ideafinalopenlockedclosedcode = models.ForeignKey(Openlockedclosed, on_delete=models.DO_NOTHING,
                                                      related_name="openlockedclosedcode+")  # Foreign Key From openlockedclosed
    ideastatusdesc = models.CharField(max_length=92, null=False)


class Idea(models.Model):
    ideanum = models.ForeignKey(Ideafirst, on_delete=models.CASCADE, primary_key=True)
    projname = models.CharField(max_length=35, null=False)
    reqamount = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    newprojnum = models.IntegerField(null=True, default=None)
    orgname = models.CharField(max_length=40, null=False)
    orgwebaddr = models.CharField(max_length=700, null=False)
    schoolname = models.CharField(max_length=35, null=True, default=None)
    schoolwebaddr = models.CharField(max_length=700, null=True, default=None)
    ideastatuscode = models.ForeignKey(Ideastatus, on_delete=models.DO_NOTHING)
    irsletter_TF = models.SmallIntegerField(null=False, default='0')
    lastaccess = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    ST_start_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    UP_update_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    S1_initsub_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    E1_InitRcptConf_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    PD1_PresDec_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    PD2_PresDecDone_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    PA_PresAccpt_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    GD1_GrantDec1_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    GD2_GrantDec1Done_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    GA1_GrantAccpt_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    E2_FinalistConfSent_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    S2_FinalSub_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    E3_FinalRcptConf_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    GD3_GrantDec2_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    GD4_GrantDec2Done_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    GA2_GrantAccpt2_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    BD_BoardDec_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    BD4_BoardDecDone_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    BA_BoardAccpt_time = models.DateTimeField(null=False, default='0000-00-00 00:00:00', )
    projnum = models.IntegerField(default=None)
    goal = models.CharField(max_length=360, null=False)
    relevance = models.CharField(max_length=360, null=False)
    summary = models.CharField(max_length=1500, null=False)
    parenting = models.CharField(max_length=2400, null=False)
    sel = models.CharField(max_length=2400, null=True)
    partnerplan = models.CharField(max_length=1800, null=True, default=True)
    resplan = models.CharField(max_length=1800, null=False, default=None)
    other = models.CharField(max_length=900, null=False, default=None)


class Idea1(models.Model):
    ideanum = models.AutoField(null=False, primary_key=True)
    projname = models.CharField(max_length=35, null=False)
    reqamount = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    newprojnum = models.IntegerField(null=True, default=None)
    orgname = models.CharField(max_length=40, null=False)
    orgwebaddr = models.CharField(max_length=700, null=False)
    schoolname = models.CharField(max_length=35, null=True, default=None)
    schoolwebaddr = models.CharField(max_length=700, null=True, default=None)
    pititle = models.CharField(max_length=3, null=False)
    picv = models.CharField(max_length=50, null=True, default=None)
    pifirstname = models.CharField(max_length=14, null=False)
    pimi = models.CharField(max_length=1, null=True, default=None)
    pilastname = models.CharField(max_length=14, null=False)
    pisuffix = models.CharField(max_length=3, null=True, default=None)
    piemail = models.CharField(max_length=700, null=False)
    pitele = models.BigIntegerField(null=False)
    piaddr1 = models.CharField(max_length=30, null=False)
    piaddr2 = models.CharField(max_length=30, null=True, default=None)
    picity = models.CharField(max_length=20, null=False)
    pistate = models.CharField(max_length=2, null=False)
    pizip = models.CharField(max_length=5, null=False)
    othertitle = models.CharField(max_length=3, null=True, default=None)
    otherfirstname = models.CharField(max_length=14, null=True, default=None)
    othermi = models.CharField(max_length=1, null=True, default=None)
    otherlastname = models.CharField(max_length=14, null=True, default=None)
    othersuffix = models.CharField(max_length=3, null=True, default=None)
    otheremail = models.CharField(max_length=700, null=True, default=None)
    othertele = models.BigIntegerField(null=True, default=None)
    otheraddr1 = models.CharField(max_length=30, null=True, default=None)
    otheraddr2 = models.CharField(max_length=30, null=True, default=None)
    othercity = models.CharField(max_length=20, null=True, default=None)
    otherstate = models.CharField(max_length=2, null=True, default=None)
    otherzip = models.CharField(max_length=5, null=True, default=None)
    ideastatuscode = models.ForeignKey(Ideastatus, on_delete=models.DO_NOTHING)
    irsletter_TF = models.SmallIntegerField(null=False, default='0')
    budget_TF = models.SmallIntegerField(null=False, default='0')
    confirmsent_TF = models.SmallIntegerField(null=False, default='0')
    projnum = models.IntegerField(default=None)
    goal = models.CharField(max_length=360, null=False)
    description = models.CharField(max_length=2400, null=False)
    aboutpeople = models.CharField(max_length=1500, null=True, default=None)
    relevance = models.CharField(max_length=2400, null=False)
    dissemination = models.CharField(max_length=900, null=False)
    projother = models.CharField(max_length=900, null=True, default=None)


class Message(models.Model):
    msgnr = models.AutoField(null=False, primary_key=True)
    msgdate = models.TimeField(null=False)
    subjectcode = models.ForeignKey(Messagesubj, on_delete=models.DO_NOTHING)
    visname = models.CharField(max_length=41, null=False)
    visemailaddr = models.CharField(max_length=60, default=None)
    ideanum = models.IntegerField(default=None)
    message = models.CharField(max_length=480, default=None)


class Statuscodeupdt(models.Model):
    currideastatuscode = models.CharField(max_length=3, primary_key=True)
    validideastatuscodeupdt = models.ForeignKey(Ideastatus, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (('currideastatuscode', 'validideastatuscodeupdt'),)


class Sffemailaddr(models.Model):
    inemailaddr = models.CharField(primary_key=True, max_length=60, null=False)
    inemailname = models.CharField(max_length=41, null=False)
    outemailaddr = models.CharField(max_length=60, null=False)
    outemailname = models.CharField(max_length=41, null=False)
    DHemailtype = models.CharField(max_length=2, null=False)
    monitored_YN = models.SmallIntegerField(null=False, default=1)
    emailpurpose = models.CharField(max_length=150, null=False)


class Stdoutemail(models.Model):
    stdoutemailnr = models.IntegerField(null=False, primary_key=True)
    emailtypecode = models.IntegerField(null=False)
    active = models.SmallIntegerField(null=False, default='1')
    delaytimehr = models.IntegerField(null=False)
    stdoutemaildesc = models.CharField(max_length=60, null=False)
    stdoutemailaddr = models.ForeignKey(Sffemailaddr, on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=2000, default=None)


###########################
class Subjcodeemail(models.Model):
    subjectcode = models.ForeignKey(Messagesubj, on_delete=models.CASCADE,primary_key=True)
    stdoutemailnr = models.ForeignKey(Stdoutemail, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('subjectcode', 'stdoutemailnr'),)


class UserFirst(models.Model):
    emailaddress = models.CharField(max_length=50, null=False, primary_key=True)


class Usercpt(models.Model):
    emailaddress = models.ForeignKey(UserFirst, primary_key=True, on_delete=models.CASCADE)
    orgname = models.CharField(max_length=40, null=False)
    schoolname = models.CharField(max_length=40, default=None)
    orgwebaddr = models.CharField(max_length=70, default=None)
    position = models.CharField(max_length=35, null=False)
    tele = models.BigIntegerField(null=False)
    addr1 = models.CharField(max_length=30, null=False)
    addr2 = models.CharField(max_length=30, default=True)
    city = models.CharField(max_length=20, null=False)
    state = models.CharField(max_length=2, null=False)
    zip = models.CharField(max_length=5, null=False)
    cv = models.CharField(max_length=70, null=False)
    about = models.CharField(max_length=1500, null=False)


class Ideaaccess(models.Model):
    ideaaccesscode = models.CharField(max_length=1, primary_key=True, null=False)
    ideaaccessdesc = models.CharField(max_length=25, null=False)


class Useridea(models.Model):
    emailaddress = models.ForeignKey(UserFirst, on_delete=models.CASCADE )
    ideanum = models.ForeignKey(Ideafirst, on_delete=models.CASCADE)
    projrolecode = models.ForeignKey(Projrole, on_delete=models.DO_NOTHING)
    ideaaccesscode = models.ForeignKey(Ideaaccess, on_delete=models.DO_NOTHING)
    anticipated_contrib = models.CharField(max_length=180, null=False)


    class Meta:
        unique_together = (('emailaddress', 'ideanum'),)


class Userideafinal(models.Model):
    emailaddress = models.ForeignKey(UserFirst, on_delete=models.CASCADE)
    ideanum = models.ForeignKey(Ideafirst, on_delete=models.CASCADE)
    projrolecode = models.ForeignKey(Projrole, on_delete=models.DO_NOTHING)
    ideaaccesscode = models.ForeignKey(Ideaaccess, on_delete=models.DO_NOTHING)
    anticipated_contrib = models.CharField(max_length=180, null=False)

    class Meta:
        unique_together = (('emailaddress', 'ideanum'),)


class Role(models.Model):
    rolecode = models.CharField(max_length=10, primary_key=True)
    entrypagename = models.CharField(max_length=65)
    roledesc = models.CharField(max_length=35)
    roleshortdesc = models.CharField(max_length=30, unique=True)


class Outmsgque(models.Model):
    emailnr = models.AutoField(primary_key=True)  # auto increment 10
    msgnr = models.ForeignKey(Message, on_delete=models.CASCADE)  # foreign key from message
    msgdate = models.DateTimeField(null=False)
    minsendtime = models.DateTimeField(null=False)
    msgsent_YN = models.SmallIntegerField(default=0, null=False)
    stdoutemailnr = models.ForeignKey(Stdoutemail, on_delete=models.DO_NOTHING)  # foreign key from stdoutemail
    emailtypecode = models.IntegerField(null=False)
    stdoutmsgsubj = models.CharField(max_length=120, null=False)
    sffsendemailaddr = models.ForeignKey(Sffemailaddr, on_delete=models.DO_NOTHING ,related_name="inemailaddr+")  # foreign key from sffemailaddr
    sffsendemailname = models.CharField(max_length=41, null=False)
    destemailaddr = models.CharField(max_length=900, null=False)
    destemailname = models.CharField(max_length=41, null=False)
    ideanum = models.IntegerField(default=None, null=False)
    body = models.CharField(max_length=2000, default=None)


class Stdoutemaildest(models.Model):
    stdoutemailnr = models.ForeignKey(Stdoutemail, on_delete=models.CASCADE)  # foreign key stdoutemail ON DELETE CASCADE
    destemailaddr = models.ForeignKey(Sffemailaddr, on_delete=models.DO_NOTHING)  # foreign key sffemailaddr

    class Meta:
        unique_together = (("stdoutemailnr", "destemailaddr"))


class Userideatemp(models.Model):
    emailaddress = models.ForeignKey(UserFirst, on_delete=models.CASCADE)  # foreign key from userfirst ON DELETE CASCADE,
    ideanum = models.ForeignKey(Ideafirst, on_delete=models.CASCADE)  # foreign key from ideafirst ON DELETE CASCADE,
    projrolecode = models.CharField(max_length=3, default=None)
    ideaaccesscode = models.ForeignKey(Ideaaccess, on_delete=models.DO_NOTHING)  # foreign key from ideaaccess
    anticipated_contrib = models.CharField(max_length=180, default=None)

    class Meta:
        unique_together = (("emailaddress", "ideanum"),)


class Ideafinal(models.Model):
    ideanum = models.ForeignKey(Ideafirst,primary_key=True, on_delete=models.CASCADE)  # foreign key ideafirst ON DELETE CASCADE
    myidea = models.CharField(max_length=3000, null=False)
    importance = models.CharField(max_length=1500, null=False)
    theoryofchange = models.CharField(max_length=1800, null=False)
    outcomealign = models.CharField(max_length=2100, null=False)
    researchplan = models.CharField(max_length=2400, null=False)
    partnership = models.TextField()
    lack = models.TextField(null=False)
    implement = models.TextField()
    outcomedetail = models.CharField(max_length=2100, null=False)
    impact = models.CharField(max_length=1500, null=False)
    definesuccess = models.CharField(max_length=1500, null=False)
    other = models.TextField()
    budget_TF = models.SmallIntegerField(null=False, default=0)
    budgetnar_TF = models.SmallIntegerField(null=False, default=0)
    workplan_TF = models.SmallIntegerField(null=False, default=0)


class Ideatemp(models.Model):
    ideanum = models.ForeignKey(Ideafirst, on_delete=models.CASCADE, primary_key=True)  # foreign key ideafirst ON DELETE CASCADE
    projname = models.CharField(max_length=35, default=None)
    reqamount = models.DecimalField(max_digits=8, decimal_places=2, default=None)
    orgname = models.CharField(max_length=40, default=None)
    orgwebaddr = models.CharField(max_length=700, default=None)
    schoolname = models.CharField(max_length=35, default=None)
    schoolwebaddr = models.CharField(max_length=700, default=None)
    irsletter_TF = models.SmallIntegerField(null=False, default=0)
    lastaccess = models.DateTimeField(auto_created=True, null=False)
    st_start_time = models.DateTimeField(auto_created=True, null=False)
    goal = models.CharField(max_length=360, null=False)
    relevance = models.CharField(max_length=360, null=False)
    summary = models.CharField(max_length=1500, null=False)
    parenting = models.CharField(max_length=2400, null=False)
    sel = models.CharField(max_length=2400, default=None)
    partnerplan = models.CharField(max_length=1800, default=None)
    resplan = models.CharField(max_length=1800, default=None)
    dissemination = models.CharField(max_length=1500, default=None)
    other = models.CharField(max_length=900, default=None)


class Piemaildest(models.Model):
    ideanum = models.ForeignKey(Ideafirst, on_delete=models.CASCADE)  # foreign key ideafirst ON DELETE CASCADE
    piemailaddr = models.CharField(max_length=60, null=False)
    piname = models.CharField(max_length=41, default=None)


    class Meta:
        unique_together = (("ideanum", "piemailaddr"),)


class Userrole(models.Model):
    emailaddress = models.ForeignKey(UserFirst,on_delete=models.CASCADE)  # foreign key userfirst ON DELETE CASCADE
    rolecode = models.ForeignKey(Role,on_delete=models.DO_NOTHING)  # foreign key role

    class Meta:
        unique_together = (("emailaddress", "rolecode"))

# class User(AbstractUser):
#     active = models.SmallIntegerField(null=False, default='1')
#     reg_complete = models.SmallIntegerField(null=False, default='0')
#     authenticated = models.SmallIntegerField(null=False, default='0')
#     anonymous = models.SmallIntegerField(null=False, default='0')
#     created_at = models.DateTimeField(null=False,auto_now=True)
#     confirmed_at = models.DateTimeField(null=True, default=None)
#     lastaccess = models.DateTimeField(null=False, auto_now=True)
#     lastlogin = models.DateTimeField(null=False, auto_now=True)
#     preferred_name = models.CharField(max_length=41 )
#     title = models.CharField(max_length=3, null=False)
#     mi = models.CharField(max_length=1, default=None)
#     namesuffix = models.CharField(max_length=3, default=None)
#     fs_uniquifier = models.CharField(max_length=255, null=False)
#     userfirst = models.ForeignKey(UserFirst,on_delete=models.DO_NOTHING)


# class Ideastatus(models.Model):
