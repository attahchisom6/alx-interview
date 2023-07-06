def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n  # Keeps track of visited boxes
    visited[0] = True  # Mark the first box as visited
    stack = [0]  # Stack to perform DFS
    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                stack.append(key)
    return all(visited)
