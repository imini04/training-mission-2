class Quiz:
    """문제 하나(문제, 선택지 4개, 정답 번호)를 표현하는 클래스"""

    def __init__(self, question, choices, answer):
        self.question = question  # 문제 (str)
        self.choices = choices    # 선택지 4개 (list[str])
        self.answer = answer      # 정답 번호 1~4 (int)

    def display(self, number):
        """문제 번호, 문제, 선택지를 출력한다."""
        print(f"[문제 {number}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")
        print()

    def is_correct(self, user_answer):
        """사용자의 답안이 정답이면 True를 반환한다."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON으로 저장할 수 있도록 딕셔너리로 바꾼다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """딕셔너리에서 Quiz 객체를 만든다. 형식이 잘못되면 ValueError를 낸다."""
        question = data["question"]
        choices = data["choices"]
        answer = data["answer"]

        if not isinstance(question, str) or question.strip() == "":
            raise ValueError("문제 형식이 올바르지 않습니다.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 4개여야 합니다.")
        if not isinstance(answer, int) or not 1 <= answer <= 4:
            raise ValueError("정답 번호는 1~4 사이여야 합니다.")

        return cls(question, choices, answer)