from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Expense
from django.http import HttpResponse
from django.template import loader
from .forms import ExpenseForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    if request.method == 'POST':
        expense_form = ExpenseForm(data = request.POST)
        if expense_form.is_valid():
            expense = expense_form.save()
    latest_expense_list = Expense.objects.order_by('-expense_created')[:5]
    context = {
        'latest_expense_list':latest_expense_list,
    }
    return render(request,'expense/index.html', context)

def detail(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)
    return render(request, 'expense/detail.html', {'expense': expense})

class ExpenseListView(ListView):
    queryset = Expense.objects.all()
    context_object_name = 'expenses'
    paginate_by = 3
    template_name = 'excalci/expense/list.html'
    form_class = ExpenseForm

    def form_valid(self, form):
        return super(ExpenseForm, self).form_valid(form)

def expense_detail(request, expense_id):
    expense = get_object_or_404(Expense, pk=expense_id)

    return render(request, 'excalci/expense/detail.html', {'expense': expense})

class ExpenseCreate(CreateView):
    model = Expense
    fields = ['expense_name', 'expense_amount', '']
