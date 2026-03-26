#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <fstream>
#include <algorithm>

using namespace std;

struct Task {
    string name;
    int priority; // 1 (High) to 10 (Low)
    int execOrder;
    bool completed;

    // Overload for Priority Queue (Min-Heap based on priority)
    bool operator>(const Task& other) const {
        return priority > other.priority;
    }
};

class ProcrastinationManager {
private:
    vector<Task> tasks;

public:
    void addTask(string n, int p) {
        tasks.push_back({n, p, -1, false});
    }

    void completeTask(string n) {
        int currentCount = 0;
        for (const auto& t : tasks) if (t.completed) currentCount++;
        
        for (auto& t : tasks) {
            if (t.name == n) {
                t.completed = true;
                t.execOrder = currentCount + 1;
            }
        }
    }

    void analyze() {
        priority_queue<Task, vector<Task>, greater<Task>> pq;
        vector<Task> completedTasks;

        for (const auto& t : tasks) {
            pq.push(t);
            if (t.completed) completedTasks.push_back(t);
        }

        sort(completedTasks.begin(), completedTasks.end(), [](Task a, Task b) {
            return a.execOrder < b.execOrder;
        });

        int score = 0;
        cout << "\n--- Behavior Analysis ---\n";
        for (auto& actual : completedTasks) {
            Task ideal = pq.top();
            pq.pop();

            if (actual.priority > ideal.priority) {
                score += (actual.priority - ideal.priority) * 10;
                cout << "[!] Procrastinated on: " << ideal.name << " by doing " << actual.name << endl;
            }
        }
        cout << "Final Procrastination Score: " << score << endl;
        if(score > 20) cout << "Result: High avoidance behavior detected." << endl;
        else cout << "Result: Strong focus on high-priority tasks." << endl;
    }

    void saveToFile() {
        ofstream out("tasks.txt");
        for (const auto& t : tasks) {
            out << t.name << " " << t.priority << " " << t.completed << " " << t.execOrder << endl;
        }
    }
};

int main() {
    ProcrastinationManager pm;
    pm.addTask("Fix Bug A", 1);
    pm.addTask("Write Documentation", 5);
    pm.addTask("Check Emails", 8);

    cout << "Simulating: Doing low priority task 'Check Emails' first..." << endl;
    pm.completeTask("Check Emails");
    pm.analyze();

    return 0;
}