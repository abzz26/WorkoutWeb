import unicodedata
from django import forms
from django.contrib.auth.models import User
from WebAppProject.models import Post, Category, Comment, UserProfile

# Post form to allow users to create post
# inheriting data from the Post model
class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the post.")
    content = forms.CharField(max_length=1024,
                              help_text="Please enter your post content.")
    class Meta:
        model = Post
        fields = ('title','content')

# Comment form to allow users and non users to create a comment on a post
# inheriting data from the Comment model
class CommentForm(forms.ModelForm):
        content = forms.CharField(max_length=1024,
                                    help_text="Please enter your comment.")
        class Meta:
            model = Comment
            fields = ( 'content',)

# Allows users to sign up for an account, using django registration redux
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta(object):
        model = User
        fields = ('username', 'email', 'password')

# Form that contains the data fields to be saved for the user
# inherting from the UserProfile model
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('height','weight', 'picture')

# Contact form which allows users to submit a query
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "What do you want to say?"