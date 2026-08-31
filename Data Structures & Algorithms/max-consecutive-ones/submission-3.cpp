class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {

        int consecutive = 0;
        int maximum = 0;

        for (int num : nums) {
            
            if (num == 1) {
                consecutive++;
                if (consecutive > maximum) {
                    maximum = consecutive;
                }
            } else
            {
                consecutive = 0;
            }

        }

        return maximum;
        
    }
};