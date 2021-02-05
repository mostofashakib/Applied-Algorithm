#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <array>
#include <limits>
#include <bits/stdc++.h>
#include <numeric>

using namespace std; 

int largestPossibleEvenSumOfKElementsInAnArray(vector<int> &nums, int k) {
  int largestEvenSum = 0;
  vector<int> onlyEvens;

  for (int i = 0; i < nums.size(); i++) {
    if (nums[i] % 2 == 0) {
      onlyEvens.push_back(nums[i]);
    }
  }

  sort(onlyEvens.begin(), onlyEvens.end());

  int index = onlyEvens.size() - 1;

  while (k > 0) {
    largestEvenSum += onlyEvens[index];
    index--;
    k--;
  }

  return largestEvenSum;
}

int main() {
  vector<int> nums {4, 9, 8, 2, 6};

  cout << "Answer: " << largestPossibleEvenSumOfKElementsInAnArray(nums, 3) << endl;

  return 0;
}