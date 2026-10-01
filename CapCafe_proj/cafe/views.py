from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import MenuItem, Category, Order
from .forms import MenuItemForm
# Create your views here.

def home_view(request):
    featured_items = MenuItem.objects.filter(is_available=True)[:4]
    return render(request, 'cafe/home.html', {'featured_items': featured_items})

def menu_list_view(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    
    items = MenuItem.objects.filter(is_available=True)
    if query:
        items = items.filter(name__icontains=query)
    if category_id:
        items = items.filter(category_id=category_id)
        
    categories = Category.objects.all()
    context = {'items': items, 'categories': categories, 'query': query, 'selected_category': category_id}
    return render(request, 'cafe/menu_list.html', context)

class MenuItemDetailView(DetailView):
    model = MenuItem
    template_name = 'cafe/menu_detail.html'
    context_object_name = 'item'

class MenuItemCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'cafe/menu_form.html'
    success_url = reverse_lazy('menu_list')

class MenuItemUpdateView(UpdateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'cafe/menu_form.html'
    success_url = reverse_lazy('menu_list')

class MenuItemDeleteView(DeleteView):
    model = MenuItem
    template_name = 'cafe/menu_confirm_delete.html'
    success_url = reverse_lazy('menu_list')

def staff_dashboard_view(request):
    orders = Order.objects.all().order_by('-created_at')
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        new_status = request.POST.get('status')
        order = get_object_or_404(Order, id=order_id)
        order.status = new_status
        order.save()
        return redirect('staff_dashboard')
    return render(request, 'cafe/dashboard.html', {'orders': orders})