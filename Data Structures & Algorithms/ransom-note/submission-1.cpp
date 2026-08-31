#include <array>
#include <string>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        array<int, 26> count{};
        
        // Count available letters in magazine
        for (char c : magazine) {
            count[c - 'a']++;
        }

        // Use letters for ransomNote
        for (char c : ransomNote) {
            count[c - 'a']--;

            if (count[c - 'a'] < 0) {
                return false;
            }
        }

        return true;
    
    }
};