from analyzer import Task, BehaviorAnalyzer
from storage import Storage

def main():
    raw_data = Storage.load_tasks()
    tasks = [Task(**d) for d in raw_data]
    
    while True:
        print("\n--- 🧠 Procrastination Detector ---")
        print("1. Add Task\n2. Mark Task Completed\n3. View Analysis\n4. Exit")
        choice = input("Select: ")

        if choice == '1':
            name = input("Task Name: ")
            pri = int(input("Priority (1-High, 10-Low): "))
            dur = input("Est. Minutes: ")
            tasks.append(Task(name, pri, dur))
            Storage.save_tasks(tasks)
        
        elif choice == '2':
            pending = [t for t in tasks if not t.completed]
            for i, t in enumerate(pending):
                print(f"{i}. {t.name} (P:{t.priority})")
            idx = int(input("Select task index: "))
            
            # Set execution order based on current completion count
            exec_count = len([t for t in tasks if t.completed])
            target_task = pending[idx]
            for t in tasks:
                if t.name == target_task.name:
                    t.completed = True
                    t.exec_order = exec_count + 1
            Storage.save_tasks(tasks)

        elif choice == '3':
            score, status, insights = BehaviorAnalyzer.calculate_score(tasks)
            print(f"\n📊 Procrastination Score: {score}")
            print(f"💡 Insight: {status}")
            for line in insights: print(line)
        
        elif choice == '4':
            break

if __name__ == "__main__":
    main()