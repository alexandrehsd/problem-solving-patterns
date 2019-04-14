/*
    write a function that receives an ordered array 
    and counts how many unique values there are 
    in the array. There can be negative numbers
    in the array.

    note: In this version, pay attention at how much less
    operations we can perform when compared to the
    CountUniqueValues function in the version without Multiple
    Pointers.
*/

function countUniqueValues(arr){
    if(arr.length === 0){
        return 0;
    }
    var i = 0;
    for(var j = 1; j<arr.length; j++){
        if(arr[j] !== arr[i]){
            i++;
            arr[i] = arr[j];
        }
    }
    return i+1;
}