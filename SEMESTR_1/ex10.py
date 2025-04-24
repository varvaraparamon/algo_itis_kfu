"""
11. Написать программу, управления стройкой
Задачи:

    • Структуры, описывающие Этап: класс  (Stage), содержащий стоимость, сроки начала и завершения как строка (в формате дд.мм.гггг, при неверном формате бросать исключение), описание этапа строкой, текущий статус (выполнен, осуществляется, запланирован, забракован), методы  next(), prev(), start(), stop(), метод забраковать()
    • потомки: проект, фундамент, стены, крыша, отделка
Класс Стройка, описывающий начало строительства и его завершение, содержит этапы в виде двунаправленного связного списка, метод run(), запускающий стройку, и возвращающий результат стройки (успешно или нет).
    • Генерация и обработка исключения (возврат к предыдущему этапу), если этап забракован (переделка начинается с предыдущего, если забракован проект, то стройка отменяется)
Создать программу осуществляющую стройку, каждый этап бракуется с вероятностью 10%
Запустить стройку 1000 раз, статистически оценить вероятность успешного завершения.
    • Написать тестовый класс, демонстрирующий выброс исключения при указании неверных дат (проверять только формат).
	
"""
import random
from datetime import datetime

class Status():
    PLANNED = "запланирован"
    IN_PROGRESS = "осуществляется"
    COMPLETED = "выполнен"
    REJECTED = "забракован"

class Stage:
    def __init__(self, cost, start_date, end_date, description):
        self.validate_date(start_date)
        self.validate_date(end_date)
        
        self.cost = cost
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.status = Status.PLANNED
        self.next_stage = None
        self.prev_stage = None
    
    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%d.%m.%Y")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {date_str}, нужно дд.мм.гггг")
    
    def start(self):
        self.status = Status.IN_PROGRESS
    
    def stop(self):
        self.status = Status.COMPLETED
    
    def reject(self):
        self.status = Status.REJECTED
    
    def next(self):
        return self.next_stage
    
    def prev(self):
        return self.prev_stage

class Project(Stage):
    def __init__(self):
        super().__init__(50000, "01.01.2023", "15.01.2023", "Создание проекта")

class Foundation(Stage):
    def __init__(self):
        super().__init__(200000, "16.01.2023", "15.02.2023", "Заливка фундамента")

class Walls(Stage):
    def __init__(self):
        super().__init__(300000, "16.02.2023", "15.04.2023", "Возведение стен")

class Roof(Stage):
    def __init__(self):
        super().__init__(150000, "16.04.2023", "15.05.2023", "Монтаж крыши")

class Finishing(Stage):
    def __init__(self):
        super().__init__(100000, "16.05.2023", "15.07.2023", "Отделочные работы")

class Construction:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_stage = None
        self._setup_stages()
    
    def _setup_stages(self):
        stages = [Project(), Foundation(), Walls(), Roof(), Finishing()]
        
        for stage in stages:
            self.add_stage(stage)
        
        self.current_stage = self.head
    
    def add_stage(self, stage):
        if not self.head:
            self.head = stage
            self.tail = stage
        else:
            stage.prev_stage = self.tail
            self.tail.next_stage = stage
            self.tail = stage
    
    def run(self):
        while self.current_stage:
            self.current_stage.start()
            
            if random.random() < 0.1:
                self.current_stage.reject()
                return self._handle_rejection()
            
            self.current_stage.stop()
            self.current_stage = self.current_stage.next()
        
        return True
    
    def _handle_rejection(self):
        if isinstance(self.current_stage, Project):
            return False
        
        prev_stage = self.current_stage.prev()
        if prev_stage:
            prev_stage.status = Status.PLANNED
            self.current_stage = prev_stage
        return False

class TestStage:
    def test_date_validation():
        try:
            Stage(1000, "32.01.2023", "15.02.2023", "Тест")
            print("TEST FAILED: неправильная дата прошла валидацию")
        except ValueError:
            print("TEST PASSED: неправильная дата обнаружена")
        
        try:
            Stage(1000, "01.01.2023", "15.02.2023", "Тест")
            print("TEST PASSED: правильные даты приняты")
        except ValueError:
            print("TEST FAILED: правильные даты не прошли валидацию")


def run_statistics():
    successes = 0
    for _ in range(1000):
        construction = Construction()
        if construction.run():
            successes += 1
    
    probability = successes / 1000
    print(f"Вероятность успешного завершения строительства: {probability:.2%}")


if __name__ == "__main__":
    TestStage.test_date_validation()
    run_statistics()
    
    construction = Construction()
    result = construction.run()
    print(result)