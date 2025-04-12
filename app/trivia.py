class Question:
    def __init__(self, description, options, correct_answer):
        self.description = description
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        return self.correct_answer == answer
    

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0
        

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None
    
    def answer_question(self,question,answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False
    

def run_quiz():
    """
    Funcion para ejecutar el quiz que imprima las preguntas en consola
    """
    q=Quiz() #Instanciar la clase quiz


    # Añadir preguntas al quiz

    preg1 = Question("¿Cuál es la capital de Peru?", ["Cali", "Bogota", "Lima", "Santiago"], "Lima")
    preg2 = Question("¿Cuál es la capital de Francia?", ["Londres", "Berlín", "Madrid", "París"], "París")
    preg3 = Question("¿Cuál es la capital de España?", ["Londres", "Berlín", "Madrid", "París"], "Madrid")
    preg4 = Question("¿Cuál es la capital de Alemania?", ["Londres", "Berlín", "Madrid", "París"], "Berlín")
    preg5 = Question("¿Cuál es la capital de Inglaterra?", ["Londres", "Berlín", "Madrid", "París"], "Londres")
    preg6 = Question("¿Cuál es la capital de Chile?", ["Londres", "Berlín", "Santiago", "París"], "Santiago")
    preg7 = Question("¿Cuál es la capital de Argentina?", ["Londres", "Buenos Aires", "Madrid", "París"], "Buenos Aires")
    preg8 = Question("¿Cuál es la capital de Colombia?", ["Cali", "Bogota", "Lima", "Santiago"], "Bogotá")
    preg9 = Question("¿Cuál es la capital de Ecuador?", ["Cali", "Bogota", "Lima", "Quito"], "Quito")
    preg10 = Question("¿Cuál es la capital de Venezuela?", ["Caracas", "Bogota", "Lima", "Santiago"], "Caracas")


    q.add_question(preg1)
    q.add_question(preg2)
    q.add_question(preg3)
    q.add_question(preg4)
    q.add_question(preg5)
    q.add_question(preg6)
    q.add_question(preg7)
    q.add_question(preg8)
    q.add_question(preg9)
    q.add_question(preg10)

    # Recorrer a travez de las preguntas del quiz

    while True:
        question= q.get_next_question()
        if question is None:
            print("Quiz terminado")
            break
        
        print(question.description)
        for i, option in enumerate(question.options,1):
            print(f"{i}. {option}")


        rpt= input("Escribe tu respuesta: ")

        if question.is_correct(rpt):
            print("Respuesta correcta")
        else:
            print("Respuesta incorrecta")


