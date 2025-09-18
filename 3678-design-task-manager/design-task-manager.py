from heapq import heapify, heappush, heappop

class TaskManager:
    '''

    Time Complexities:
    - __init__()         : O(n)
    - add()              : O(logn)
    - edit()             : O(logn)
    - rmv()              : O(1)
    - execTop()          
      Best Case          : O(logn)   # top of heap is valid
      Average/Worst Case : O(nlogn)  # many stale entries in heap precedes a valid entry

    Space Complexity: O(n)

    To support all task manager operations efficiently, we use 
    a max-heap with lazy deletion together with hash tables.

    Two hash tables are used as the source of truth for retrieving
    information for a task.

    (1) taskUsers    : This maps each task to its specified user.
    (2) tasksPriority: This maps each task to its current priority.

    The max-heap takes care of the ordering of all tasks, which executes
    and returns the task with the highest priority. In the case where 
    multiple tasks have the same priority, its taskId is used as the tie-breaker. 

    Operations:

    add(): Inserts the new task into both hash tables and the heap.

    edit(): Updates the task's existing priority and pushes the updated entry 
            (-newPriority, -taskId) into the heap. The stale entry is left in place 
            be discarded during execution by lazy deletion.

    rmv(): Removes the task from both hash tables. Existing heap entries for this 
            task (including those with outdated priorities) become stale and will 
            be discarded during execution by lazy deletion. Since no heap operations
            are involved, removing a task takes O(1) time.

    execTop(): Repeatedly pops the top of the heap and validates it against the 
               maps. An entry is stale if its taskId no longer exists or if its 
               priority does not match the current value. Once a valid entry is 
               found, its entry is removed from the maps and its userId is returned.
               If no valid entry remains, returns -1.

    With the lazy deletion strategy, expensive in-heap updates at avoided at the 
    cost of popping several stale entries. As a result, a single execTop() may
    degrade to O(nlogn) in the worst case if many stale entries precede the next 
    valid one. However, across many operations the amortized behavior remains 
    efficient because each stale heap entry is popped at most once.

    '''

    def __init__(self, tasks: List[List[int]]):
        self.tasksHeap = []
        self.tasksUsers = {}      # taskId -> userId
        self.tasksPriority = {}   # taskId -> priority
        
        for userId, taskId, priority in tasks:
            self.tasksUsers[taskId] = userId
            self.tasksPriority[taskId] = priority
            self.tasksHeap.append( (-priority, -taskId) )
        
        heapify(self.tasksHeap)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasksUsers[taskId] = userId
        self.tasksPriority[taskId] = priority
        heappush(self.tasksHeap, (-priority, -taskId) )

    def edit(self, taskId: int, newPriority: int) -> None:
        self.tasksPriority[taskId] = newPriority
        heappush(self.tasksHeap, (-newPriority, -taskId) )

    def rmv(self, taskId: int) -> None:
        del self.tasksUsers[taskId]
        del self.tasksPriority[taskId]
    
    def execTop(self) -> int:
        while self.tasksHeap:
            priority, taskId = heappop(self.tasksHeap)

            if self.tasksPriority.get(-taskId) == -priority:
                userId = self.tasksUsers.get(-taskId)
                del self.tasksUsers[-taskId]
                del self.tasksPriority[-taskId]
                return userId

        return -1

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()