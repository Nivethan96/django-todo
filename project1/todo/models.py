from django.db import models

# Todo Model
class Todo(models.Model):
	todo_text = models.CharField(max_length=200)
	added_date = models.DateTimeField('date added')

	def __str__(self):
		return self.todo_text	

