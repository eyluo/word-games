# Letter Boxed


### Rules

- Connect letters to spell words
- Words must be at least 3 letters long
- Letters can be reused
- Consecutive letters cannot be from the same side
- The last letter of a word becomes the first letter of the next word
    e.g. THY > YES > SINCE
- Words cannot be proper nouns or hyphenated
- No cussing either, sorry
- Use all letters to solve!

### Design

1. Generate every word
1. Create a directed graph
    - Every node is a word
    - Node A connects to node B __iff__ the last letter of node A is the first letter of node B
1. 

### Questions

1. How to handle cycles? I think we should evaluate cycles and remove them if they don't 
1. Does NYT always specify how many words the answer has? If so, this will limit the search problem