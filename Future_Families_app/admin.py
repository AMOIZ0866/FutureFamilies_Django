from django.contrib import admin

# Register your models here.

# Register your models here.
from Future_Families_app.models.dependent_model import Idea, Idea1, Message, Messagesubj, Openlockedclosed, Projrole, \
    Statuscodeupdt, Stdoutemail, Subjcodeemail, Usercpt, Useridea, Userideafinal, Ideafirst, Role, Ideaaccess, \
    Ideastatus, Outmsgque, Stdoutemaildest, UserFirst, Userideatemp, Ideafinal, Ideatemp, Piemaildest, Sffemailaddr, \
    Userrole
from Future_Families_app.models.independent_models import Ideafinalhist, States, Stdoutemailhist, Ideahist, Userhist, \
    Projectinfo, Userideahist, Settings, Webpage

admin.site.register(Ideafinalhist)
admin.site.register(States)
admin.site.register(Stdoutemailhist)
admin.site.register(Ideahist)
admin.site.register(Userhist)
admin.site.register(Projectinfo)
admin.site.register(Userideahist)
admin.site.register(Settings)
admin.site.register(Webpage)
admin.site.register(Idea)
admin.site.register(Idea1)
admin.site.register(Message)
admin.site.register(Messagesubj)
admin.site.register(Openlockedclosed)
admin.site.register(Projrole)
admin.site.register(Statuscodeupdt)
admin.site.register(Stdoutemail)
admin.site.register(Subjcodeemail)
admin.site.register(Usercpt)
admin.site.register(Useridea)
admin.site.register(Userideafinal)
admin.site.register(Ideafirst)
admin.site.register(Role)
# admin.site.register(User)
admin.site.register(Ideaaccess)
admin.site.register(Ideastatus)
admin.site.register(Outmsgque)
admin.site.register(Stdoutemaildest)
admin.site.register(UserFirst)
admin.site.register(Userideatemp)
admin.site.register(Ideafinal)
admin.site.register(Ideatemp)
admin.site.register(Piemaildest)
admin.site.register(Sffemailaddr)
admin.site.register(Userrole)