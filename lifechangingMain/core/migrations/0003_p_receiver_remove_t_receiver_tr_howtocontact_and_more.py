# Generated by Django 5.0.3 on 2024-07-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_p_donor_d_category_remove_p_donor_d_regno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_receiver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('R_name', models.CharField(blank=True, max_length=100, null=True)),
                ('R_item_name', models.CharField(blank=True, max_length=100, null=True)),
                ('R_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('R_reginfo', models.CharField(blank=True, max_length=100, null=True)),
                ('R_item', models.CharField(blank=True, choices=[('select', 'Select'), ('money', 'Money'), ('clothes', 'Clothes'), ('food items', 'Food Items'), ('others', 'Others')], max_length=50, null=True)),
                ('R_photo_logo', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('R_contact', models.IntegerField(blank=True, null=True)),
                ('R_description', models.CharField(blank=True, max_length=600, null=True)),
                ('R_location', models.CharField(blank=True, max_length=100, null=True)),
                ('R_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='t_receiver',
            name='tr_howtocontact',
        ),
        migrations.AddField(
            model_name='t_receiver',
            name='tr_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='t_receiver',
            name='tr_description',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='t_receiver',
            name='tr_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='t_receiver',
            name='tr_item',
            field=models.CharField(blank=True, choices=[('select', 'Select'), ('money', 'Money'), ('clothes', 'Clothes'), ('food items', 'Food Items'), ('others', 'Others')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='t_receiver',
            name='tr_item_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='t_receiver',
            name='tr_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='t_receiver',
            name='tr_photo_logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='P_reciever',
        ),
    ]
