/*
    Write a function called zumZero which accepts a sorted array of integers.
    The function should find the first pair where the sum is 0.
    return an array that includes both values that sum to zero or undefined if
    a pair does not exists.
*/

function sumZero(arr){
    var left = 0;
    var right = arr.length - 1;
    while(left < right){
        var sum = arr[left] + arr[right];
        if(sum === 0){
            return [arr[left], arr[right]]
        } else if(sum > 0){
            right--;
        } else {
            left++;
        }
    }
}

sumZero([-4,-3,-2,-1,0,1,2,5])