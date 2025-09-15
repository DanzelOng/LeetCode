class BrowserHistory:
    '''

    Time Complexities:
    - visit() :   O(1)
    - back():     O(1)
    - forward():  O(1)

    Space Complexity: O(n)

    To solve this problem, we use an append-only list to store
    the sequence of visited URLs, and two pointers to navigate 
    the history efficiently.

    - 'idx' points to the current page.
    - 'end' marks the furthest valid page.

    When visiting a new URL:
    - Increment 'idx' to move forward.
    - If there is already a slot at 'idx' in the list, overwrite
      it with the new URL. Otherwise, append the URL to the list.
    - Update 'end = idx' to logically discard any forward history
      beyond this point.

    When moving back or forward:
    - Adjust 'idx' by 'steps', clamped to valid bounds (0 for back,
      'end' for forward).
    - Return the URL at 'history[idx]'.

    This approach avoids any slicing or node traversal and provides
    constant time access for all operations.

    '''

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.idx = self.end = 0

    def visit(self, url: str) -> None:
        self.idx += 1

        if self.idx < len(self.history):
            self.history[self.idx] = url
        else:
            self.history.append(url)  

        self.end = self.idx      
  
    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx - steps)
        return self.history[self.idx]
 
    def forward(self, steps: int) -> str:
        self.idx = min(self.end, self.idx + steps)
        return self.history[self.idx]

'''

    Doubly Linked List Approach

    Time Complexities:
    - visit():    O(1)
    - back():     O(steps)
    - forward():  O(steps)

    Space Complexity: O(n)

    class BrowserHistory:
        class URLNode:
            def __init__(self, url, prev=None, nxt=None):
                self.url = url
                self.prev = prev
                self.next = nxt
        
        class DLL:
            def __init__(self, root):
                self.pnter = BrowserHistory.URLNode(url=root)

        def __init__(self, homepage: str):
            self.browserHistory = BrowserHistory.DLL(root=homepage)

        def visit(self, url: str) -> None:
            cur = self.browserHistory.pnter
            cur.next = BrowserHistory.URLNode(url=url)
            cur.next.prev = cur
            self.browserHistory.pnter = cur.next

        def back(self, steps: int) -> str:
            cur = self.browserHistory.pnter

            for _ in range(steps):
                if cur.prev is None:
                    break

                cur = cur.prev
                self.browserHistory.pnter = cur

            return self.browserHistory.pnter.url

        def forward(self, steps: int) -> str:
            cur = self.browserHistory.pnter

            for _ in range(steps):
                if cur.next is None:
                    break

                cur = cur.next
                self.browserHistory.pnter = cur
            
            return self.browserHistory.pnter.url

'''