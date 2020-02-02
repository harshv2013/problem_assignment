from django.shortcuts import redirect, render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from design.forms import PersonForm
from design.models import Person

#
# class PersonCreate(CreateView):
#     model = Person
#     fields = '__all__'
#
# class PersonListView(generic.ListView):
#     model = Person
#     # paginate_by = 3
#
# class PersonDetailView(generic.DetailView):
#     model = Person
#
#
# class PersonUpdate(UpdateView):
#     model = Person
#     fields = '__all__'
#
# class PersonDelete(DeleteView):
#     model = Person
#     success_url = reverse_lazy('authers')
class PersonListView(generic.ListView):
    model = Person
    paginate_by = 10

class PersonDetailView(generic.ListView):
    model = Person




def emp(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        # print('form dict is ---------------@@@@@@@@@@@@@@@@@@@@', form.__dict__)

        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = PersonForm()
    return render(request,'design/person_edit.html',{'form':form})

def show(request):
    persons = Person.objects.all()
    return render(request,"show.html",{'persons':persons})

# def edit(request, id):
#     print('id of person is ----',id)
#     person = Person.objects.get(id=id)
#     print('person to edit---------------',person)
#     form = PersonForm()
#     return render(request,'edit.html', {'person':person})

def edit(request, id):
    print('id received----',id)
    person = get_object_or_404(Person, id=id)
    print('person object is ---', person)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)


        # if form.is_valid():
        #     try:
        #         form.save()
        #         return redirect('/show')
        #     except:
        # #         pass
        if form.is_valid():
            form.save()
        # person = form.save(commit=False)
        # post.author = request.user
        # post.save()
        return redirect('/show')
            # return redirect('post_detail', pk=post.pk)
    else:
        form = PersonForm(instance=person)
        # print('form dict is ---------------', form.__dict__)
    return render(request, 'design/person_edit.html', {'form': form})


def person_detail(request, id):
    person = get_object_or_404(Person, pk=id)

    return render(request, 'design/person_detail.html', {'person': person})


# def update(request, id):
#     person = Person.objects.get(id=id)
#     form = PersonForm(request.POST, instance = person)
#     if form.is_valid():
#         form.save()
#         return redirect("/show")
#     return render(request, 'index.html', {'person': person})
def destroy(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect("/show")
