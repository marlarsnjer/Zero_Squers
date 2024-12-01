def heuristic(self, B_matrix):
    # تعريف الأهداف والمحركات
    targets = {'M': [], 'A': [], 'L': []}  # الأهداف
    movers = {'R': [], 'B': [], 'O': []}   # المحركات

    # البحث عن مواقع الأهداف والمحركات في المصفوفة
    for i in range(len(B_matrix)):
        for j in range(len(B_matrix[i])):
            if B_matrix[i][j] in targets:  # إذا كانت الخلية هدفًا
                targets[B_matrix[i][j]].append((i, j))
            elif B_matrix[i][j] in movers:  # إذا كانت الخلية محركًا
                movers[B_matrix[i][j]].append((i, j))

    # حساب المسافة المانهاتنية لكل محرك إلى أقرب هدف له
    total_distance = 0
    for mover in movers:
        for (mx, my) in movers[mover]:  # لكل محرك
            min_distance = float('inf')  # قيمة المسافة الدنيا
            for (tx, ty) in targets[mover]:  # لكل هدف
                # حساب المسافة المانهاتنية بين المحرك والهدف
                distance = abs(mx - tx) + abs(my - ty)
                min_distance = min(min_distance, distance)  # اختيار أقرب هدف
            total_distance += min_distance  # إضافة المسافة الأقرب إلى إجمالي المسافة

    return total_distance








import heapq  # استيراد مكتبة القائمة ذات الأولوية

def astar(self):
    initial_state = self.state_ins  # الحالة الابتدائية
    pq = []  # قائمة الانتظار ذات الأولوية
    heapq.heappush(pq, (0, initial_state, []))  # إضافة الحالة الأولية إلى القائمة
    visited = set()  # مجموعة لتخزين الحالات التي تمت زيارتها

    while pq:  # طالما هناك حالات في قائمة الانتظار
        cost, current_state, path = heapq.heappop(pq)  # أخذ الحالة ذات التكلفة الأقل

        # إذا تم الوصول إلى الهدف
        if current_state.check_win(current_state.mattrix):
            print("Solution found with A*: Path:", path)
            return path

        # إذا تم زيارة هذه الحالة مسبقًا، نتجاوزها
        if current_state in visited:
            continue
        visited.add(current_state)

        # الحركات الممكنة
        directions = ['up', 'down', 'left', 'right']
        for direction in directions:
            new_state = current_state.move1(current_state, direction)  # تطبيق الحركة
            g_cost = len(path) + 1  # حساب تكلفة الحركة (عدد الخطوات)
            h_cost = self.heuristic(new_state.mattrix)  # تقدير المسافة باستخدام heuristic
            f_cost = g_cost + h_cost  # التكلفة الإجمالية

            # إذا كانت الحالة لم تتم زيارتها بعد
            if new_state not in visited:
                heapq.heappush(pq, (f_cost, new_state, path + [direction]))  # إضافة الحالة إلى القائمة

    print("No solution found with A*.")
    return None
