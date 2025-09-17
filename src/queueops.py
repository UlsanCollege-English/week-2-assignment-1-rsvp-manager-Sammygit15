from typing import List, Tuple

def take_next(queue: List[str]) -> Tuple[str | None, List[str]]:
    if queue:
        return queue[0], queue[1:]  # Return the first element and the rest of the queue
    else:
        return None, []  # Return None and an empty list if the queue is empty

def move_to_back(queue: List[str], name: str) -> List[str]:
    if name in queue:
        # Find the index of the first occurrence of name and move it to the back
        index = queue.index(name)
        return queue[:index] + queue[index+1:] + [name]
    return queue  # If name is not in the list, return the queue unchanged

def interleave(q1: List[str], q2: List[str]) -> List[str]:
    result = []
    # Interleave elements from both lists
    while q1 and q2:
        result.append(q1.pop(0))  # Take the first element from q1
        result.append(q2.pop(0))  # Take the first element from q2
    # Add the remaining elements of the longer list
    result.extend(q1)
    result.extend(q2)
    return result
