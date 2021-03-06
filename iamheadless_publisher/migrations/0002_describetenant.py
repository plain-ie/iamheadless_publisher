# Generated by Django 4.0.3 on 2022-04-21 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iamheadless_projects', '0002_create_projects_tenants'),
        ('iamheadless_publisher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescribeTenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='described_tenant', to='iamheadless_publisher.item')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='described_by_item', to='iamheadless_projects.tenant')),
            ],
        ),
    ]
