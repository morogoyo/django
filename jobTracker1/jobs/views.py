from django.shortcuts import render
from .models import LmsCompanies
from django.http import HttpResponse,HttpRequest
from .forms import Search


# Create your views here.
 
def index(request):
	today ="this is working" 				#test text for template use 
	companies = LmsCompanies.objects.all() 	#collect all info from data base and store it 
	context = {'dataBase':companies } 		#make a dictionary to iterate thru in the template 
	return render(request,'jobs/template.html',context)
	'''return the render function it has all it needs to function ie
	 the Httprequest, template load,'''


def search(request):
	title = 'Search Page'
	 
	if request.method == 'POST':
		print(request.POST)
	form = Search(request.POST or None)# add form (instanciate form from imported class)
	# 									   # wer are passing in the form as a part of the context so django will handle it
	companies = LmsCompanies.objects.all()
	post = request.POST['search']
	# the query API will search no case sensitivity it uses sql wildcard
	#variable = modelName.objects.get(columnName__Filter='what you are searching for')	
	after_post=LmsCompanies.objects.get(name__icontains=post)
	
	context={'title':title,'value':companies,'post_after':after_post,'form':form}
	
	
		
	return render(request,"jobs/search-result.html",context)
	
		# return render(request,"jobs/search.html",context)
				











# def search(request):
# 	companies = LmsCompanies.objects.all() #collect all info from data base and store it
# 	testVariable= "the method is passing a value"
# 	context ='' 
# 	if request.method == "POST":
# 		name = Search(request.POST)
		
# 		for search in companies:
			
# 			if name == search:
# 				name = "rene"
# 			context = {'dataBase': name, 'testVariable':testVariable}
# 		return render(request,'jobs/search-result.html',context)
# 	else:
# 		return render(request,'jobs/search.html',context)	


	# context = {'dataBase': context, 'testVariable':testVariable}
	# return render(request,'jobs/search-result.html',context)

