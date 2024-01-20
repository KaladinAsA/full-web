from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        
        
    def save(self, commit=True, author=None, article=None):
        comment = super().save(commit=False)
        comment.author = author
        comment.article = article
        
        if commit:
            comment.save()
            
        return comment
        