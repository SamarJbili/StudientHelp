from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.views.generic import View ,ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Stage, Logement , Transport
from django.db.models import Q
from .models import Stage, Logement, ÉvenClub, ÉvenSocial, Transport, Recommandation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Comment, Like

# Create your views here.


class acceuilView(ListView):
    model = Post
    template_name = 'acceuil.html' 
 
def inscription(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès!')
            return redirect('acceuil')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/inscription.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Met à jour la session de l'utilisateur pour éviter la déconnexion
            messages.success(request, 'Votre mot de passe a été changé avec succès!')
            return redirect('acceuil')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registration/change_password.html', {'form': form})


class EvenementCulturelCreateView(LoginRequiredMixin,CreateView):
    model = ÉvenClub
    template_name = 'forms/evenementCult_form.html'
    fields = ['Title','Type', 'Image', 'Description','Intitulé','Lieu','ContactInfo','Club']
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    success_url = reverse_lazy('eventCult-list')  # Mettez à jour avec votre URL de succès

class EvenementScientifiqueCreateView(LoginRequiredMixin,CreateView):
    model = ÉvenSocial
    template_name = 'forms/evenementSc_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    fields = ['Title', 'Type',  'Image','Description','Intitulé','Lieu','ContactInfo','Prix']
    success_url = reverse_lazy('eventSc-list')  # Mettez à jour avec votre URL de succès

class TransportCreateView(LoginRequiredMixin,CreateView):
    model = Transport
    template_name = 'forms/transport_form.html'
    success_url = reverse_lazy('transport-list') # Mettez à jour avec votre URL de succès
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    fields = ['Title',  'Type', 'Image', 'Départ', 'Destination', 'Heure_dep', 'Nbre_sièges', 'Contactinfo']

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Stage, Post
from django.contrib.auth.mixins import LoginRequiredMixin

class StageCreateView(LoginRequiredMixin, CreateView):
    model = Stage
    template_name = 'forms/stage_form.html'  # Assurez-vous que votre modèle a un formulaire associé à ce modèle
    fields = ['Title', 'Type', 'Image', 'Stage_type', 'Société', 'Durée', 'Sujet', 'Contactinfo', 'Spécialité']
    success_url = reverse_lazy('stage-list')  # Mettez à jour avec votre URL de succès

    def form_valid(self, form):
        # Récupérer l'instance de stage créée
        stage_instance = form.save(commit=False)
        stage_instance.author = self.request.user

        # Enregistrer le stage
        stage_instance.save()

        # Créer une instance de post associée au stage
        post_instance = Post.objects.create(
            Title=stage_instance.Title,
            Type=stage_instance.Type,
            Image=stage_instance.Image,
            author=self.request.user
        )

        # Mettre à jour l'instance de stage avec l'ID du post associé
        stage_instance.post = post_instance
        stage_instance.save()

        return super().form_valid(form)

from django.views.generic import CreateView
from .models import Logement, Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

class LogementCreateView(LoginRequiredMixin, CreateView):
    model = Logement
    template_name = 'forms/logement_form.html'
    success_url = reverse_lazy('logement-list')  # Mettez à jour avec votre URL de succès
    fields = ['Title', 'Type', 'Image', 'Localisation', 'Description', 'Contactinfo']

    def form_valid(self, form):
        # Récupérer l'instance de post créée
        post = Post.objects.create(
            Title=form.cleaned_data['Title'],
            Type=form.cleaned_data['Type'],
            Image=form.cleaned_data['Image'],
            author=self.request.user
        )
        # Enregistrer l'ID du post dans le formulaire Logement
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)


class LogementListView(ListView):
    model = Logement
    template_name = 'List/logementList.html' 

 
class StageListView(ListView):
    model = Stage
    template_name = 'List/StageList.html' 

 
 
class TransportListView(ListView):
    model = Transport
    template_name = 'List/TransportList.html' 

     
class eventCultView(ListView):
    model = ÉvenClub
    template_name = 'List/EvenementCulturelList.html' 


class eventScView(ListView):
    model = ÉvenSocial
    template_name = 'List/EvenementScientifiqueList.html' 

class PostScView(ListView):
    model = ÉvenSocial
    template_name = 'acceuil' 


class EvenementCulturelUpdateView(LoginRequiredMixin,UpdateView):
    model = ÉvenClub
    template_name = 'List/update/updatelogement.html'
    fields = ['Title','Type', 'Image', 'Description','Intitulé','Lieu','ContactInfo','Club']
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    success_url = reverse_lazy('mespost-view')  # Mettez à jour avec votre URL de succès

