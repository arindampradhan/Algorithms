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