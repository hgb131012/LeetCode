/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    return nums.map((n) => {
        return n ** 2
    }).sort((a, b) => a - b);
};