class EvenementScientifiqueUpdateView(LoginRequiredMixin,UpdateView):
    model = ÉvenSocial
    template_name = 'List/update/updatelogement.html'
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    fields = ['Title', 'Type',  'Image','Description','Intitulé','Lieu','ContactInfo','Prix']
    success_url = reverse_lazy('mespost-view')  # Mettez à jour avec votre URL de succès

class TransportUpdateView(LoginRequiredMixin,UpdateView):
    model = Transport
    template_name = 'forms/transport_form.html'
    success_url = reverse_lazy('mespost-view') # Mettez à jour avec votre URL de succès
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    fields = ['Title',  'Type', 'Image', 'Départ', 'Destination', 'Heure_dep', 'Nbre_sièges', 'Contactinfo']

class StageUpdateView(LoginRequiredMixin,UpdateView):
    model = Stage
    template_name = 'forms/stage_from.html'
    fields = ['Title', 'Type', 'Image', 'Stage_type', 'Société', 'Durée', 'Sujet', 'Contactinfo', 'Spécialité']
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    success_url = reverse_lazy('mespost-view')# Mettez à jour avec votre URL de succès

class LogementUpdateView(LoginRequiredMixin,UpdateView):
    model = Logement
    template_name ='List/update/updatelogement.html'
    success_url = reverse_lazy('mespost-view')# Mettez à jour avec votre URL de succès
    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    fields = ['Title','Type', 'Image', 'Localisation', 'Description', 'Contactinfo']







class eventScDeleteView(DeleteView):
    model = ÉvenSocial
    success_url = reverse_lazy('mespost-view')# Mettez à jour avec votre URL de succès
    template_name = 'List/confirmdeleteeventSc.html'

class eventCultDeleteView(DeleteView):
    model = ÉvenClub
    success_url = reverse_lazy('mespost-view')# Mettez à jour avec votre URL de succès
    template_name = 'List/confirmdeleteeventcult.html'


class logementDeleteView(DeleteView):
    model = Logement
    success_url = reverse_lazy('mespost-view')# Mettez à jour avec votre URL de succès
    template_name = 'List/confirmdelete.html'


class StageDeleteView(DeleteView):
    model = Stage
    success_url = reverse_lazy('mespost-view')# Mettez à jour avec votre URL de succès
    template_name = 'List/confirmdeletestage.html'


class TransportDeleteView(DeleteView):
    model =Transport
    success_url = reverse_lazy('mespost-view')# Mettez à jour avec votre URL de succès
    template_name = 'List/confirmdeletetransport.html'




def inputform (request):
    return render(request,'List/inputform.html')

class MesPostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        stage_posts = Stage.objects.filter(author=user)
        logement_posts = Logement.objects.filter(author=user)        
        club_posts = ÉvenClub.objects.filter(author=user)
        social_posts = ÉvenSocial.objects.filter(author=user)
        transport_posts = Transport.objects.filter(author=user)
        recommandation_posts = Recommandation.objects.filter(author=user)

        context = {
            'stage_posts': stage_posts,
            'logement_posts': logement_posts,
            'club_posts': club_posts,
            'social_posts': social_posts,
            'transport_posts': transport_posts,
            'recommandation_posts': recommandation_posts,
        }

        return render(request,'List/mespost.html', context)
  
def search(request):
    query = request.GET.get('q')
    results = []

    if query:
        # Search in all relevant models using Django's Q operator
        results += Logement.objects.filter(Q(Title__icontains=query))
        results += Stage.objects.filter(Q(Title__icontains=query))
        results += ÉvenClub.objects.filter(Q(Title__icontains=query))
        results += ÉvenSocial.objects.filter(Q(Title__icontains=query))
        results += Transport.objects.filter(Q(Title__icontains=query))

  
    context = {
        'results': results,
        'query': query,
    }

    return render(request, 'List/search_results.html', context)







def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès!')
            return redirect('acceuil')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/inscription.html', {'form': form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Met à jour la sessio
            messages.success(request, 'Votre mot de passe a été changé avec succès!')
            return redirect('acceuil')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registration/change_password.html', {'form': form})

from django.shortcuts import get_object_or_404

from django.shortcuts import get_object_or_404

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    success_url = reverse_lazy('acceuil')
    template_name = 'add_comment.html'

    def form_valid(self, form):
        # Obtenir l'objet Post associé à partir de l'URL
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        # Ajouter l'auteur et l'objet de contenu au formulaire de commentaire
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)



class LikeView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete()
        return redirect('post-detail', pk=self.kwargs['post_id'])

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
