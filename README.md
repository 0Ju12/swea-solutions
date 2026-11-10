# swea-solutions — SW Expert Academy 풀이 모음

SSAFY 과정에서 SWEA 문제를 풀며 쓴 Python 풀이를 주제별로 정리했습니다.
**내가 쓴 코드와 풀이 설명만** 올리고, 문제 원문·공식 입출력 예제는 넣지 않았습니다 (문제는 번호로 SWEA에서 찾을 수 있습니다).

```bash
python -m pytest -q      # 37 passed — 직접 만든 작은 입력으로 각 풀이를 실행해 출력 비교
```

테스트 입력은 손으로 답을 셀 수 있게 새로 만든 것이라, 채점 서버의 시간 제한·큰 입력까지 보장하지는 않습니다.

## 폴더

| 폴더 | 주제 |
|---|---|
| [implementation](implementation/) | 구현·시뮬레이션 (격자 탐색, 델타 이동, 완전탐색) |
| [graph](graph/) | DFS, 위상 정렬, MST(Prim) |
| [backtracking-dp-greedy](backtracking-dp-greedy/) | 백트래킹·가지치기, 비트마스크 메모이제이션, DP, 그리디 |
| [string-stack](string-stack/) | 회문, 괄호 스택, 투 포인터 |

## 문제별 풀이

