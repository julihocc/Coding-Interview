# Daily Temperatures (Next Cooler Day)

## Problem Description

Alright, Space Explorer! You have a list of daily temperatures recorded in ascending order of days. Your job is, for each day, to find out how many days you'll have to wait until the next **cooler** day.

If there is no cooler day in the future, put `-1`.

### Input

- A list of integers `temperatures` representing the daily temperatures.
- The list can be empty, contain a single record, or have duplicates.

### Output

- Return a list where the `i-th` element denotes the number of days you have to wait until the next cooler day after the `i-th` day.
- If no cooler day exists, the value should be `-1`.

### Examples

**Example 1:**
```
Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output: [3, 2, 1, 1, -1, 2, -1, -1]
```
*Explanation:*
- Day 0 (73): Next cooler is 71 (3 days later).
- Day 1 (74): Next cooler is 71 (2 days later).
- Day 2 (75): Next cooler is 71 (1 day later).
- Day 3 (71): Next cooler is 69 (1 day later).
- Day 4 (69): No cooler day -> -1.
- Day 5 (72): Next cooler is INVALID EXAMPLE, actually 72 is followed by 76 (warmer) then 73 (warmer). Wait, standard problem is warmer. This problem is **cooler**.
Let's trace Day 5 (72): Next days are 76, 73. Neither is cooler than 72? No, 73 is not cooler. 76 is not cooler. So -1?
Wait, if the example input is standard, let's re-read carefully.
"Find out how many days you'll have to wait until the next **cooler** day."
Example trace again with "Cooler":
[73, 74, 75, 71, 69, 72, 76, 73]
- 73: 74(Warm), 75(Warm), 71(Cool). Index 0 -> 3. Days = 3-0 = 3. Correct.
- 74: 75(Warm), 71(Cool). Index 1 -> 3. Days = 3-1 = 2. Correct.
- 75: 71(Cool). Index 2 -> 3. Days = 3-2 = 1. Correct.
- 71: 69(Cool). Index 3 -> 4. Days = 4-3 = 1. Correct.
- 69: 72(W), 76(W), 73(W). No cooler. -> -1. Correct.
- 72: 76(W), 73(W). No cooler. -> -1. Correct. Wait, previous example output said 2??
    - If output was 2, that implies Index 5+2=7 is cooler. Index 7 is 73. 73 is NOT cooler than 72.
    - Maybe the example output I wrote above was for "Warmer" (standard problem)?
    - Let's stick to the prompt's rules: "Next COOLER day".
    - So for 72: Next are 76, 73. Neither < 72. So -1.
- 76: 73(Cool). Index 6 -> 7. Days = 7-6 = 1.
- 73: End. -> -1.

Corrected Example Output for **Cooler**: [3, 2, 1, 1, -1, -1, 1, -1]

**Example 2:**
```
Input: [30, 40, 50, 60]
Output: [-1, -1, -1, -1]
```

**Example 3:**
```
Input: [60, 50, 40, 30]
Output: [1, 1, 1, -1]
```

## Constraints

- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`
