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
    
    while len(matches) < 10:
        # Sinh tất cả các cặp đôi có thể
        a_pairs = list(itertools.combinations(a_players, 2))
        b_pairs = list(itertools.combinations(b_players, 2))
        
        # Xáo trộn các cặp đôi để tìm kiếm ngẫu nhiên
        random.shuffle(a_pairs)
        random.shuffle(b_pairs)
        
        # Tìm cặp đôi hợp lệ
        for a_pair in a_pairs:
            for b_pair in b_pairs:
                match = (a_pair, b_pair)
                if is_valid_match(matches, match):
                    matches.append(match)
                    a_players.remove(a_pair[0])
                    a_players.remove(a_pair[1])
                    b_players.remove(b_pair[0])
                    b_players.remove(b_pair[1])
                    break
            else:
                continue
            break
    
    return matches

matches = create_matches(group_a, group_b)

# In kết quả
for i, match in enumerate(matches):
    print(f"Match {i + 1}:")
    print(f"  Group A: {match[0][0][0]} & {match[0][1][0]}")
    print(f"  Group B: {match[1][0][0]} & {match[1][1][0]}")
    print()
