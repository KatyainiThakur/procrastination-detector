import heapq

class Task:
    def __init__(self, name, priority, duration, completed=False, exec_order=None):
        self.name = name
        self.priority = int(priority)  # 1 (High) to 10 (Low)
        self.duration = duration
        self.completed = completed
        self.exec_order = exec_order

class BehaviorAnalyzer:
    @staticmethod
    def calculate_score(tasks):
        completed_tasks = [t for t in tasks if t.completed]
        if not completed_tasks:
            return 0, "No data yet.", []

        # DSA: Priority Queue to get the "Ideal" order
        # We use a min-heap because Priority 1 > Priority 10
        ideal_pq = []
        for t in tasks:
            heapq.heappush(ideal_pq, (t.priority, t.name))

        # Sort completed tasks by their actual execution order
        actual_order = sorted(completed_tasks, key=lambda x: x.exec_order)
        
        procrastination_score = 0
        insights = []

        for i, actual_task in enumerate(actual_order):
            ideal_priority, ideal_name = heapq.heappop(ideal_pq)
            
            # Logic: If actual priority is numerically higher (less important) 
            # than what was available in the ideal heap.
            if actual_task.priority > ideal_priority:
                procrastination_score += (actual_task.priority - ideal_priority) * 10
                insights.append(f"⚠️ Delayed '{ideal_name}' to work on '{actual_task.name}'")

        if procrastination_score == 0:
            status = "Excellent discipline! You followed priorities perfectly."
        elif procrastination_score < 30:
            status = "Fairly productive, but minor distractions noted."
        else:
            status = "High Procrastination: You are avoiding high-impact tasks."

        return procrastination_score, status, insights