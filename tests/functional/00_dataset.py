import database as db
from tests.data.cards_data import CARDS
from tests.data.coaches_data import COACHES
from tests.data.lesson_templates_data import LESSON_TEMPLATES
from tests.data.sold_cards import SOLD_CARDS
from tests.data.students_data import STUDENTS


def test_add_cards():
    db.init_db()
    for card in CARDS:
        db.create_card(card["name"], card["price"],card["lessons_count"],card["duration"],card["color"],card["status"])

    for coach in COACHES:
        db.add_coach(coach["first_name"],coach["last_name"],coach["middle_name"],coach["contacts"],coach["birthday"],coach["lessons_count"],coach["lessons_paid"],coach["student_payment"],coach["additional_info"])

    for student in STUDENTS:
        db.add_student(student["first_name"],student["last_name"],student["middle_name"],student["contacts"],student["birthday"],student["lessons_count"], student["additional_info"])

    for lesson_template in LESSON_TEMPLATES:
        db.add_lesson_template(lesson_template["template_name"], lesson_template["coach_id"], lesson_template["student_ids"].split(","))

    for sold_card in SOLD_CARDS:
        db.store_purchased_card(sold_card["date"], sold_card["card_id"], sold_card["student_id"])