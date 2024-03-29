# Generated by Django 4.1.7 on 2023-03-07 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow_statuses',
            fields=[
                ('b_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('b_status_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Id_types',
            fields=[
                ('t_id', models.AutoField(primary_key=True, serialize=False)),
                ('t_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item_categories',
            fields=[
                ('item_cate_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_cate_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item_statuses',
            fields=[
                ('item_status_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_status_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_privileges',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('u_id', models.AutoField(primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=100, unique=True)),
                ('u_password', models.CharField(max_length=100)),
                ('u_email', models.EmailField(max_length=100)),
                ('u_tel', models.IntegerField()),
                ('u_created_at', models.DateTimeField(auto_now_add=True)),
                ('u_updated_at', models.DateTimeField(auto_now=True)),
                ('u_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_eq_borrow.departments')),
                ('u_faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_eq_borrow.faculties')),
                ('u_privilege', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_eq_borrow.user_privileges')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100)),
                ('item_description', models.TextField()),
                ('item_note', models.TextField()),
                ('item_img_id', models.ImageField(upload_to='')),
                ('item_created_at', models.DateTimeField(auto_now_add=True)),
                ('item_updated_at', models.DateTimeField(auto_now=True)),
                ('item_borrow_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_eq_borrow.borrow_statuses')),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_eq_borrow.item_categories')),
                ('item_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_eq_borrow.departments')),
                ('item_faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_eq_borrow.faculties')),
                ('item_id_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_eq_borrow.id_types')),
                ('item_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_eq_borrow.item_statuses')),
            ],
        ),
        migrations.CreateModel(
            name='Borrow_info',
            fields=[
                ('b_id', models.AutoField(primary_key=True, serialize=False)),
                ('b_location', models.TextField()),
                ('b_note', models.TextField()),
                ('b_borrow_time', models.DateTimeField()),
                ('b_return_time', models.DateTimeField()),
                ('b_created_at', models.DateTimeField(auto_now_add=True)),
                ('b_updated_at', models.DateTimeField(auto_now=True)),
                ('b_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_eq_borrow.items')),
                ('b_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab_eq_borrow.users')),
            ],
        ),
    ]
