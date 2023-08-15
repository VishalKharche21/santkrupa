from django.db import models

# Create your models here.

class customers(models.Model):
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    gstno = models.CharField(max_length=100)
    
class report(models.Model):
    bill_no=models.IntegerField()
    company=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    gst=models.CharField(max_length=200)
    date = models.DateField()
    total_amount = models.CharField(max_length=200,blank=True,null=True)
    cgst = models.CharField(max_length=200,blank=True,null=True)
    sgst = models.CharField(max_length=200,blank=True,null=True)
    tgst = models.CharField(max_length=200,blank=True,null=True)
    cgst_amount = models.CharField(max_length=200,blank=True,null=True)
    sgst_amount = models.CharField(max_length=200,blank=True,null=True)
    tgst_amount = models.CharField(max_length=200,blank=True,null=True)
    grand_total = models.CharField(max_length=200,blank=True,null=True)
    word_total = models.CharField(max_length=800,blank=True,null=True)
    laborer = models.CharField(max_length=100,blank=True,null=True)
    lvno = models.CharField(max_length=100,blank=True,null=True)
    ltrip = models.CharField(max_length=100,blank=True,null=True)
    lrate = models.CharField(max_length=100,blank=True,null=True)
    lamount = models.CharField(max_length=100,blank=True,null=True)
    invoice_type = models.IntegerField()

    

class trip(models.Model):
    Report = models.ManyToManyField(report)
    from_company = models.CharField(max_length=500)
    to_company = models.CharField(max_length=500)
    vehical = models.CharField(max_length=200)
    trip = models.CharField(max_length=100)
    rate = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
