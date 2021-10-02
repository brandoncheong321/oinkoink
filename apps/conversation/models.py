from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Conversation(models.Model):

    users = models.ManyToManyField(User, related_name = 'conversations')
    modified_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-modified_at']


class ConversationMessage(models.Model):

    conversation = models.ForeignKey(Conversation, related_name = 'messages', on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True) 
    # on_delete arg: it deletes the variable upon deletion of whatever class it references, e.g in this case, User 
    # (i.e if user deletes account, messages get deleted)
    created_by = models.ForeignKey(User, related_name = 'messages', on_delete = models.CASCADE)
    
    # messages displayed in order of chronology 
    class Meta:
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        self.conversation.save()

        super(ConversationMessage, self).save(*args, **kwargs)
