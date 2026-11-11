from quiz import Quiz
from data import get_default_quizzes

class QuizGame:
    """퀴즈 게임 관리 클래스"""

    def __init__(self):
        self.quizzes = get_default_quizzes()
        self.best_score = None

    def show_menu(self):
        print("=" * 40)
        print("       크리스마스 퀴즈 게임")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def get_number(self, prompt, min_value, max_value):
        """min_value~max_value 사이 정수를 받을 때까지 반복해서 입력받는다."""
        while True:
            raw = input(prompt).strip()
            if raw == "":
                print("입력이 비어 있습니다. 숫자를 입력하세요.")
                continue
            try:
                number = int(raw)
            except ValueError:
                print(f"잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue
            if not min_value <= number <= max_value:
                print(f"잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue
            return number

    def get_text(self, prompt):
        """비어 있지 않은 문자열을 받을 때까지 반복해서 입력받는다."""
        while True:
            text = input(prompt).strip()
            if text == "":
                print("입력이 비어 있습니다. 내용을 입력하세요.")
                continue
            return text

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_number("선택: ", 1, 5)
            print()
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            else:
                print("게임을 종료합니다.")
                break
            print()

    def play_quiz(self):
        """저장된 퀴즈를 순서대로 출제하고 결과를 보여준다."""
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return

        total = len(self.quizzes)
        correct_count = 0
        print(f"퀴즈를 시작합니다! (총 {total}문제)")
        print()

        for number, quiz in enumerate(self.quizzes, start=1):
            print("-" * 40)
            quiz.display(number)
            user_answer = self.get_number("정답 입력: ", 1, 4)

            if quiz.is_correct(user_answer):
                print("정답입니다!")
                correct_count += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")
            print()

        score = correct_count * 100 // total
        print("=" * 40)
        print(f"결과: {total}문제 중 {correct_count}문제 정답! ({score}점)")
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")
        print("=" * 40)

    def add_quiz(self):
        """문제, 선택지 4개, 정답 번호를 입력받아 새 퀴즈를 추가한다."""
        print("새로운 퀴즈를 추가합니다.")
        print()

        question = self.get_text("문제를 입력하세요: ")
        choices = []
        for i in range(1, 5):
            choices.append(self.get_text(f"선택지 {i}: "))
        answer = self.get_number("정답 번호 (1-4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))
        print()
        print("퀴즈가 추가되었습니다!")

    def list_quizzes(self):
        """등록된 퀴즈의 문제를 번호와 함께 보여준다."""
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print()
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("-" * 40)

    def show_score(self):
        """최고 점수를 보여준다."""
        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았습니다. 먼저 퀴즈를 풀어 보세요!")
            return

        print(f"최고 점수: {self.best_score}점")