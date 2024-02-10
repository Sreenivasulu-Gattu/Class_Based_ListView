1.We have to create a folder inside templates folder under app name .
2. create the ListView class and just mension the following code 
    class SchoolList(ListView):
      model = School                  --> just give the model name , automatically everything will be done 
      context_object_name = 'Schools'     --> creating of list of objects and creating and returning context will done internally 
      ordering = ['col name']       --> based on the condition only orderby will perform
      queryset = modelname.objects.filter(col = value) --> optional
      template_name = 'appname/modelname_list.html' -->optional 
3.create the template and mension the objects 
4.Path('SchoolList/',SchoolList.as_view(),name='SchoolList'),
