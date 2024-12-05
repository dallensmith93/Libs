from django.db import models

# Create your models here.


class Lib1(models.Model):

     def __str__ (self):
        return self.lib_adj
        
     def __str__ (self):
        return self.lib_verb 

     def __str__ (self):
        return self.lib_adj2

     def __str__ (self):
        return self.lib_Noun


     lib_adj = models.CharField(max_length=40)
     lib_verb = models.CharField(max_length=40)
     lib_adj2 = models.CharField(max_length=40)
     lib_Noun = models.CharField(max_length=40)

class Lib2(models.Model):

     def __str__ (self):
        return self.lib2_Noun
        
     def __str__ (self):
        return self.lib2_verb

     def __str__ (self):
        return self.lib2_adj

     lib2_Noun = models.CharField(max_length=40)
     lib2_verb = models.CharField(max_length=40)
     lib2_adj = models.CharField(max_length=40)

class Lib3(models.Model):
     def __str__ (self):
        return self.lib3_adj

     def __str__ (self):
        return self.lib3_adj2

     def __str__ (self):
        return self.lib3_body
        
     def __str__ (self):
        return self.lib3_adj3

     

     lib3_adj = models.CharField(max_length=40)
     lib3_adj2 = models.CharField(max_length=40)
     lib3_body = models.CharField(max_length=40)
     lib3_adj3 = models.CharField(max_length=40)
    

