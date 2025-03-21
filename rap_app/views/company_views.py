from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ..forms.company_form import CompanyForm
from ..models.company import Company

# Liste des entreprises
class CompanyListView(ListView):
    model = Company
    template_name = 'company/company_list.html'
    context_object_name = 'companies'
    ordering = ['-created_at']

# Détail d'une entreprise
class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/company_detail.html'

# Création d'une entreprise
class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company_form.html'
    success_url = reverse_lazy('company-list')

# Mise à jour d'une entreprise
class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company_form.html'
    success_url = reverse_lazy('company-list')

# Suppression d'une entreprise
class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company/company_confirm_delete.html'
    success_url = reverse_lazy('company-list')
