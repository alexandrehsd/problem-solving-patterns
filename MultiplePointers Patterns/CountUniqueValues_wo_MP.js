/*
    write a function that receives an ordered array 
    and counts how many unique values there are 
    in the array. There can be negative numbers
    in the array.
*/

function CountUniqueValues(arr){
    if(arr.length < 2){
        return arr.length;
    }
    uniqueCounter = 1; // i. e., there exists at least one unique value in the array
    for(var i=1; i<arr.length; i++){
        if(arr[i] !== arr[i-1]){
            uniqueCounter++;
        }
    }
    return uniqueCounter;
}

console.log(CountUniqueValues([1,2,3,4,5,6,7]));