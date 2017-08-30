from django.contrib import admin
from Survey.models import office,intro
from Survey.forms import officeForm, introForm
# Register your models here.


def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=senario_Office.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("Office")
    
    row_num = 0
    
    columns = [
        (u"ID", 2000),

    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1
    
    for obj in queryset:
        row_num += 1
        row = [
            obj.ID
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)
    return response
    
export_xls.short_description = u"Export XLS"

class OfficeAdmin(admin.ModelAdmin):
    actions = [export_xls]
	
admin.site.register(office, OfficeAdmin)


class introAdmin(admin.ModelAdmin):
	form = introForm
admin.site.register(intro, introAdmin)
'''
def get_User_Info(request):
form = introForm(request.POST)
print(request.method)
if request.method == 'POST':
form = introForm(request.POST)
if form.is_valid():			
name = request.POST['name']
print(name)
			sex = request.POST['sex']
			education = request.POST['education']
			intro.objects.create(
				name = name,
				sex = sex,
				education = education
			)
			intro.save()
			print (connection.queries)
		 
			return HttpResponseRedirect("/vote/")
	return render(request, 'index.html', {'introForm': form})
'''
