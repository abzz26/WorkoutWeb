from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from WebAppProject.models import Category, Post, Comment, UserProfile
from django.core.urlresolvers import reverse
from WebAppProject.forms import PostForm, CommentForm
from WebAppProject.forms import UserForm,UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from WebAppProject.forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template



category_list = Category.objects.order_by()[:6]
cat_dict = {}
for category in category_list:
    try:
        posts = Post.objects.filter(category=category).order_by('-likes')[:5]
        cat_dict[category] = posts
    except Category.DoesNotExist:
        cat_dict[category] = None

def index(request):
    context_dict = {}
    context_dict['categories'] = cat_dict
    return render(request,'workoutweb/index.html', context_dict)

def about(request):
    context_dict = {}
    context_dict['categories'] = cat_dict
    return render(request, 'workoutweb/about.html', context_dict)

@login_required
def account(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    userprofile = UserProfile.objects.filter(user_id=request.user.id)

    return render(request, 'workoutweb/account.html', {'userprofile':userprofile})

def nearestgym(request):
    context_dict = {}
    context_dict['categories'] = cat_dict
    return render(request, 'workoutweb/nearest-gym.html', context_dict)

def faq(request):
    context_dict = {}
    context_dict['categories'] = cat_dict
    return render(request, 'workoutweb/faq.html', context_dict)

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    context_dict['categories'] = cat_dict
    context_dict['repeat'] = None
    try:
        category = Category.objects.get(slug=category_name_slug)
        posts = Post.objects.filter(category=category).order_by('-likes')
        context_dict['category'] = category
        context_dict['posts'] = posts
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['posts'] = None

    try:
        category =  Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    form = PostForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = PostForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            if category:
                try:
                    post = form.save(commit=False)
                    post.category = category
                    post.save()
                    context_dict['repeat'] = None
                except:
                    context_dict['repeat'] = 'Post title exists.'
        else:
            print(form.errors)
    context_dict['form'] = form
    return render(request, 'workoutweb/category.html', context_dict)


def show_post(request, post_name_slug, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    context_dict['categories'] = cat_dict
    try:
        post = Post.objects.get(slug=post_name_slug)
        print post
        comments = Comment.objects.filter(post=post)
        context_dict['post'] = post
        context_dict['comments'] = comments
    except Post.DoesNotExist:
        context_dict['post'] = None
        context_dict['comments'] = None

    try:
        post =  Post.objects.get(slug=post_name_slug)
    except Post.DoesNotExist:
        post = None
    form = CommentForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # Have we been provided with a valid form?
        if form.is_valid():
            if post:
                comment = form.save(commit=False)
                comment.post = post
                if request.user.is_authenticated:
                    comment.user = request.user
                else:
                    comment.user = None
                comment.save()

    context_dict['form'] = form
    return render(request, 'workoutweb/post.html', context_dict)

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']


            else:

                print(user_form.errors, profile_form.errors)
            profile.save()
            registered = True
    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,'registration/registration_form.html',{'user_form': user_form,
                                                          'profile_form': profile_form,
                                                          'registered': registered})


def user_login(request):
    print "@@@@@@"
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'registration/login.html', {})


@login_required
def restricted(request):
    return render(request, 'workoutweb/restricted.html',{})

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.weight = '155'
    user.profile.height = '170'
    user.save()


def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))

def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
                , '')
            contact_email = request.POST.get(
                'contact_email'
                , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template =\
                get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Workout Web" + '',
                ['milsnorton@hotmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            return redirect('contact')
    return render(request, 'workoutweb/contact.html',{'categories': cat_dict,'form': form_class})
