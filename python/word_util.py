from typing import List, Set


def sides_to_letter_set(sides: List[str]) -> Set[str]:
    result = set()
    for side in sides:
        for c in side:
            result.add(c)
    return result
