function permute(nums: number[]): number[][] {
  const ans: number[][] = [];
  const ds: number[] = [];
  const freq: boolean[] = Array(nums.length).fill(false);

  function recurPermute(ds: number[], nums: number[], ans: number[][], freq: boolean[]): void {
      if (ds.length === nums.length) {
          ans.push([...ds]); // Push a copy of ds to avoid mutation
          return;
      }
      for (let i = 0; i < nums.length; i++) {
          if (!freq[i]) {
              ds.push(nums[i]);
              freq[i] = true;
              recurPermute(ds, nums, ans, freq);
              freq[i] = false;
              ds.pop();
          }
      }
  }

  recurPermute(ds, nums, ans, freq);
  return ans;
}

// Usage example
const nums = [1, 2, 3];
console.log("All Permutations are:", permute(nums));
