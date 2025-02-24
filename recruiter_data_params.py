from dataclasses import dataclass
from typing import Literal, Optional
from enum import Enum

EducationLevelLiteral = Literal['Среднее', 'Среднее специальное', 'Высшее',
'Незаконченное высшее', 'Магистр', 'Бакалавр']
BinaryChoiceLiteral = Literal['Да', 'Нет']
GenderLiteral = Literal['Мужской', 'Женский', 'Любой']


class Period(Enum):
    ALL_TIME = "За все время"
    DAY = "За сутки"
    THREE_DAYS = "За последние три дня"
    WEEK = "За неделю"
    MONTH = "За месяц"
    YEAR = "За год"


class MissingParameterError(Exception):
    pass


@dataclass
class RecruiterDataParams:
    applicant_limit: int  # Лимит на данную вакансию
    recruiter_name: str  # ФИО рекрутера (полностью)
    recruiter_email: str  # Почта рекрутера
    application_number: str  # Номер заявки в IQHR/ссылка на заявку
    job_position: str  # Вакансия по штатной книге

    period: Period  # Глубина просмотра резюме
    region: str  # Регион (территория поиска)

    job_title: str  # Название должности (ключевые слова или варианты поиска)
    job_responsibilities: str  # Основные обязанности (ключевые слова)

    education: EducationLevelLiteral  # Образование (минимальный уровень)

    job_search_status: str  # Статус поиска

    additional_education: str  # Дополнительное образование (Наличие сертификатов, лицензий)

    required_experience: str  # Необходимый опыт работы (отрасль, должности, уровень ответственности и др.)

    employment_type_full_time: BinaryChoiceLiteral  # Тип занятости: Полная занятость
    employment_type_part_time: BinaryChoiceLiteral  # Тип занятости: Частичная занятость
    employment_type_project: BinaryChoiceLiteral  # Тип занятости: Проектная работа/разовое задание
    employment_type_internship: BinaryChoiceLiteral  # Тип занятости: Стажировка
    work_schedule_full_day: BinaryChoiceLiteral  # График работы: Полный день
    work_schedule_shift: BinaryChoiceLiteral  # График работы: Сменный график
    work_schedule_flexible: BinaryChoiceLiteral  # График работы: Гибкий график
    work_schedule_remote: BinaryChoiceLiteral  # График работы: Удаленная работа
    work_schedule_rotational: BinaryChoiceLiteral  # График работы: Вахтовый метод

    salary: str  # Заработная плата

    age: str  # Возраст

    gender_preference: Optional[GenderLiteral]  # Пол (предпочтения руководителя)

    work_experience: str  # Стаж работы (с опытом/без опыта)

    software_knowledge: str  # Знание/владение ПО (ключевые требования к владению ПО)

    specialization: str | None  # Специализация (указать из справочника специализации, если не требуется - None)
    professional_roles: str | None  # Профессиональные роли (указать из справочника специализаци)
    show_resume_without_salary: BinaryChoiceLiteral  # Показывать резюме без указания зарплаты

    application_period: Period  # Глубина просмотра резюме на HH.ru в днях
    minimal_score: int  # Минимальная первичная оценка для дальнейшего рассмотрения

    exception_rules: int  # Правила исключения
    recruiter_requests: str  # Поле пожеланий от рекрутера для нейросети

    def __post_init__(self):
        # Проверка обязательных параметров
        if not self.recruiter_name:
            raise MissingParameterError("ФИО рекрутера обязательно.")
        if not self.recruiter_email:
            raise MissingParameterError("Почта рекрутера обязательна.")
        if not self.application_number:
            raise MissingParameterError("Номер заявки обязателен.")
        if not self.job_position:
            raise MissingParameterError("Вакансия обязательна.")
        if not self.region:
            raise MissingParameterError("Регион (территория поиска).")
        if not self.job_title:
            raise MissingParameterError("Название должности обязательно.")
        if not self.job_responsibilities:
            raise MissingParameterError("Основные обязанности обязательны.")
        if not self.education:
            raise MissingParameterError("Минимальный уровень образования обязателен")
        if not self.work_experience:
            raise MissingParameterError("Необходимый опыт работы обязателен.")
        if not self.salary:
            raise MissingParameterError("Заработная плата обязательна.")
        if not self.age:
            raise MissingParameterError("Возраст обязателен")

