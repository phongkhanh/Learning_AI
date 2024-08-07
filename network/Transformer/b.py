import random
from collections import Counter

# Danh sách nhóm
group_a = [
    ("Đạt", 0),
    ("Phong", 1),
    ("Thành", 1),
    ("Minh", 1),
    ("Hoàng", 2),
    ("Tài", 2),
    ("Nguyên", 2),
    ("Việt Anh", 2),
    ("Đức", 2),
    ("a.Duy", 2),
    ("Long", 3)
]

group_b = [
    ("Khang", 0),
    ("Kiệt", 1),
    ("Sơn", 2),
    ("Khoa", 2),
    ("Nam", 2),
    ("Mến", 3),
    ("Tùng", 3),
    ("Duy", 3),
    ("Tuấn", 4)
]

# Hàm tìm các cặp có tổng level
def find_pairs(group, target_sum):
    pairs = []
    for i in range(len(group)):
        for j in range(i+1, len(group)):
            if group[i][1] + group[j][1] in (target_sum - 1, target_sum, target_sum + 1):
                pairs.append((group[i], group[j]))
    return pairs

# Hàm kiểm tra xem người đã chơi không bị chọn liên tiếp
def valid_match(match, last_match):
    return not (last_match and (match[0] in last_match or match[1] in last_match))

# Hàm ưu tiên người có level cao hơn (số nhỏ hơn)
def priority_match_players(group, match_counts):
    # Sắp xếp nhóm theo level từ thấp đến cao (0 là level cao nhất)
    sorted_group = sorted(group, key=lambda x: x[1])
    return sorted_group

# Hàm cân bằng số trận tham gia của từng thành viên
def balance_matches(matches, group_a, group_b):
    match_counts_a = Counter(player for match in matches for player in match[0])
    match_counts_b = Counter(player for match in matches for player in match[1])
    
    while len(matches) < 10 or any(count == 0 for player, count in match_counts_a.items() if player in dict(group_a)) or any(count == 0 for player, count in match_counts_b.items() if player in dict(group_b)):
        if len(matches) >= 10:
            break
        
        # Tạo thêm trận đấu để đảm bảo tất cả thành viên được tham gia
        for player_a in priority_match_players(group_a, match_counts_a):
            if match_counts_a[player_a[0]] == 0:
                remaining_players_b = [p for p in priority_match_players(group_b, match_counts_b) if match_counts_b[p[0]] == 0]
                if remaining_players_b:
                    player_b = random.choice(remaining_players_b)
                    remaining_players_b.remove(player_b)
                    player_b2 = random.choice(remaining_players_b) if remaining_players_b else random.choice(group_b)
                    
                    matches.append(((player_a, player_b), (player_b2, player_b)))
                    match_counts_a[player_a[0]] += 1
                    match_counts_b[player_b[0]] += 1
                    match_counts_b[player_b2[0]] += 1
                    break
    
    return matches

# Hàm thực hiện lựa chọn và in kết quả
def create_matches(group_a, group_b, num_matches):
    matches = []
    match_counts_a = Counter(player[0] for player in group_a)
    match_counts_b = Counter(player[0] for player in group_b)
    
    last_match_a = None
    last_match_b = None
    
    while len(matches) < num_matches:
        sorted_group_a = priority_match_players(group_a, match_counts_a)
        players_a = random.sample(sorted_group_a, 2)
        total_level_a = players_a[0][1] + players_a[1][1]
        
        valid_pairs = find_pairs(group_b, total_level_a)
        random.shuffle(valid_pairs)
        
        match_found = False
        for pair_b in valid_pairs:
            if valid_match(pair_b, last_match_b):
                matches.append((players_a, pair_b))
                last_match_a = players_a
                last_match_b = pair_b
                match_counts_a[players_a[0][0]] += 1
                match_counts_a[players_a[1][0]] += 1
                match_counts_b[pair_b[0][0]] += 1
                match_counts_b[pair_b[1][0]] += 1
                match_found = True
                break
        
        if not match_found:
            continue
    
    matches = balance_matches(matches, group_a, group_b)
    
    # In kết quả
    for i, (match_a, match_b) in enumerate(matches):
        print(f"Match {i+1}:")
        print(f"  Group A: {match_a[0][0]} (Level {match_a[0][1]}), {match_a[1][0]} (Level {match_a[1][1]})")
        print(f"  Group B: {match_b[0][0]} (Level {match_b[0][1]}), {match_b[1][0]} (Level {match_b[1][1]})")
    
    print("\nMatch counts in Group A:")
    for player, count in match_counts_a.items():
        print(f"  {player}: {count} matches")
    
    print("\nMatch counts in Group B:")
    for player, count in match_counts_b.items():
        print(f"  {player}: {count} matches")

# Thực hiện tạo các trận đấu
create_matches(group_a, group_b, 20)
