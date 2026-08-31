class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {

        int size = nums.size();
        int consecutive = 0;
        int maximum = 0;

        for (int i = 0; i < size; i++) {
        
            if (nums[i] != 0) {
                consecutive++;
                maximum = max(maximum, consecutive);
            }
            else {
                consecutive = 0;
            }
        }

        return maximum;
        
    }
};