# Recursion

#### Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

```tsx
function findCombination(ind: number, arr: number[], target: number, ans: number[][], ds: number[]) {
  if(ind == arr.length) {
    if(target == 0) {
      ans.push([...ds]);
    }
    return;
  }

  if(arr[ind] <= target) {
    ds.push(arr[ind]);
    findCombination(ind, arr, target - arr[ind], ans, ds);
    ds.pop();
  }

  findCombination(ind + 1, arr, target, ans, ds);
}


function combinationSum(candidates: number[], target: number): number[][] {

  let ans = []
  findCombination(0, candidates, target, ans, []);
  return ans
};

console.log(combinationSum([2, 3, 6, 7], 7));
```


```mermaid
graph TD
  Start --> Call_0["findCombination(0, arr, target, ans, ds)"]

  subgraph Level_0
    Call_0 --> If_0{"arr[0] <= target"}
    If_0 -->|Yes| Call_0_1["findCombination(0, arr, target-arr[0], ans, ds + arr[0])"]
    If_0 -->|No| Call_1_1["findCombination(1, arr, target, ans, ds)"]
  end
  
  subgraph Level_1
    Call_0_1 --> If_1{"arr[0] <= target"}
    If_1 -->|Yes| Call_0_2["findCombination(0, arr, target-arr[0], ans, ds + arr[0])"]
    If_1 -->|No| Call_1_2["findCombination(1, arr, target, ans, ds)"]
  end

  subgraph Level_2
    Call_1_1 --> If_2{"arr[1] <= target"}
    If_2 -->|Yes| Call_1_3["findCombination(1, arr, target-arr[1], ans, ds + arr[1])"]
    If_2 -->|No| Call_2_1["findCombination(2, arr, target, ans, ds)"]
  end

  subgraph Base_Case
    Call_2_1 --> End["if target == 0 { ans.push(ds) }"]
  end
```

#### Combination Sum II


```tsx
function findCombinations(ind, arr, target, ans, ds) {
  // Base case: if target is 0, add the current combination to the answer list
  if (target === 0) {
      ans.push([...ds]); // Copy the current combination and add it to ans
      return;
  }

  // Recursive case: iterate through the array
  for (let i = ind; i < arr.length; i++) {
      // Skip duplicates
      if (i > ind && arr[i] === arr[i - 1]) continue;
      
      // Break if the current number is greater than the target
      if (arr[i] > target) break;

      // Add the current number to the combination
      ds.push(arr[i]);

      // Recursive call to find combinations with updated index and reduced target
      findCombinations(i + 1, arr, target - arr[i], ans, ds);

      // Backtrack by removing the last element added
      ds.pop();
  }
}

function combinationSum2(candidates, target) {
  const ans = [];
  candidates.sort((a, b) => a - b); // Sort the candidates to handle duplicates
  findCombinations(0, candidates, target, ans, []);
  return ans;
}

// Example usage:
const candidates = [10, 1, 2, 7, 6, 1, 5];
const target = 8;
const result = combinationSum2(candidates, target);
console.log(result);

```


```mermaid
graph TD
    A["findCombinations(0, [10, 1, 2, 7, 6, 1, 5], 8, ans, ds)"] 
    A --> B1["findCombinations(1, [10, 1, 2, 7, 6, 1, 5], 7, ans, [1]) (Include 1)"]
    A --> C1["findCombinations(1, [10, 1, 2, 7, 6, 1, 5], 8, ans, []) (Skip 1)"]

    %% First Subtree (Starting with 1)
    B1 --> B2["findCombinations(2, [10, 1, 2, 7, 6, 1, 5], 6, ans, [1, 1]) (Include 1)"]
    B1 --> C2["findCombinations(2, [10, 1, 2, 7, 6, 1, 5], 7, ans, [1]) (Skip 1)"]
    B2 --> B3["findCombinations(3, [10, 1, 2, 7, 6, 1, 5], 4, ans, [1, 1, 2]) (Include 2)"]
    B3 --> B4["findCombinations(4, [10, 1, 2, 7, 6, 1, 5], -3, ans, [1, 1, 2, 7]) (Include 7 - Invalid)"]
    B3 --> C3["findCombinations(4, [10, 1, 2, 7, 6, 1, 5], 4, ans, [1, 1, 2]) (Skip 7)"]
    C3 --> B5["findCombinations(5, [10, 1, 2, 7, 6, 1, 5], -2, ans, [1, 1, 2, 6]) (Include 6 - Invalid)"]
    C3 --> C4["findCombinations(5, [10, 1, 2, 7, 6, 1, 5], 4, ans, [1, 1, 2]) (Skip 6)"]
    C4 --> B6["findCombinations(6, [10, 1, 2, 7, 6, 1, 5], -1, ans, [1, 1, 2, 5]) (Include 5 - Invalid)"]
    C4 --> C5["findCombinations(6, [10, 1, 2, 7, 6, 1, 5], 4, ans, [1, 1, 2]) (Skip 5)"]

    %% Skip Duplicate 1
    C1 --> C6["findCombinations(2, [10, 1, 2, 7, 6, 1, 5], 8, ans, []) (Skip 1 Duplicate)"]

    %% Subtree when 1 is included and 7 is included (Valid Combination)
    B2 --> V1["findCombinations(3, [10, 1, 2, 7, 6, 1, 5], 0, ans, [1, 1, 6]) (Include 7 - Valid!)"]
    V1 --> V2["Base case - [1, 1, 6]"]

    %% Second Subtree (Starting with 2)
    C6 --> B7["findCombinations(3, [10, 1, 2, 7, 6, 1, 5], 6, ans, [2]) (Include 2)"]
    B7 --> B8["findCombinations(4, [10, 1, 2, 7, 6, 1, 5], -1, ans, [2, 7]) (Include 7 - Invalid)"]
    B7 --> C7["findCombinations(4, [10, 1, 2, 7, 6, 1, 5], 6, ans, [2]) (Skip 7)"]
    C7 --> B9["findCombinations(5, [10, 1, 2, 7, 6, 1, 5], 0, ans, [2, 6]) (Include 6 - Valid!)"]
    B9 --> V3["Base case - [1, 2, 5]"]

    %% Subtree for Skipping Elements
    C7 --> C8["findCombinations(5, [10, 1, 2, 7, 6, 1, 5], 5, ans, [2]) (Skip 6)"]
    C8 --> B10["findCombinations(6, [10, 1, 2, 7, 6, 1, 5], 0, ans, [1, 7]) (Include 5 - Valid!)"]
    B10 --> V4["Base case - [1, 7]"]

    %% Further branches omitted for clarity

```


