import heapq

class TaskManager:
    def __init__(self, tasks):
        # tasks is a list of [userId, taskId, priority]
        self.heap = []  # max-heap simulated with (-priority, taskId)
        self.taskPriority = {}  # taskId -> priority
        self.taskOwner = {}     # taskId -> userId

        for task in tasks:
            self.add(task[0], task[1], task[2])

    def add(self, userId, taskId, priority):
        heapq.heappush(self.heap, (-priority, taskId))
        self.taskPriority[taskId] = priority
        self.taskOwner[taskId] = userId

    def edit(self, taskId, newPriority):
        heapq.heappush(self.heap, (-newPriority, taskId))
        self.taskPriority[taskId] = newPriority

    def rmv(self, taskId):
        self.taskPriority[taskId] = -1  # mark as removed

    def execTop(self):
        while self.heap:
            priority, taskId = heapq.heappop(self.heap)
            priority = -priority  # convert back

            # Check if this task is still valid
            if self.taskPriority.get(taskId, -1) == priority:
                self.taskPriority[taskId] = -1  # mark as executed
                return self.taskOwner[taskId]   # return userId
        return -1


# Example usage
if __name__ == "__main__":
    initTasks = [
        [1, 101, 5],
        [2, 102, 3],
        [1, 103, 7]
    ]

    tm = TaskManager(initTasks)

    print("ExecTop: User", tm.execTop())  # Executes task 103 (priority 7)

    tm.add(3, 104, 10)
    print("ExecTop: User", tm.execTop())  # Executes task 104

    tm.edit(102, 9)
    print("ExecTop: User", tm.execTop())  # Executes task 102

    tm.rmv(101)
    print("ExecTop: User", tm.execTop())  # -1 (no valid tasks left)
