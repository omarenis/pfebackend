from django.db.models import CASCADE, ForeignKey, Model, OneToOneField, SET_NULL
from django.db.models.fields import FloatField, TextField, DateTimeField
from rest_framework.serializers import ModelSerializer
from common.models import create_model_serializer


class level1(Model):
    looks_at_pointed_item= TextField(null=False, db_column='looks_at_pointed_item')
    possibly_deaf = TextField(null=False, db_column='possibly_deaf')
    pretending_playing= TextField(null=False, db_column='pretending_playing')
    climbing_things= TextField(null=False, db_column='climbing_things')
    unusual_moves_next_to_eyes= TextField(null=False, db_column='unusual_moves_next_to_eyes')
    point_to_get_assistance= TextField(null=False, db_column='point_to_get_assistance')
    point_to_show_smth= TextField(null=False, db_column='point_to_show_smth')
    cares_abt_other_children= TextField(null=False, db_column='cares_abt_other_children')
    bring_smth_to_show= TextField(null=False, db_column='bring_smth_to_show')
    response_to_his_name= TextField(null=False, db_column='response_to_his_name')
    smiles_back= TextField(null=False, db_column='smiles_back')
    annoyed_by_daily_noise= TextField(null=False, db_column='annoyed_by_daily_noise')
    walks= TextField(null=False, db_column='walks')
    makes_eye_contact= TextField(null=False, db_column='makes_eye_contact')
    imitate_parent_action= TextField(null=False, db_column='imitate_parent_action')
    turn_head_like_parent= TextField(null=False, db_column='turn_head_like_parent')
    make_parent_watch= TextField(null=False, db_column='make_parent_watch')
    understand_assignments= TextField(null=False, db_column='understand_assignments')
    check_parent_reaction= TextField(null=False, db_column='check_parent_reaction')
    loves_dynamic_activities= TextField(null=False, db_column='loves_dynamic_activities')


class level1Serializer(ModelSerializer):
    class Meta:
        model = level1
        fields = '__all__'


class level2 (Model):
    turns_to_bell_when_busy= TextField(null=False, db_column='turns_to_bell_when_busy')
    place_3shapes_correctly= TextField(null=False, db_column='place_3shapes_correctly')
    place_4shapes_correctly= TextField(null=False, db_column='place_4shapes_correctly')
    place_5shapes_correctly= TextField(null=False, db_column='place_5shapes_correctly')
    place_6shapes_correctly= TextField(null=False, db_column='place_6shapes_correctly')
    animal_or_map_image= TextField(null=False, db_column='animal_or_map_image')
    boy_or_girl_image= TextField(null=False, db_column='boy_or_girl_image')
    sound_device_by_order= TextField(null=False, db_column='sound_device_by_order')
    match_5items_with_pic= TextField(null=False, db_column='match_5items_with_pic')
    find_smth_hidden= TextField(null=False, db_column='find_smth_hidden')
    hidden_food_under_cups= TextField(null=False, db_column='hidden_food_under_cups')
    identify_by_touching= TextField(null=False, db_column='identify_by_touching')
    copy_straight_lines= TextField(null=False, db_column='copy_straight_lines')
    copy_circle= TextField(null=False, db_column='copy_circle')
    copy_square= TextField(null=False, db_column='copy_square')
    copy_triangle= TextField(null=False, db_column='copy_triangle')
    copy_diamond= TextField(null=False, db_column='copy_diamond')
    copy_7letters= TextField(null=False, db_column='copy_7letters')
    draw_leg= TextField(null=False, db_column='draw_leg')
    write_his_name= TextField(null=False, db_column='write_his_name')
    cut_paper_by_scissor= TextField(null=False, db_column='cut_paper_by_scissor')
    intrested_in_images_book= TextField(null=False, db_column='intrested_in_images_book')
    silent_acting= TextField(null=False, db_column='silent_acting')
    matches_9letters= TextField(null=False, db_column='matches_9letters')
    cubes_by_color= TextField(null=False, db_column='cubes_by_color')
    shapes_by_color= TextField(null=False, db_column='shapes_by_color')
    classify_cards= TextField(null=False, db_column='classify_cards')
    reacts_to_imitated_movements= TextField(null=False, db_column='reacts_to_imitated_movements')
    reacts_to_imitated_sounds= TextField(null=False, db_column='reacts_to_imitated_sounds')
    repeat_3sounds= TextField(null=False, db_column='repeat_3sounds')
    repeat_2numbers= TextField(null=False, db_column='repeat_2numbers')
    repeat_2words= TextField(null=False, db_column='repeat_2words')
    achieve_3tasks_order= TextField(null=False, db_column='achieve_3tasks_order')


class level2Serializer(ModelSerializer):
    class Meta:
        model = level2
        fields = '__all__'