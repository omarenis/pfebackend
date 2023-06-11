from common.models import text_field
from common.services import Service
from .repositories import level1Repository,level2Repository


level1_fields ={
    'looks_at_pointed_item': text_field,
    'possibly_deaf': text_field,
    'pretending_playing': text_field,
    'climbing_things': text_field,
    'unusual_moves_next_to_eyes': text_field,
    'point_to_get_assistance': text_field,
    'point_to_show_smth': text_field,
    'cares_abt_other_children': text_field,
    'bring_smth_to_show': text_field,
    'response_to_his_name': text_field,
    'smiles_back': text_field,
    'annoyed_by_daily_noise': text_field,
    'walks': text_field,
    'makes_eye_contact': text_field,
    'imitate_parent_action': text_field,
    'turn_head_like_parent': text_field,
    'make_parent_watch': text_field,
    'understand_assignments': text_field,
    'check_parent_reaction': text_field,
    'loves_dynamic_activities': text_field,
}



level2_fields ={
    'turns_to_bell_when_busy': text_field,
    'place_3shapes_correctly': text_field,
    'place_4shapes_correctly': text_field,
    'place_5shapes_correctly': text_field,
    'place_6shapes_correctly': text_field,
    'animal_or_map_image': text_field,
    'boy_or_girl_image': text_field,
    'sound_device_by_order': text_field,
    'match_5items_with_pic': text_field,
    'find_smth_hidden': text_field,
    'hidden_food_under_cups': text_field,
    'identify_by_touching': text_field,
    'copy_straight_lines': text_field,
    'copy_circle': text_field,
    'copy_square': text_field,
    'copy_triangle': text_field,
    'copy_diamond': text_field,
    'copy_7letters': text_field,
    'draw_leg': text_field,
    'write_his_name': text_field,
    'cut_paper_by_scissor': text_field,
    'intrested_in_images_book': text_field,
    'silent_acting': text_field,
    'matches_9letters': text_field,
    'cubes_by_color': text_field,
    'shapes_by_color': text_field,
    'classify_cards': text_field,
    'reacts_to_imitated_movements': text_field,
    'reacts_to_imitated_sounds': text_field,
    'repeat_3sounds': text_field,
    'repeat_2numbers': text_field,
    'repeat_2words': text_field,
    'achieve_3tasks_order': text_field,

}




class level1Service(Service):
    def __init__(self, repository=level1Repository()):
        super().__init__(repository, fields=level1_fields)

class level2Service(Service):
    def __init__(self, repository=level2Repository()):
        super().__init__(repository, fields=level2_fields)