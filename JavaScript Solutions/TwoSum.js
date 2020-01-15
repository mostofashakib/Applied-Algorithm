/*
LeetCode Problem 1. Two Sum
Link: https://leetcode.com/problems/two-sum/
Written by: Mostofa Adib Shakib
Language: JavaScript
*/


var twoSum = function(nums, target) {
    let FirstPointer = 0;
    let LastPointer = nums.length - 1;
    let result = new Array(1);
    let answer = new Array(1);
    let original = nums.slice();
    let flag = false;
    
    function swap(items, leftIndex, rightIndex){
    var temp = items[leftIndex];
    items[leftIndex] = items[rightIndex];
    items[rightIndex] = temp;
    }
    
    function partition(items, left, right) {
        var pivot   = items[Math.floor((right + left) / 2)], //middle element
            i       = left, //left pointer
            j       = right; //right pointer
        while (i <= j) {
            while (items[i] < pivot) {
                i++;
            }
            while (items[j] > pivot) {
                j--;
            }
            if (i <= j) {
                swap(items, i, j); //sawpping two elements
                i++;
                j--;
            }
        }
        return i;
    }

    function quickSort(items, left, right) {
        var index;
        if (items.length > 1) {
            index = partition(items, left, right); //index returned from partition
            if (left < index - 1) { //more elements on the left side of the pivot
                quickSort(items, left, index - 1);
            }
            if (index < right) { //more elements on the right side of the pivot
                quickSort(items, index, right);
            }
        }
        return items;
    }
    
    nums = quickSort(nums, FirstPointer, LastPointer);
    
    while (FirstPointer < LastPointer){
        if(nums[FirstPointer] + nums[LastPointer] == target){
            result[0] = nums[FirstPointer];
            result[1] = nums[LastPointer];
            break;
        }
        else if(nums[FirstPointer] + nums[LastPointer] > target){
            LastPointer -= 1;
        }
        else{
            FirstPointer += 1;
        }
    }
    
    for( var i = 0; i < original.length; i++){
        if(original[i] == result[0] && flag == false){
            answer[0] = i;
            flag = true;
        }
        else if (original[i] == result[1]){
            answer[1] = i;
        }
    }
    return answer;
};