"""직접 만든 작은 입력으로 각 풀이를 실행해 출력을 비교합니다.

입력은 문제 원문·공식 예제가 아니라, 손으로 답을 셀 수 있게 새로 만든 것입니다.
"""
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def rep(block: str, n: int = 10) -> str:
    """테스트 케이스 수가 10으로 고정된 문제용 (T 를 읽지 않음)"""
    return block * n


def run(path: str, stdin: str) -> list[str]:
    p = subprocess.run([sys.executable, str(ROOT / path)], input=stdin, capture_output=True, text=True, timeout=10)
    assert p.returncode == 0, p.stderr[-400:]
    return [" ".join(line.split()) for line in p.stdout.strip().splitlines()]


CASES = [
    ("implementation/1208_flatten.py", rep("1\n3 2 1\n"), [f"#{i} 0" for i in range(1, 11)]),
    ("implementation/1860_bungeoppang.py", "2\n2 2 2\n3 4\n2 2 1\n1 2\n", ["#1 Possible", "#2 Impossible"]),
    ("implementation/1926_simple_369.py", "13\n", ["1 2 - 4 5 - 7 8 - 10 11 12 -"]),
    ("implementation/1959_two_sequences.py", "1\n2 3\n1 2\n1 2 3\n", ["#1 8"]),
    ("implementation/1961_rotate_array.py", "1\n2\n1 2\n3 4\n", ["#1", "31 43 24", "42 21 13"]),
    ("implementation/1974_sudoku_check.py",
     "1\n" + "".join(" ".join(str((r * 3 + r // 3 + c) % 9 + 1) for c in range(9)) + "\n" for r in range(9)), ["#1 1"]),
    ("implementation/1979_word_fit.py", "1\n3 2\n1 1 0\n0 0 0\n1 1 0\n", ["#1 2"]),
    ("implementation/2001_fly_swatter.py", "1\n3 2\n1 2 3\n4 5 6\n7 8 9\n", ["#1 28"]),
    ("implementation/2805_farm_harvest.py", "1\n3\n123\n456\n789\n", ["#1 25"]),
    ("implementation/3499_perfect_shuffle.py", "1\n5\nA B C D E\n", ["#1 A D B E C"]),
    ("implementation/4613_russian_flag.py", "1\n3 2\nWB\nBB\nRR\n", ["#1 1"]),
    ("implementation/8702_carrot_harvest.py", "1\n3\n1 2 3\n", ["#1 2 0"]),
    ("implementation/10761_bot_trust.py", "3\n4 O 2 B 1 B 2 O 4\n3 O 5 O 8 B 100\n2 B 2 B 1\n", ["#1 6", "#2 100", "#3 4"]),
    ("implementation/12712_fly_swatter3.py", "1\n3 2\n1 2 3\n4 5 6\n7 8 9\n", ["#1 29"]),
    ("implementation/18575_balloon_bonus.py", "1\n2\n1 2\n3 4\n", ["#1 3"]),
    ("implementation/23795_space_monster.py", "1\n3\n0 0 0\n0 2 0\n0 0 0\n", ["#1 4"]),
    ("implementation/25052_hiking_trail.py", "1\n2\n1 2\n3 4\n", ["#1 3"]),
    ("implementation/25985_max_product.py", "1\n1 2\n2\n3 -1\n", ["#1 6"]),
    ("implementation/26059_fruit_grading.py", "2\n6 2 2\n1 2 3 4 5 6\n3 2 2\n1 1 1\n", ["#1 0", "#2 -1"]),
    ("implementation/29638_downhill.py", "2\n3\n3 2 1\n3\n3 3 1\n", ["#1 1", "#2 0"]),
    ("graph/1219_find_road.py", rep("1 2\n0 1 1 99\n"), [f"#{i} 1" for i in range(1, 11)]),
    ("graph/1251_hanaro_prim.py", "1\n2\n0 3\n0 4\n1\n", ["#1 25"]),
    ("graph/1267_task_order_a.py", rep("3 2\n1 2 2 3\n"), [f"#{i} 1 2 3" for i in range(1, 11)]),
    ("graph/1267_task_order_b.py", rep("3 2\n1 2 2 3\n"), [f"#{i} 1 2 3" for i in range(1, 11)]),
    ("graph/island_count_dfs.py", "1\n3 3\nLLW\nWWW\nWLL\n", ["#1 2"]),
    ("backtracking-dp-greedy/1952_swimming_pool_dp.py", "1\n10 40 100 300\n1 0 0 0 0 0 0 0 0 0 0 0\n", ["#1 10"]),
    ("backtracking-dp-greedy/1952_swimming_pool_dp.py", "2\n10 40 30 300\n1 1 1 0 0 0 0 0 0 0 0 0\n10 40 100 50\n5 5 5 5 5 5 5 5 5 5 5 5\n", ["#1 30", "#2 50"]),
    ("backtracking-dp-greedy/2806_n_queen.py", "2\n4\n1\n", ["#1 2", "#2 1"]),
    ("backtracking-dp-greedy/3234_balance_a_backtracking.py", "2\n1\n5\n2\n1 1\n", ["#1 1", "#2 4"]),
    ("backtracking-dp-greedy/3234_balance_b_bitmask_memo.py", "2\n1\n5\n2\n1 1\n", ["#1 1", "#2 4"]),
    ("backtracking-dp-greedy/14510_tree_height.py", "3\n2\n1 2\n2\n1 3\n3\n1 1 1\n", ["#1 1", "#2 2", "#3 0"]),
    ("backtracking-dp-greedy/22375_switch_greedy.py", "2\n3\n0 0 0\n1 1 1\n3\n0 0 0\n1 0 1\n", ["#1 1", "#2 3"]),
    ("string-stack/1215_palindrome1.py", rep("8\n" + "AAAAAAAA\n" * 8), [f"#{i} 16" for i in range(1, 11)]),
    ("string-stack/1218_bracket_pairs.py", rep("4\n([])\n", 5) + rep("2\n(]\n", 5), [f"#{i} 1" for i in range(1, 6)] + [f"#{i} 0" for i in range(6, 11)]),
    ("string-stack/1222_calculator1.py", rep("3\n1+2\n"), [f"#{i} 3" for i in range(1, 11)]),
    ("string-stack/21936_palindrome_m.py", "1\n5 3\nabcba\n", ["#1 bcb"]),
    ("string-stack/26045_subsequence_two_pointer.py", "2\n3 2\n1 2 3\n1 3\n2 2\n1 2\n2 1\n", ["#1 YES", "#2 NO"]),
]


@pytest.mark.parametrize("path,stdin,expected", CASES, ids=[c[0].split("/")[-1] for c in CASES])
def test_solution(path, stdin, expected):
    assert run(path, stdin) == expected
