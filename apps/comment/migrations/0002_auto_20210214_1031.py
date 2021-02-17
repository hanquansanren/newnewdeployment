# Generated by Django 2.2.13 on 2021-02-14 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20210214_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='create_p',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_create', to=settings.AUTH_USER_MODEL, verbose_name='提示创建者'),
        ),
        migrations.AddField(
            model_name='notification',
            name='get_p',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_get', to=settings.AUTH_USER_MODEL, verbose_name='提示接收者'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articlecomment_related', to=settings.AUTH_USER_MODEL, verbose_name='评论人'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='belong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comments', to='blog.Article', verbose_name='所属文章'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articlecomment_child_comments', to='comment.ArticleComment', verbose_name='父评论'),
        ),
        migrations.AddField(
            model_name='articlecomment',
            name='rep_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articlecomment_rep_comments', to='comment.ArticleComment', verbose_name='回复'),
        ),
    ]
