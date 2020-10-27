# Generated by Django 3.1.1 on 2020-10-09 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_operation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userleavingmessage',
            name='user',
            field=models.ForeignKey(help_text='$显示字段$__username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='userfav',
            name='goods',
            field=models.ForeignKey(help_text='$显示字段$__name', on_delete=django.db.models.deletion.CASCADE, to='goods.goods', verbose_name='商品'),
        ),
        migrations.AddField(
            model_name='userfav',
            name='user',
            field=models.ForeignKey(help_text='$显示字段$__username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='user',
            field=models.ForeignKey(help_text='$显示字段$__username', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterUniqueTogether(
            name='userfav',
            unique_together={('user', 'goods')},
        ),
    ]