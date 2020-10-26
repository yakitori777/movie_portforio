from django.db import models

# Create your models here.
class MovieDetailModel(models.Model):
    #映画タイトル
    title = models.CharField(max_length=100)
    #映画あらすじ
    story = models.TextField()
    #画像
    images = models.ImageField(upload_to='')
    #動画
    videos = models.CharField(max_length=100)
    #リリース日
    release = models.DateTimeField()
    #上映時間
    running_time = models.IntegerField()
    #ジャンル
    genre = models.CharField(max_length=20)
    #監督
    director = models.CharField(max_length=50)
    #キャスト
    cast = models.TextField()
    #上映中か未公開かのフラグ
    show_flg = models.CharField(max_length=20)
    #年齢指定
    resting = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title