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

console.log(subsetsWithDup([4,1,1,2]))