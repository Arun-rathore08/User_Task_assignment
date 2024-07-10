from django.db import models

Tasks = [("Pending", "pending"), ("Done", "done"),]

class Task(models.Model):
    task_details = models.TextField(max_length=50)
    task_type = models.CharField(max_length=50, choices=Tasks)
    
    def __str__(self) -> str:
        return str(self.task_details)
    
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()
    Id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
    
    
    class Meta:
        db_table = "User"
    
    def __str__(self) -> str:
        return str(self.name)
    
