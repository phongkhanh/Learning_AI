import itertools
import random

# Danh sách người chơi và cấp độ
group_a = [
    ("Đạt", 0), ("Phong", 1), ("Thành", 1), ("Minh", 1), ("Hoàng", 2),
    ("Tài", 2), ("Nguyên", 2), ("Việt Anh", 2), ("Đức", 2), ("a.Duy", 2), ("Long", 3)
]

group_b = [
    ("Khang", 0), ("Kiệt", 1), ("Sơn", 2), ("Khoa", 2), ("Nam", 2),
    ("Mến", 3), ("Tùng", 3), ("Duy", 3), ("Tuấn", 4)
]

# Hàm tính tổng level của cặp đôi
def pair_level(pair):
    return pair[0][1] + pair[1][1]

# Hàm kiểm tra điều kiện
def is_valid_match(matches, match):
    if len(matches) == 0:
        return True
    
    # Kiểm tra điều kiện không có người chơi nào đánh liên tiếp
    last_match = matches[-1]
    if (match[0][0] in [last_match[0][0], last_match[0][1][0]] or
        match[0][1] in [last_match[0][0], last_match[0][1][0]] or
        match[1][0] in [last_match[1][0], last_match[1][1][0]] or
        match[1][1] in [last_match[1][0], last_match[1][1][0]]):
        return False
    
    # Kiểm tra tổng level của các cặp đôi trong nhóm không chênh nhau 1 level
    match_level_a = pair_level(match[0])
    match_level_b = pair_level(match[1])
    for m in matches:
        last_match_level_a = pair_level(m[0])
        last_match_level_b = pair_level(m[1])
        if abs(match_level_a - last_match_level_a) > 1 or abs(match_level_b - last_match_level_b) > 1:
            return False
    
    return True

# Hàm tạo danh sách trận đấu
def create_matches(group_a, group_b):
    matches = []
    
    a_players = group_a[:]
    b_players = group_b[:]
    
    a_combinations = list(itertools.combinations(a_players, 2))
    b_combinations = list(itertools.combinations(b_players, 2))
    
    random.shuffle(a_combinations)
    random.shuffle(b_combinations)
    
    used_a_players = set()
    used_b_players = set()

    while len(matches) < 10 and (a_combinations or b_combinations):
        for a_pair in a_combinations:
            if a_pair[0] in used_a_players or a_pair[1] in used_a_players:
                continue
            for b_pair in b_combinations:
                if b_pair[0] in used_b_players or b_pair[1] in used_b_players:
                    continue
                match = (a_pair, b_pair)
                if is_valid_match(matches, match):
                    matches.append(match)
                    used_a_players.update(a_pair)
                    used_b_players.update(b_pair)
                    break
            else:
                continue
            break
        
        a_combinations = [pair for pair in a_combinations if pair[0] not in used_a_players and pair[1] not in used_a_players]
        b_combinations = [pair for pair in b_combinations if pair[0] not in used_b_players and pair[1] not in used_b_players]

    return matches

matches = create_matches(group_a, group_b)

# In kết quả
for i, match in enumerate(matches):
    print(f"Match {i + 1}:")
    print(f"  Group A: {match[0][0][0]} & {match[0][1][0]}")
    print(f"  Group B: {match[1][0][0]} & {match[1][1][0]}")
    print()
