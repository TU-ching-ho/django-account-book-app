from django.shortcuts import render, redirect
from .forms import ExpenseModelForm
from .models import Expense
from django.db.models import Sum
# Create your views here.


def index(request):
    expenses = Expense.objects.all()  # 查詢所有資料
    summary = Expense.objects.aggregate(Sum('price'))['price__sum']
    form = ExpenseModelForm()
    if request.method == "POST":
        form = ExpenseModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/#")
   # print(summary)
    context = {
        'form': form,
        'expenses': expenses,
        'sum': summary
    }
    return render(request, 'expenses/index.html', context)


def update(request, id):
    expense = Expense.objects.get(id=id)
    form = ExpenseModelForm(instance=expense)
    if request.method == 'POST':
        form = ExpenseModelForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'expenses/update.html', context)


def delete(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == "POST":
        expense.delete()
        return redirect('/')
    context = {
        'expense': expense
    }
    return render(request, 'expenses/delete.html', context)
