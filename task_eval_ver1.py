# タスク管理用辞書
a = {}
scores = {}
task_totals={}
# タスク入力
print("タスクを5つ入力してください。全角スペースで区切ってね")
tasks = list(input().split())

# 各タスクを3つに分割
for task in tasks:
    print(f"{task} を3つに分割してください")
    components = list(input().split())
    if len(components) != 3:
        print("※3つに分割してください。もう一度入力")
        components = list(input().split())
    a[task] = components

# 各要素を評価
for task in tasks:
    for component in a[task]:
        print(f"{component} の報酬、心理的負荷、時間を0~9で評価してください（半角スペースで区切る）")
        score = list(map(int, input().split()))
        while len(score) != 3 or any(s < 0 or s > 9 for s in score):
            print("※0~9の数字を3つ入力してください。もう一度入力")
            score = list(map(int, input().split()))
        scores[component] = score

# 結果出力
print("\n=== 入力結果 ===")

for task in tasks:
    print(f"\nタスク: {task}")
    total_score = 0

    for component in a[task]:
        reward = scores[component][0]
        stress = scores[component][1]
        time = scores[component][2]

        score_sum = reward*2 - stress*1.5 - time
        total_score += score_sum

        print(f"  {component} → 報酬:{reward}, 心理的負荷:{stress}, 時間:{time}, 合算:{score_sum:.1f}")

    task_totals[task] = total_score
    print(f"  タスク合計スコア: {total_score:.1f}")

print("\n=== タスク優先順位 ===")

ranking = sorted(task_totals.items(), key=lambda x: x[1], reverse=True)

for i, (task, score) in enumerate(ranking, 1):
    print(f"{i}位: {task} (スコア {score:.1f})")
