# Generated by Django 4.2 on 2023-04-30 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BehaviorTroubleTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrogant_impolite', models.TextField(db_column='arrogant_impolite')),
                ('angry_unexpected_behavior', models.TextField(db_column='angry_unexpected_behavior')),
                ('sensitive_criticism', models.TextField(db_column='sensitive_criticism')),
                ('pout_sulk_easily', models.TextField(db_column='pout_sulk_easily')),
                ('moody', models.TextField(db_column='moody')),
                ('brawler', models.TextField(db_column='brawler')),
                ('deny_mistakes_blame_others', models.TextField(db_column='deny_mistakes_blame_others')),
                ('few_relations_school', models.TextField(db_column='few_relations_school')),
            ],
            options={
                'db_table': 'behavior_trouble_teacher',
            },
        ),
        migrations.CreateModel(
            name='FormAbrTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restless_squirms_chair', models.TextField(db_column='restless_squirms_chair')),
                ('angry_unexpected_behavior', models.TextField(db_column='angry_unexpected_behavior')),
                ('distracted', models.TextField(db_column='distracted')),
                ('annoy_students', models.TextField(db_column='annoy_students')),
                ('pout_sulk_easily', models.TextField(db_column='pout_sulk_easily')),
                ('moody', models.TextField(db_column='moody')),
                ('goes_left_right', models.TextField(db_column='goes_left_right')),
                ('easily_turn_on_impulsive', models.TextField(db_column='easily_turn_on_impulsive')),
                ('trouble_finishing_things', models.TextField(db_column='trouble_finishing_things')),
                ('upset_easily_make_effort', models.TextField(db_column='upset_easily_make_effort')),
            ],
            options={
                'db_table': 'form_abr_teacher',
            },
        ),
        migrations.CreateModel(
            name='FormTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('score', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'form_teachers',
            },
        ),
        migrations.CreateModel(
            name='InattentionTroubleTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distracted', models.TextField(db_column='distracted')),
                ('dreamer', models.TextField(db_column='dreamer')),
                ('led_by_others', models.TextField(db_column='led_by_others')),
                ('trouble_guiding_others', models.TextField(db_column='trouble_guiding_others')),
                ('trouble_finishing_things', models.TextField(db_column='trouble_finishing_things')),
                ('immature', models.TextField(db_column='immature')),
                ('upset_easily_make_effort', models.TextField(db_column='upset_easily_make_eff')),
                ('has_learning_difficulties', models.TextField(db_column='has_learning_difficulties')),
                ('form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formteacher.formteacher')),
            ],
            options={
                'db_table': 'inattention_form_teacher',
            },
        ),
        migrations.CreateModel(
            name='HyperActivityTroubleTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restless_squirms_chair', models.TextField(db_column='restless_squirms_chair')),
                ('inappropriate_noises', models.TextField(db_column='inappropriate_noises')),
                ('immediately_satisfied_needs', models.TextField(db_column='immediately_satisfied_needs')),
                ('annoy_students', models.TextField(db_column='annoy_students')),
                ('goes_left_right', models.TextField(db_column='goes_left_right')),
                ('easily_turn_on_impulsive', models.TextField(db_column='easily_turn_on_impulsive')),
                ('excessive_attention_from_teacher', models.TextField(db_column='excessive_attention_from_teacher')),
                ('form', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='formteacher.formteacher')),
            ],
            options={
                'db_table': 'hyperactivity_trouble_teacher',
            },
        ),
    ]
