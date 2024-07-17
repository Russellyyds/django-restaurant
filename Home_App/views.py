from django.http import HttpResponse
from django.shortcuts import render, redirect

from Home_App.models import ItemList, Items, AboutUs, Feedback, BookTable


# Create your views here.
def home(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html', {'items': items, 'list': list, "review": review})


def about(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html', {'data': data})


def book_table(request):
    if request.method == 'POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_persons = request.POST.get('total_person')
        booking_date = request.POST.get('booking_date')

        if name != "" and email != "" and total_persons != 0 and booking_date != "":
            data = BookTable(Name=name, Phone_number=phone_number, Email=email, Total_person=total_persons,
                             Booking_date=booking_date)
            data.save()
            return redirect('/book_table?success=true')

    return render(request, 'book_table.html')


def menu(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})


def feedback(request):
    return render(request, 'feedback.html')