| 번호 | 문제 | 풀이 핵심 | 파일 |
|---|---|---|---|
| 1208 | Flatten | 덤프마다 정렬 후 최고−1·최저+1 | [implementation/1208_flatten.py](implementation/1208_flatten.py) |
| 1215 | 회문1 | 가로는 슬라이싱, 세로는 열을 모아 뒤집어 비교 | [string-stack/1215_palindrome1.py](string-stack/1215_palindrome1.py) |
| 1218 | 괄호 짝짓기 | 여는 괄호 push, 닫는 괄호는 짝 사전으로 top 비교 | [string-stack/1218_bracket_pairs.py](string-stack/1218_bracket_pairs.py) |
| 1219 | 길찾기 | 인접 리스트 + DFS로 0 → 99 도달 여부 | [graph/1219_find_road.py](graph/1219_find_road.py) |
| 1222 | 계산기1 | 한 자리 수 덧셈식이라 숫자만 더함 | [string-stack/1222_calculator1.py](string-stack/1222_calculator1.py) |
| 1251 | 하나로 | 완전 그래프 MST — Prim + heapq, 거리² × E | [graph/1251_hanaro_prim.py](graph/1251_hanaro_prim.py) |
| 1267 | 작업순서 | 진입 차수 0부터 큐로 위상 정렬 (2가지 작성) | [a](graph/1267_task_order_a.py) · [b](graph/1267_task_order_b.py) |
| 1860 | 진기의 최고급 붕어빵 | 도착 시각 정렬 후 i번째 손님 시각까지 만든 개수 ≥ i+1 | [implementation/1860_bungeoppang.py](implementation/1860_bungeoppang.py) |
| 1926 | 간단한 369게임 | 자릿수에서 3·6·9 개수만큼 '-' | [implementation/1926_simple_369.py](implementation/1926_simple_369.py) |
| 1952 | 수영장 | dp[i] = min(일권, 월권, 3개월권 + dp[i−3]), 마지막에 1년권과 비교 | [backtracking-dp-greedy/1952_swimming_pool_dp.py](backtracking-dp-greedy/1952_swimming_pool_dp.py) |
| 1959 | 두 개의 숫자열 | 짧은 쪽을 밀며 곱의 합 최댓값 | [implementation/1959_two_sequences.py](implementation/1959_two_sequences.py) |
| 1961 | 숫자 배열 회전 | 90·180·270도 좌표 변환 | [implementation/1961_rotate_array.py](implementation/1961_rotate_array.py) |
| 1974 | 스도쿠 검증 | 행·열·3×3을 set 크기 9로 검사 | [implementation/1974_sudoku_check.py](implementation/1974_sudoku_check.py) |
| 1979 | 어디에 단어가 들어갈 수 있을까 | 가로·세로 연속 1의 길이가 정확히 K인 구간 수 | [implementation/1979_word_fit.py](implementation/1979_word_fit.py) |
| 2001 | 파리 퇴치 | M×M 창 합 완전탐색 | [implementation/2001_fly_swatter.py](implementation/2001_fly_swatter.py) |
| 2805 | 농작물 수확하기 | 중심과의 맨해튼 거리 ≤ N//2 | [implementation/2805_farm_harvest.py](implementation/2805_farm_harvest.py) |
| 2806 | N-Queen | 열 집합 + 이전 행과 대각 검사(for-else) 백트래킹 | [backtracking-dp-greedy/2806_n_queen.py](backtracking-dp-greedy/2806_n_queen.py) |
| 3234 | 준환이의 양팔저울 | ① 왼쪽이 절반 이상이면 남은 경우를 2^k·k!로 한 번에 더하는 가지치기 ② (사용한 추, 왼쪽 무게) 비트마스크 메모 | [a](backtracking-dp-greedy/3234_balance_a_backtracking.py) · [b](backtracking-dp-greedy/3234_balance_b_bitmask_memo.py) |
| 3499 | 퍼펙트 셔플 | 앞 절반(홀수면 하나 더)과 뒤 절반을 번갈아 | [implementation/3499_perfect_shuffle.py](implementation/3499_perfect_shuffle.py) |
| 4613 | 러시아 국기 같은 깃발 | 경계 두 줄 완전탐색, 칠할 칸 수 최소 | [implementation/4613_russian_flag.py](implementation/4613_russian_flag.py) |
| 8702 | 당근 수확 | 나누는 위치마다 양쪽 합의 차 최소 | [implementation/8702_carrot_harvest.py](implementation/8702_carrot_harvest.py) |
| 10761 | 신뢰 | 두 로봇이 다른 로봇 차례에 미리 움직인 시간을 빼고 누적 | [implementation/10761_bot_trust.py](implementation/10761_bot_trust.py) |
| 12712 | 파리퇴치3 | + / × 모양 델타 배열로 M−1칸까지 합 | [implementation/12712_fly_swatter3.py](implementation/12712_fly_swatter3.py) |
| 14510 | 나무 높이 | 부족분을 2와 1의 개수로 나누고 균형을 맞춰 날짜 계산 | [backtracking-dp-greedy/14510_tree_height.py](backtracking-dp-greedy/14510_tree_height.py) |
| 18575 | 풍선팡 보너스 게임 | 칸마다 행+열−자기, 최댓값−최솟값 | [implementation/18575_balloon_bonus.py](implementation/18575_balloon_bonus.py) |
| 21936 | 길이가 M인 회문 | 길이 M 창을 밀며 뒤집어 비교 | [string-stack/21936_palindrome_m.py](string-stack/21936_palindrome_m.py) |
| 22375 | 스위치 | 앞에서부터 다르면 그 뒤를 모두 뒤집는 그리디 | [backtracking-dp-greedy/22375_switch_greedy.py](backtracking-dp-greedy/22375_switch_greedy.py) |
| 23795 | 우주 괴물 | 괴물 위치에서 4방향으로 벽(1)까지 표시, 남은 0 개수 | [implementation/23795_space_monster.py](implementation/23795_space_monster.py) |
| 25052 | 등산로 | 칸마다 가장 낮은 이웃으로만 내려가며 길이 측정 | [implementation/25052_hiking_trail.py](implementation/25052_hiking_trail.py) |
| 25985 | 숫자열의 최대 곱 | 겹치는 모든 위치(음수 이동 포함)에서 곱의 합 | [implementation/25985_max_product.py](implementation/25985_max_product.py) |
| 26045 | 부분 수열 판별 | B 포인터 하나로 A를 한 번 훑기 (투 포인터) | [string-stack/26045_subsequence_two_pointer.py](string-stack/26045_subsequence_two_pointer.py) |
| 26059 | 과일 등급 분류 | 정렬 후 경계 두 개, 같은 무게 사이는 경계 불가 | [implementation/26059_fruit_grading.py](implementation/26059_fruit_grading.py) |
| 29638 | 내리막 | 인접 쌍이 모두 감소인지 | [implementation/29638_downhill.py](implementation/29638_downhill.py) |
| — | 섬 찾기 | 'L'을 만나면 개수 +1 후 DFS로 섬 전체를 지움 | [graph/island_count_dfs.py](graph/island_count_dfs.py) |

## 테스트를 붙이며 고친 것

드라이브에 있던 원본은 첫 커밋에 그대로 있고, 테스트에서 실패한 6개만 다음 커밋에서 최소한으로 고쳤습니다.

| 문제 | 테스트에서 난 오류 | 고친 내용 |
|---|---|---|
| 1219 길찾기 | 10번째 뒤에 `EOFError` | `range(1, T+10)` → `range(1, T+1)` |
| 1952 수영장 | `IndexError` | dp 길이 13, `plan[i-1]`, 3개월권을 1·2월에도 허용(`dp[max(0, i-3)]`) |
| 1974 스도쿠 | `NameError: sqd` | 변수 이름 오타 `sqd` → `sdq` |
| 2806 N-Queen | `int(input)` 에서 `TypeError` | `int(input())`, 대각 검사를 for-else 로 (원래는 첫 행에서 재귀가 일어나지 않음) |
| 3234 양팔저울 ② | `UnboundLocalError` | `global visited`, 왼쪽에 올리는 경우의 반환값도 더함 |
| 18575 풍선팡 | 최댓값·최솟값 초깃값이 바뀌어 항상 9999 | 초깃값을 −∞ / +∞ 로 |
