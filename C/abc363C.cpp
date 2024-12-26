// Python Code:
// import itertools
// 
// N, K = map(int, input().split())
// S = input()
// 
// Seen = set()
// ans = 0
// for pattern in itertools.permutations(list(range(N)), r=N):
//   Str = ""
//   for idx in pattern:
//     Str += S[idx]
//   
//   if Str not in Seen:
//     containFlg = 0
//     for i in range(N - K + 1):
//       cnt = 0
//       for j in range(1, K + 1):
//         if Str[i + j - 1] != Str[i + K - j]:
//           break
//         cnt += 1
//       if cnt == K:
//         containFlg = 1
//         break 
//     if containFlg == 0:
//       ans += 1
//   
//     Seen.add(Str)
// 
// print(ans)

#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    string S;
    cin >> S;

    set<string> Seen;
    int ans = 0;

    // Generate all permutations of N elements
    vector<int> pattern(N);
    for (int i = 0; i < N; ++i) {
        pattern[i] = i;
    }

    do {
        // Create a string from the current permutation
        string Str = "";
        for (int idx : pattern) {
            Str += S[idx];
        }

        if (Seen.find(Str) == Seen.end()) {
            bool containFlg = false;

            // Check for palindromic substrings of length K
            for (int i = 0; i <= N - K; ++i) {
                int cnt = 0;
                for (int j = 1; j <= K; ++j) {
                    if (Str[i + j - 1] != Str[i + K - j]) {
                        break;
                    }
                    cnt++;
                }
                if (cnt == K) {
                    containFlg = true;
                    break;
                }
            }

            if (!containFlg) {
                ans++;
            }

            Seen.insert(Str);
        }

    } while (next_permutation(pattern.begin(), pattern.end()));

    cout << ans << endl;

    return 0;
}
