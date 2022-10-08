# 엑셀은 Microsoft사가 개발한 프로그램입니다. 새 엑셀 파일을 만들면, 직사각형 셀(cell)이 2차원 평면을 가득 채우고 있습니다.
# 엑셀의 모든 셀은 자신이 위치한 행, 열에 따른 고유한 이름을 가지고 있습니다. 셀의 이름이 주어지면 그 왼쪽에 있는 셀과 윗쪽에 있는 셀의 이름을 순서대로 출력해주세요. 
# 다음은 셀의 이름에 대한 자세한 설명입니다.
# 행의 이름은 1 이상의 10진법 정수입니다. 맨 위 행의 이름은 1이고, 어떤 행의 이름이 x라면 그 아래쪽 행의 이름은 x+1입니다.
# 열의 이름은 길이 1 이상의 A부터 Z까지의 영어 알파벳으로 이루어진 문자열입니다. 문자열이 사전순으로 앞설수록 더 왼쪽의 열을 나타냅니다.
# 두 문자열을 비교했을 때, 길이가 다르다면 더 짧은 쪽이, 같다면 제일 왼쪽의 문자부터 비교하여 알파벳 순으로 앞서는 문자가 먼저 나오는 쪽이 사전순으로 앞섭니다.
# 따라서 맨 왼쪽 열은 A이고, 다음 25열은 B, C, …, Z 이고, 다음 26 * 26 열은 AA, AB, AC, …, ZY, ZZ 이고, 다음 26 * 26 * 26 열은 AAA, AAB, AAC, …, ZZY, ZZZ 입니다.
# 마지막으로 (row)행 (column)열에 위치한 셀의 이름은 (column)(row)입니다.

# 예제 입력1
# AA9
# 예제 출력1
# Z9
# AA8

# 예제 입력2
# NIA97
# 예제 출력2
# NHZ97
# NIA96

# 입력값 설명
# 선택된 셀의 이름이 주어집니다.
# 1 < 행의 이름 ≤ 999
# A < 열의 이름 ≤ ZZZ

# 출력값 설명
# 첫 번째 줄에 왼쪽에 있는 셀의 이름을 출력합니다.
# 두 번째 줄에 위쪽에 있는 셀의 이름을 출력합니다.

import sys

cell = sys.stdin.readline().strip()

for i in range(len(cell)):
    if ord(cell[i]) < 65 or 90 < ord(cell[i]):
        column = list(cell[: i])
        column2 = cell[: i]
        row = cell[i :]

        if column.count('A') == len(column):
            column = 'Z' * (len(column) - 1)

        elif column[-1] == 'A':
            for j in range(-1, len(column) * -1 - 1, -1):
                column[j] = 'Z'

                if column[j - 1] != 'A':
                    column[j - 1] = chr(ord(column[j - 1]) - 1)
                    break

        else:
            print(column[-1])
            print(chr(ord(column[-1]) - 1))
            column[-1] = chr(ord(column[-1]) - 1)
            
        print(*column, int(row), sep = '')
        print(column2, int(row) - 1, sep = '')

        break