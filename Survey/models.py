from django.db import models

# Create your models here.
'''
class Office(models.Model):
	optionsID = models.AutoField(primary_key = True)
	optionValue = models.IntegerField()
	optionContext = models.CharField(max_length = 40)

	class Meta:
		db_table = u'Office'
'''


class intro(models.Model):
	EDUCATION_CHOICES = (
						('1','1'),
						('2','2'),
						('3','3'),
						('4','4'),
						('G','Graduate'),
						('P','Professor')
						)
	SEX_CHOICES = (
			   ('M','Male'),
			   ('F','Female'),
			   )
	name = models.CharField(max_length = 10, default = 'apple')
	education = models.CharField(max_length = 1,choices = EDUCATION_CHOICES, default = '1')
	sex = models.CharField(max_length = 1, choices = SEX_CHOICES, default = 'M')
'''
class Issues(models.Model):
	name = models.charField(max_lengt= 2)	
'''
class office(models.Model):
	'''
	Office_Space = (
		('ISSUE1',(
				('R1B1','R1B1'),
				('R2B1', 'R2B1'),
				('R3B1', 'R3B1'),
			)),
		('ISSUE2',(
				('R1B2', 'R1B2'),
				('R2B2', 'R2B2'),
				('R3B2', 'R3B2'),  
			)),
		('ISSUE3',(
				('R1B3', 'R1B3'),
				('R2B3', 'R2B3'),
				('R3B3', 'R3B3'),
			)),		
	)
	'''
	#issues = models.ForeignKey(Issues, on_delete = models.CASCADE)
	R1B1 = models.PositiveSmallIntegerField(default = 1)
	R2B1 = models.PositiveSmallIntegerField(default = 1)
	R3B1 = models.PositiveSmallIntegerField(default = 1)
	R1B2 = models.PositiveSmallIntegerField(default = 1)
	R2B2 = models.PositiveSmallIntegerField(default = 1)
	R3B2 = models.PositiveSmallIntegerField(default = 1)
	R1B3 = models.PositiveSmallIntegerField(default = 1)
	R2B3 = models.PositiveSmallIntegerField(default = 1)
	R3B3 = models.PositiveSmallIntegerField(default = 1)

	#values = models.PositiveSmallIntegerField(default = 1)
	#user = models.ForeignKey(Intro, on_delete = models.CASCADE)
