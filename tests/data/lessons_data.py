import random
from datetime import datetime, timedelta

today = datetime.now().date()

def generate_students_numbers(student_count: int, max_number: int) -> list[str]:
    numbers = [str(random.randint(1, max_number)) for _ in range(student_count)]
    return numbers

LESSONS_DATA = [
    {
        "lesson_name": "Урок № "+str(random.randint(0, 100)),
        "date": today,
        "coach_id": random.randint(1, 2),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось",
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": today,
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=1)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=1)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=2)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=2)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=3)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=3)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=4)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=4)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=5)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=5)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=6)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=6)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=7)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=7)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=8)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=8)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=9)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=9)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=10)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=10)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=11)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=11)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=12)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=12)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=13)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=13)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=14)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=14)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=15)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=15)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=16)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=16)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=17)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=17)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=18)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=18)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=19)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=19)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=20)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=20)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=21)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=21)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=22)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=22)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=23)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=23)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=24)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=24)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=25)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=25)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=26)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=26)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=27)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=27)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=28)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=28)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=29)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=29)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=30)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=30)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=31)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=31)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=32)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=32)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=33)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=33)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=34)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=34)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=35)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    },
    {
        "lesson_name": "Урок № " + str(random.randint(0, 100)),
        "date": (today - timedelta(days=35)).strftime("%Y-%m-%d"),
        "coach_id": random.randint(1, 3),
        "student_ids": generate_students_numbers(11, 90),
        "status": "Состоялось"
    }
   ]


