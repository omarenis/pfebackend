from django.test import TestCase
from gestionpatient.models import Patient
from gestionpatient.service import PatientService, calculate_score, get_age
from gestionusers.models import PersonProfile


class CalculateScoreServiceTest(TestCase):

    def setUp(self) -> None:
        self.service = PatientService()

    def test_create_patient(self):
        data_form_parent = {
            'name': 'John',
            'parent': None,
            'birthdate': '2014-02-01',
            'gender': 'M',
            'sick': None,
            'behaviortroubleparent': {
                'insolent_with_grown_ups': "never",
                'feels_attacked_defensive': "never",
                'destructive': "never",
                'deny_mistakes_blame_others': "never",
                'quarrelsome_get_involved_fight': "never",
                'bully_intimidate_comrades': "never",
                'constantly_fight': "never",
                'unhappy': "never"
            },
            'learningtroubleparent': {
                'has_learning_difficulties': "never",
                'trouble_finishing_things': "never",
                'easily_being_distracted': "never",
                'enability_finish_when_do_effort': "never"
            },
            'somatisationtroubleparent': {
                'headaches': "never",
                'upset_stomach': "never",
                'physical_aches': "never",
                'vomiting_nausea': "never"
            },
            'hyperactivitytroubleparent': {
                'excitable_impulsive': "never",
                'want_dominate': "never",
                'squirms': "never",
                'restless_needs_do_something': "never"
            },
            'anxitytroubleparent': {
                'afraid_new_things': "never",
                'shy': "never",
                'worry_much': "never",
                'being_crashed_manipulated': "never"
            },
            'formabrparent': {
                'excitable_impulsive': "never",
                'cry_often_easily': "never",
                'squirms': "never",
                'restless_needs_do_something': "never",
                'destructive': "never",
                'trouble_finishing_things': "never",
                'easily_being_distracted': "never",
                'moody': "never",
                'enability_finish_when_do_effort': "never",
                'disturb_other_children': "never"
            }
        }
        data_form_teacher = {
            'name': 'John',
            'parent': None,
            'teacher': 3,
            'birthdate': '2014-02-01',
            'gender': 'M',
            'sick': None,

            'behaviortroubleteacher': {

                'arrogant_impolite': "never",
                'angry_unexpected_behavior': "never",
                'sensitive_criticism': "never",
                'pout_sulk_easily': "never",
                'moody': "never",
                'brawler': "never",
                'deny_mistakes_blame_others': "never",
                'few_relations_school': "never"
            },

            'hyperactivitytroubleteacher': {

                'restless_squirms_chair': "never",
                'inappropriate_noises': "never",
                'immediately_satisfied_needs': "never",
                'annoy_students': "never",
                'goes_left_right': "never",
                'easily_turn_on_impulsive': "never",
                'excessive_attention_from_teacher': "never"
            },
            'inattentiontroubleteacher': {

                'distracted': "never",
                'dreamer': "never",
                'led_by_others': "never",
                'trouble_guiding_others': "never",
                'trouble_finishing_things': "never",
                'immature': "never",
                'upset_easily_make_effort': "never",
                'has_learning_difficulties': "never"

            },
            'formabrteacher': {
                'restless_squirms_chair': "never",
                'angry_unexpected_behavior': "never",
                'distracted': "never",
                'annoy_students': "never",
                'pout_sulk_easily': "never",
                'moody': "never",
                'goes_left_right': "never",
                'easily_turn_on_impulsive': "never",
                'trouble_finishing_things': "never",
                'upset_easily_make_effort': "never"
            }

        }
        type_user = 'teacher'
        patient = self.service.create(data=data_form_teacher, type_user=type_user)
        # print('pppp',patient.formabrparent.score)
        self.assertIsInstance(patient, Patient)
