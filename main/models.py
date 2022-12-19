from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name

class Chapters(models.Model):
    course = models.ForeignKey(Courses, related_name="chapter", on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    slug = models.SlugField()

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"

    def __str__(self):
        return self.name

class Summary(models.Model):
    course = models.ForeignKey(Courses, related_name="summary", on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapters, related_name="summary", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    body = RichTextField()
    isverified = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Summaries"

    def __str__(self):
        return self.course.name

class Quiz(models.Model):
    course = models.ForeignKey(Courses, related_name="quiz", on_delete=models.CASCADE)
    name = models.CharField(max_length=2000)

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name

class Question(models.Model):
    course = models.ForeignKey(Courses, related_name="question", on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name="question", on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.quiz.name

class QuestionStem(models.Model):
    question = models.ForeignKey(Question, related_name="stem", on_delete=models.CASCADE)
    body = models.CharField(max_length=20000)
    ans = models.BooleanField(default=False)

    def __str__(self):
        return self.question.name

class PracticeQuestions(models.Model):
    course = models.ForeignKey(Courses, related_name="theory", on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapters, related_name="theory", on_delete=models.CASCADE)
    question = models.TextField()
    image1 = models.URLField(blank=True, null=True)
    image2 = models.URLField(blank=True, null=True)
    image3 = models.URLField(blank=True, null=True)
    explanation = RichTextField()

    class Meta:
        verbose_name = "Theory"
        verbose_name_plural = "Theories"

    def __str__(self):
        return self.course.name