#### Subset Sum II

```tsx
function findSubsets(ind: number, nums, ds: number[], ans: number[][]) {
  ans.push([...ds]);
  for (let i = ind; i < nums.length; i++) {
    if (i !== ind && nums[i] === nums[i - 1]) continue;
    ds.push(nums[i]);
    findSubsets(i + 1, nums, ds, ans);
    ds.pop();
  }
}

function subsetsWithDup(nums: number[]): number[][] {
  let ans = [];
  nums.sort();
  findSubsets(0, nums, [], ans);
  return ans;
}
```

```mermaid
graph TD
    A["findSubsets(0, [1, 1, 2, 4], [], ans)"] 
    A --> B1["findSubsets(1, [1, 1, 2, 4], [1], ans) (Include 1)"]
    A --> C1["findSubsets(1, [1, 1, 2, 4], [], ans) (Skip 1)"]

    %% First Subtree (Starting with 1)
    B1 --> B2["findSubsets(2, [1, 1, 2, 4], [1, 1], ans) (Include 1)"]
    B1 --> C2["findSubsets(2, [1, 1, 2, 4], [1], ans) (Skip 1)"]
    
    %% First Subtree when [1, 1] is included
    B2 --> B3["findSubsets(3, [1, 1, 2, 4], [1, 1, 2], ans) (Include 2)"]
    B3 --> B4["findSubsets(4, [1, 1, 2, 4], [1, 1, 2, 4], ans) (Include 4)"]
    B4 --> V1["Base case - Add [1, 1, 2, 4] to ans"]

    B3 --> C3["findSubsets(4, [1, 1, 2, 4], [1, 1, 2], ans) (Skip 4)"]
    C3 --> V2["Base case - Add [1, 1, 2] to ans"]
    
    B2 --> C4["findSubsets(3, [1, 1, 2, 4], [1, 1], ans) (Skip 2)"]
    C4 --> B5["findSubsets(4, [1, 1, 2, 4], [1, 1, 4], ans) (Include 4)"]
    B5 --> V3["Base case - Add [1, 1, 4] to ans"]
    C4 --> V4["Base case - Add [1, 1] to ans"]

    %% First Subtree when [1] is included, [1] skipped
    C2 --> B6["findSubsets(3, [1, 1, 2, 4], [1, 2], ans) (Include 2)"]
    B6 --> B7["findSubsets(4, [1, 1, 2, 4], [1, 2, 4], ans) (Include 4)"]
    B7 --> V5["Base case - Add [1, 2, 4] to ans"]

    B6 --> C5["findSubsets(4, [1, 1, 2, 4], [1, 2], ans) (Skip 4)"]
    C5 --> V6["Base case - Add [1, 2] to ans"]

    C2 --> B8["findSubsets(4, [1, 1, 2, 4], [1, 4], ans) (Include 4)"]
    B8 --> V7["Base case - Add [1, 4] to ans"]
    C2 --> V8["Base case - Add [1] to ans"]

    %% Skip duplicate 1 (first subtree skipping [1, 1])
    C1 --> B9["findSubsets(2, [1, 1, 2, 4], [2], ans) (Include 2)"]
    B9 --> B10["findSubsets(3, [1, 1, 2, 4], [2, 4], ans) (Include 4)"]
    B10 --> V9["Base case - Add [2, 4] to ans"]

    B9 --> C6["findSubsets(4, [1, 1, 2, 4], [2], ans) (Skip 4)"]
    C6 --> V10["Base case - Add [2] to ans"]

    C1 --> B11["findSubsets(3, [1, 1, 2, 4], [4], ans) (Include 4)"]
    B11 --> V11["Base case - Add [4] to ans"]
    C1 --> V12["Base case - Add [] to ans"]

```