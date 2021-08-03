# Generated by Django 3.2.1 on 2021-08-03 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnxityTroubleParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('afraidNewThings', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='afraid_new_things')),
                ('shy', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')])),
                ('worryMuch', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='worry_much')),
                ('beingCrashedManipulated', models.TextField(db_column='being_crashed_manipulated')),
            ],
            options={
                'db_table': 'anxity_trouble_parent',
            },
        ),
        migrations.CreateModel(
            name='BehaviorTroubleParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('insolentWithGrownUps', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='insolent_wth_grown_ups')),
                ('feelsAttackedDefensive', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='feels_attacked_defensive')),
                ('destructive', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='descructive')),
                ('denyMistakesBlameOthers', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='deny_mistakes_blame_others')),
                ('quarrelsomeGetInvolvedFight', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='quarrelsome_get_involved_fight')),
                ('bullyIntimidateComrades', models.TextField(db_column='bully_intimidate_comrades')),
                ('constantlyFight', models.TextField(db_column='constantly_fight')),
                ('unhappy', models.TextField(db_column='unhappy')),
            ],
            options={
                'db_table': 'behavior_trouble_parent',
            },
        ),
        migrations.CreateModel(
            name='ExtraTroubleParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('chewMibThings', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='chew_mib_things')),
                ('troubleMakeKeepFriends', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='trouble_make_keep_friends')),
                ('suckChewThings', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='suck_chew_things')),
                ('dreamer', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='dreamer')),
                ('lieMadeUpStories', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='lie_made_up_stories')),
                ('getTroublesMoreThanOthers', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='get_troubles_more_than_others')),
                ('speakLikeBabyStutters', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='speak_like_baby_stutters')),
                ('poutSulkEasily', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='pout_sulk_easily')),
                ('stealThings', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='steal_things')),
                ('disobeyReluctantlyObey', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='disobey_reluctantly_obey')),
                ('easilyWrinkledEasilyAngry', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='easily_wrinkled_easily_angry')),
                ('troubleFinishRepetitiveActivity', models.TextField(db_column='trouble_finish_repetitive_activity')),
                ('cruel', models.TextField(db_column='cruel')),
                ('immature', models.TextField(db_column='immature')),
                ('breakRules', models.TextField(db_column='break_rules')),
                ('notGetAlongWithBrothers', models.TextField(db_column='not_get_along_with_brothers')),
                ('feedingProblems', models.TextField(db_column='feeding_problems')),
                ('sleepingProblems', models.TextField(db_column='sleeping_problems')),
                ('feelWrongedCryOutInjustice', models.TextField(db_column='feel_wronged_cry_out_injustice')),
                ('bragsBoastful', models.TextField(db_column='brags_boastful')),
                ('bowelMovementProblems', models.TextField(db_column='bowel_movement_problems')),
            ],
            options={
                'db_table': 'extra_trouble_parent',
            },
        ),
        migrations.CreateModel(
            name='HyperActivityTroubleParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('excitableImpulsive', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='excitable_impulsive')),
                ('cryOftenEasily', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='suck_chew_things')),
                ('squirms', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='squirms')),
                ('restlessNeedsDoSomething', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')])),
                ('destructive', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='descructive')),
                ('troubleFinishingThings', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='trouble_finishing_things')),
                ('easilyBeingDistracted', models.TextField(db_column='easily_being_distracted')),
                ('moody', models.TextField(db_column='moody')),
                ('enabilityFinishWhenDoEffort', models.TextField(db_column='enability_finish_when_do_effort')),
                ('disturbOtherChildren', models.TextField(db_column='disrurb_other_children')),
            ],
            options={
                'db_table': 'hyperactivity_trouble_parent',
            },
        ),
        migrations.CreateModel(
            name='ImpulsivityTroubleParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('excitableImpulsive', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='excitable_impulsive')),
                ('wantDominate', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='want_dominate')),
                ('squirms', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='squirms')),
                ('restlessNeedsDoSomething', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')])),
            ],
            options={
                'db_table': 'impulisivity_trouble_parent',
            },
        ),
        migrations.CreateModel(
            name='LearningTroubleParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('hasLearningDifficulties', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='has_learning_difficulties')),
                ('troubleFinishingThings', models.TextField(choices=[('never', 'never'), ('sometimes', 'sometimes'), ('usual', 'usual'), ('always', 'always')], db_column='trouble_finishing_things')),
                ('easilyBeingDistracted', models.TextField(db_column='easily_being_distracted')),
                ('enabilityFinishWhenDoEffort', models.TextField(db_column='enability_finish_when_do_effort')),
            ],
            options={
                'db_table': 'learning_trouble_parent',
            },
        ),
        migrations.CreateModel(
            name='SomatisationTroubleParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('headaches', models.TextField(db_column='headaches')),
                ('upsetStomach', models.TextField(db_column='upset_stomach')),
                ('physicalAches', models.TextField(db_column='physical_aches')),
                ('vomitingNausea', models.TextField(db_column='vomiting_nausea')),
            ],
            options={
                'db_table': 'somatisation_trouble_parent',
            },
        ),
    ]
