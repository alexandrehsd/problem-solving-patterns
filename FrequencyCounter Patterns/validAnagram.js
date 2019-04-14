/*
    Given two strings, write a function 
    to determine if the second string is an anagram
    of the first. An anagram is a word, phrase, or name
    formed by rearranging the letters of another,
    such as cinema, formed from iceman.
*/

function validAnagram(str1, str2){
    if(str1.length !== str2.length){
        return false;
    }

    var freqCounter1 = {};
    var freqCounter2 = {};

    for(var val of str1){
        freqCounter1[val] = (freqCounter1[val] || 0) + 1;
    }
    for(var val of str2){
        freqCounter2[val] = (freqCounter2[val] || 0) + 1;
    }
    for(var key in freqCounter1){
        if(!(key in freqCounter2)){
            return false;
        }
        if(freqCounter1[key] !== freqCounter2[key]){
            return false;
        }
    }
    return true;
}

console.log(validAnagram('cinema','iceman'))