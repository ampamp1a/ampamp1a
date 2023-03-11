# Generated by Django 4.1.7 on 2023-03-11 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab_eq_borrow', '0004_user_groups_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='user',
            name='u_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='lab_eq_borrow.department'),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_email',
            field=models.EmailField(db_column='u_email', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_faculty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='lab_eq_borrow.facultie'),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_privilege',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='lab_eq_borrow.user_privilege'),
        ),
    ]
