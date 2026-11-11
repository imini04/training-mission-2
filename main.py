from game import QuizGame


def main():
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        game.save_state()
        print("\n\n입력이 중단되어 저장 후 프로그램이 종료됩니다.")


if __name__ == "__main__":
    main()