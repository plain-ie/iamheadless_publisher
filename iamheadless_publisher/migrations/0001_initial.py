# Generated by Django 4.0.1 on 2022-03-03 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('iamheadless_projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(blank=True, default=dict, null=True)),
                ('item_type', models.CharField(db_index=True, max_length=4096)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iamheadless_publisher_items', to='iamheadless_projects.project')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='iamheadless_publisher_items', to='iamheadless_projects.tenant')),
            ],
        ),
        migrations.CreateModel(
            name='TextLookupIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(db_index=True, max_length=4096)),
                ('value', models.CharField(max_length=4096)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_lookup_indexes', to='iamheadless_publisher.item')),
            ],
        ),
        migrations.CreateModel(
            name='PublisherProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='publishing_app', to='iamheadless_projects.project')),
            ],
        ),
        migrations.CreateModel(
            name='ItemRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='iamheadless_publisher.item')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='iamheadless_publisher.item')),
            ],
        ),
        migrations.CreateModel(
            name='FloatLookupIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(db_index=True, max_length=4096)),
                ('value', models.DecimalField(decimal_places=100000000000000000000, max_digits=100000000000000000000)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='float_lookup_indexes', to='iamheadless_publisher.item')),
            ],
        ),
        migrations.CreateModel(
            name='DateTimeLookupIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(db_index=True, max_length=4096)),
                ('value', models.DateTimeField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='datetime_lookup_indexes', to='iamheadless_publisher.item')),
            ],
        ),
        migrations.CreateModel(
            name='DateLookupIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(db_index=True, max_length=4096)),
                ('value', models.DateField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='date_lookup_indexes', to='iamheadless_publisher.item')),
            ],
        ),
        migrations.CreateModel(
            name='BooleanLookupIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(db_index=True, max_length=4096)),
                ('value', models.BooleanField(default=None)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boolean_lookup_indexes', to='iamheadless_publisher.item')),
            ],
        ),
    ]
