from django.db import models

# Create your models here.


class PartsArrangement(models.Model):
    design_release_date = models.DateField()
    date_of_input = models.DateField(auto_now_add=True)
    pa_controller = models.CharField(max_length=50)
    model_code = models.CharField(max_length=50)
    set_adoption = models.BooleanField()
    CATAGORY_CHOICES = (
        ('T', 'Trial'),
        ('A', 'ASAP'),
        ('B', 'Blue'),
        ('R', 'Red')
    )
    catagory = models.CharField(max_length=1, choices=CATAGORY_CHOICES)
    design_note = models.CharField(max_length=50)
    lup = models.CharField(max_length=50, blank=True, null=True)
    old_part = models.CharField(max_length=50)
    old_status = models.CharField(max_length=50)
    old_sourcing = models.CharField(max_length=50)
    old_supplier = models.CharField(max_length=50)
    new_part = models.CharField(max_length=50, null=True, blank=True)
    NEW_CARRY_OVER_CHOICES = (
        ('N', 'New'),
        ('C', 'Carry_Over')
    )
    new_carry_over = models.CharField(max_length=1, choices=NEW_CARRY_OVER_CHOICES, null=True, blank=True)
    NEW_LP_OR_KD_CHOICES = (
        ('L', 'LP'),
        ('K', 'KD')
    )
    new_lp_or_kd = models.CharField(max_length=1, choices=NEW_LP_OR_KD_CHOICES, null=True, blank=True)
    new_region = models.CharField(max_length=50, null=True, blank=True)
    new_supplier_code = models.CharField(max_length=50, null=True, blank=True)
    new_supplier_name = models.CharField(max_length=100, null=True, blank=True)
    part_name = models.CharField(max_length=100)
    design_change_content = models.CharField(max_length=100)
    adoption_condition = models.CharField(max_length=100)
    torishi_old = models.CharField(max_length=50, null=True, blank=True)
    torishi_new = models.CharField(max_length=50, null=True, blank=True)
    per_car = models.IntegerField()
    application = models.CharField(max_length=50)
    adoption_agreed_plan = models.DateField(null=True, blank=True)
    physical_adoption_date_forecast = models.DateField(null=True, blank=True)
    due_by_against_planned_adoption = models.IntegerField(null=True, blank=True)

    @property
    def status_monitoring(self):
        return self.physical_adoption_date_forecast - self.date_of_input