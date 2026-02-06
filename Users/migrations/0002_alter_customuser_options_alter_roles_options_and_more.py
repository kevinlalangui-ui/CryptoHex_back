import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-is_superuser', 'is_active', 'email'], 'verbose_name': '1. Usuario', 'verbose_name_plural': '1. Usuarios'},
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'ordering': ['nombre', 'is_active'], 'verbose_name': '2. Role', 'verbose_name_plural': '2. Roles'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Users.roles'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True, help_text='(Obligatorio si queremos que el usuario pueda acceder a su cuenta)', verbose_name='¿Está activo?'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='¿Está activo?'),
        ),
    ]
