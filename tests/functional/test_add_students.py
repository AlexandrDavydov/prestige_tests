from pages.add_student_page import AddStudentPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.students_page import StudentsPage


def test_add_students(driver):
    students = [
        {
            "last_name": "Давыдова",
            "first_name": "Ольга",
            "middle_name": "Александровна",
            "contacts": "+79398518023",
            "birthday": "29.10.2010",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Драгунова",
            "first_name": "Ксения",
            "middle_name": "Георгиевна",
            "contacts": "123456789",
            "birthday": "05.04.2010",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Шершукова",
            "first_name": "Ольга",
            "middle_name": "Ильинична",
            "contacts": "987654321",
            "birthday": "12.06.2011",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Родионова",
            "first_name": "Татьяна",
            "middle_name": "Игоревна",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Лисицына",
            "first_name": "Евдокия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Паолилло",
            "first_name": "Асия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Хохлова",
            "first_name": "Дарья",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Смирнова ",
            "first_name": "Алена",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Федорова",
            "first_name": "Полина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Дадашева",
            "first_name": "Ксения",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Кестер",
            "first_name": "Аврора",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Шевхужева",
            "first_name": "Элина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Приходько",
            "first_name": "Лидия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Шевхужева",
            "first_name": "Лия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Острожникова",
            "first_name": "Марго",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Каюкова",
            "first_name": "Дарина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Александрова",
            "first_name": "Оливия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Кириллова",
            "first_name": "Луша",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Даленко",
            "first_name": "Ульяна",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Даленко",
            "first_name": "Саша",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Тимохина",
            "first_name": "Анна",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Стыш",
            "first_name": "Эмилия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Терещенко",
            "first_name": "Марьяна",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Носова",
            "first_name": "Велена",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Зудкина",
            "first_name": "София",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Шибецкая",
            "first_name": "Вероника",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Хлебникова",
            "first_name": "Саша",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Новикова",
            "first_name": "Арина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Армаганова",
            "first_name": "Дина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Гумирова",
            "first_name": "Виктория",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Г",
            "first_name": "Варя",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Лепехина",
            "first_name": "София",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Ревякина",
            "first_name": "Арина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Птицына",
            "first_name": "София",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Завгородняя",
            "first_name": "Анна",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Перова",
            "first_name": "Анастасия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Макарова",
            "first_name": "Виктория",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Шипунова",
            "first_name": "Алевтина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Карпановская",
            "first_name": "Елена",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Черноморова",
            "first_name": "Саша",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Топольская",
            "first_name": "Майя",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Мутина",
            "first_name": "Ярослава",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Озерина",
            "first_name": "Арина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Павлова",
            "first_name": "Ольга",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Журавлева",
            "first_name": "Ксения",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Кулагина",
            "first_name": "Злата",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Бочкарева",
            "first_name": "Виктория",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Брюшинина",
            "first_name": "Елена",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Минеева",
            "first_name": "Татьяна",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Кузнецова",
            "first_name": "Кира",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Квасова",
            "first_name": "Кристина",
            "middle_name": "Васильевна",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Еремина",
            "first_name": "Кира",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Тихонова",
            "first_name": "Катерина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Калачева",
            "first_name": "Есения",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Лебедева",
            "first_name": "Людмила",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Коваленко",
            "first_name": "Ника",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Коростелева",
            "first_name": "Анна",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Комарова",
            "first_name": "Майя",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Петрова",
            "first_name": "Варвара",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Аракелян",
            "first_name": "Екатерина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Воробьева",
            "first_name": "Анна",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Клепикова",
            "first_name": "София",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Пядык",
            "first_name": "Святослава",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Алешина",
            "first_name": "Софья",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Мартишина",
            "first_name": "Настя",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Капустина",
            "first_name": "Настя",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Шайкин",
            "first_name": "Григорий",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Маскаева",
            "first_name": "София",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Жесткова",
            "first_name": "Варвара",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Агафонычева",
            "first_name": "Мира",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Пичугина",
            "first_name": "Мария",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Пелагеина",
            "first_name": "Василиса",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Бодрякова",
            "first_name": "Саша",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Санникова",
            "first_name": "Полина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Руделева",
            "first_name": "Тася",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Гумирова",
            "first_name": "Арника",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Эрисова",
            "first_name": "Елена",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Третьяк",
            "first_name": "Ольга",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Орданова",
            "first_name": "Валерия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Корнеева",
            "first_name": "Анастасия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Ляховка",
            "first_name": "Ирина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Даленко",
            "first_name": "Ирина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Козлитина",
            "first_name": "Лиза",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Капустина",
            "first_name": "Лиза",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Любанова",
            "first_name": "Мария",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Войнова",
            "first_name": "Алина",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Венина",
            "first_name": "Мария",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Ляховка",
            "first_name": "Вероника",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Литвина",
            "first_name": "Ульяна",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Климова",
            "first_name": "Саша",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Рязапова",
            "first_name": "Варвара",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        },
        {
            "last_name": "Дрозд",
            "first_name": "Мия",
            "middle_name": "",
            "contacts": "",
            "birthday": "",
            "lessons_count": 0,
            "additional_info": ""
        }
    ]

    page = LoginPage(driver)
    page.open()
    page.login(page.getUsername(), page.getPassword())

    page = MainPage(driver)
    page.go_to_students()

    for student in students:
        page = StudentsPage(driver)
        page.go_to_add_student()
        page=AddStudentPage(driver)
        page.fill_form(student["last_name"], student["first_name"], student["middle_name"], student["contacts"],
            student["birthday"], student["lessons_count"], student["additional_info"])
        page.save()

    page = StudentsPage(driver)
    for student in students:
        assert page.is_data_present_flexible(student)

    page.has_number_of_rows(len(students))


