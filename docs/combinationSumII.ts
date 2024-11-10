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
