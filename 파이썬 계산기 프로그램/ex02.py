def calculator():
    print("=== 간단한 계산기 ===")
    print("1: 덧셈")
    print("2: 뺄셈")
    print("3: 곱셈")
    print("4: 나눗셈")
    print("0: 종료")
    
    while True:
        choice = input("원하는 연산을 선택하세요 (0-4): ")
        if choice == "0":
            print("계산기를 종료합니다.")
            break
        elif choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("첫 번째 숫자: "))
                num2 = float(input("두 번째 숫자: "))
                if choice == "1":
                    print(f"결과: {num1} + {num2} = {num1 + num2}")
                elif choice == "2":
                    print(f"결과: {num1} - {num2} = {num1 - num2}")
                elif choice == "3":
                    print(f"결과: {num1} * {num2} = {num1 * num2}")
                elif choice == "4":
                    if num2 == 0:
                        print("오류: 0으로 나눌 수 없습니다.")
                    else:
                        print(f"결과: {num1} / {num2} = {num1 / num2}")
            except ValueError:
                print("오류: 숫자를 입력하세요.")
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
            
# 프로그램 실행
calculator()
