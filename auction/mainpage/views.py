from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Items,Bids
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    item=Items.objects.all()    
    return render(request,"index.html",{
        "items":item,
    })

@login_required
def bid(request,slug):
    book=get_object_or_404(Items,slug=slug)
    if request.method == 'POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            bid=Bids()
            increment = form.cleaned_data['bid']
            if increment>0:
                user = request.user 
                if user==book.highest:
                    return redirect("auction")
                bid.item=book.slug
                bid.name=user
                book.bid+=increment
                bid.bid=book.bid
                bid.save()
                book.highest=user
                book.save()
            return redirect("auction")        
    else:
        form=ReviewForm()
    bids=Bids.objects.filter(item=slug).order_by('-timestamp')
    return render(request,"bid.html",{
        "book":book,
        "form":form,
        "bids":bids
    })