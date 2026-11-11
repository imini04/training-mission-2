class QuizGame:
    """퀴즈 게임 관리 클래스"""

    def __init__(self):
        self.quizzes = []
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
        print("none")

    def add_quiz(self):
        print("none")

    def list_quizzes(self):
        print("none")

    def show_score(self):
        print("none")