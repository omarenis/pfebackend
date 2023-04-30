# Generated by Django 4.2 on 2023-04-30 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('formparent', '0001_initial'),
        ('gestionpatient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='somatisationtroubleparent',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionpatient.patient'),
        ),
        migrations.AddField(
            model_name='learningtroubleparent',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionpatient.patient'),
        ),
        migrations.AddField(
            model_name='hyperactivitytroubleparent',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionpatient.patient'),
        ),
        migrations.AddField(
            model_name='formabrparent',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionpatient.patient'),
        ),
        migrations.AddField(
            model_name='behaviortroubleparent',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionpatient.patient'),
        ),
        migrations.AddField(
            model_name='anxitytroubleparent',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionpatient.patient'),
        ),
    ]
