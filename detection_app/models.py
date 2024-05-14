from django.db import models

# Create your models here.


class prompt_reply(models.Model):
    prompt = models.CharField(max_length=2000, blank=False, null=False)
    answer = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f"prompt:\n{self.prompt}\nreply: {self.answer}\n"

    class Meta:
        db_table = "prompt_reply"
