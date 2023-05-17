from djongo import models


'''
MongoDB 의 Document 를 활용가능한
Embedded Model 활용 컨벤션

아래 모델 Entry 가 해당 예시. (일대다 - 다대일 - 다대다 모델 관계에서 Embedded Model 활용)
'''


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        abstract = True


class MetaData(models.Model):
    pub_date = models.DateField()
    mod_date = models.DateField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    class Meta:
        abstract = True


class Author(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__ (self):
        return self.name


class Entry(models.Model):
    _id = models.ObjectIdField()
    blog = models.EmbeddedField(
        model_container=Blog,
    )
    meta_data = models.EmbeddedField(
        model_container=MetaData,
    )

    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()

    def __str__(self):
        return self.headline
