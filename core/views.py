from django.views import View
from django.shortcuts import render, redirect
from .models import Category, Item
from .forms import ItemForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView



# Create your views here.

class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        items = Item.objects.all()
        context = {
            "title": "Home",
            "categories": categories,
            "items": items,
        }
        return render(request, 'home.html', context)
    
class AddItemView(View):
    def get(self, request):
        context = {
            "title": "Add Item",
        }
        form = ItemForm()
        return render(request, 'add_item.html', {"form":form, "context": context})
    
    def post(self, request):
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        context = {
            "title": "Add Item",
        }
        return render(request, 'add_item.html', {"form":form, "context": context})

class ItemDetailView(View):
    def get(self, request, pk):
        try:
            item = Item.objects.get(id=pk)
        except Item.DoesNotExist:
            return redirect('home')
        context = {
            "title": item.name,
            "item": item,
        }
        return render(request, 'item_detail.html', context)
    
class ItemUpdateView(UpdateView):
    model = Item
    fields = [
        "name",
        "description",
        "category",
        "quantity",
        "purchase_date",
        "price",
        "serial_number",
        "warranty_expiry",
        "location",
        "notes",
        "image"
    ]
    template_name = "add_item.html"  # reuse Add form template

    # After edit, redirect back to item detail
    def get_success_url(self):
        return reverse_lazy("item_detail", kwargs={"pk": self.object.pk})
    
class ItemDeleteView(View):
    def post(self, request, pk):
        print("Deleting item with pk:", pk)
        try:
            item = Item.objects.get(id=pk)
            item.delete()
        except Item.DoesNotExist:
            pass
        return redirect('home')