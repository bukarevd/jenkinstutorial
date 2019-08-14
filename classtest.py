class Answer():
    def __init__(self, answers):
        self.answers = answers
        self.listofanswer = []

    def save_answer(self, answer_param=''):
        self.listofanswer.append(answer_param)

    def print_answers(self):
        for answer1 in self.listofanswer:
            print(answer1)


test =Answer('test')
test.save_answer()
test.print_answers()

