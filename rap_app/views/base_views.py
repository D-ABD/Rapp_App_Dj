from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

class CustomLoginRequiredMixin(LoginRequiredMixin):
    """Mixin personnalisé pour gérer les utilisateurs non connectés"""
    def handle_no_permission(self):
        # Ajouter un message d'erreur
        messages.error(self.request, "Vous devez être connecté pour accéder à cette page.")
        # Rediriger vers la page de connexion
        return redirect('login')  # Remplacez 'login' par le nom de votre URL de connexion

class BaseListView(CustomLoginRequiredMixin, ListView):
    """Vue de base pour les listes avec pagination"""
    paginate_by = 20
    template_name_suffix = '_list'


class BaseDetailView(CustomLoginRequiredMixin, DetailView):
    """Vue de base pour afficher un détail"""
    template_name_suffix = '_detail'


class BaseCreateView(CustomLoginRequiredMixin, CreateView):
    """Vue de base pour créer un objet"""

    def form_valid(self, form):
        """Ajoute un message de succès après la création"""
        response = super().form_valid(form)
        messages.success(self.request, f"{self.model._meta.verbose_name} créé avec succès.")
        return response


class BaseUpdateView(CustomLoginRequiredMixin, UpdateView):
    """Vue de base pour modifier un objet"""

    def form_valid(self, form):
        """Ajoute un message de succès après la modification"""
        response = super().form_valid(form)
        messages.success(self.request, f"{self.model._meta.verbose_name} mis à jour avec succès.")
        return response


class BaseDeleteView(CustomLoginRequiredMixin, DeleteView):
    """Vue de base pour supprimer un objet"""
    success_url = reverse_lazy('dashboard')

    def delete(self, request, *args, **kwargs):
        """Ajoute un message de succès après la suppression"""
        messages.success(request, f"{self.model._meta.verbose_name} supprimé avec succès.")
        return super().delete(request, *args, **kwargs)