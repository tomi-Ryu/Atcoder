// Original Python Code:
// N = int(input())
// A = input()
// A_pyramid = [""] * (N+1)
// for level in reversed(range(N+1)):
//   if level == N:
//     A_pyramid[level] = A
//   else:
//     for cnt in range(3**level):
//       if A_pyramid[level+1][3*cnt:3*(cnt+1)].count("1") >= 2:
//         A_pyramid[level] += "1"
//       else:
//         A_pyramid[level] += "0"
// def Change_MinCnt(TargetBitStr, level, Kbn):
//   Ret_Cnt = 0
//   if level == N:
//     if A_pyramid[level][Kbn] != TargetBitStr:
//       return 1
//     else:
//       return 0
//   CntOrder_list = []
//   NeedChgCnt = 2
//   for i in range(3*Kbn, 3*(Kbn+1)):
//     if A_pyramid[level+1][i] == TargetBitStr:
//       NeedChgCnt -= 1
//     else:
//       CntOrder_list.append(Change_MinCnt(TargetBitStr, level+1, i))
//   CntOrder_list.sort()
//   for r in range(NeedChgCnt):
//     Ret_Cnt += CntOrder_list[r]
//   return Ret_Cnt
// if A_pyramid[0] == "1":
//   print(Change_MinCnt("0", 0, 0))
// else:
//   print(Change_MinCnt("1", 0, 0))





#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>  // For using pow function
using namespace std;

// Function for computing minimum changes required
int Change_MinCnt(string TargetBitStr, int level, int Kbn, const vector<string>& A_pyramid, int N) {
    int Ret_Cnt = 0;

    if (level == N) {
        if (A_pyramid[level][Kbn] != TargetBitStr[0]) {
            return 1;
        } else {
            return 0;
        }
    }

    vector<int> CntOrder_list;
    int NeedChgCnt = 2;
    for (int i = 3 * Kbn; i < 3 * (Kbn + 1); ++i) {
        if (A_pyramid[level + 1][i] == TargetBitStr[0]) {
            --NeedChgCnt;
        } else {
            CntOrder_list.push_back(Change_MinCnt(TargetBitStr, level + 1, i, A_pyramid, N));
        }
    }

    sort(CntOrder_list.begin(), CntOrder_list.end());

    // 0 or less are not added, skip the loop
    for (int r = 0; r < NeedChgCnt; ++r) {
        Ret_Cnt += CntOrder_list[r];
    }

    return Ret_Cnt;
}

int main() {
    int N;
    string A;
    cin >> N >> A;

    vector<string> A_pyramid(N + 1);
    
    // Generating the pyramid in reverse order
    for (int level = N; level >= 0; --level) {
        if (level == N) {
            A_pyramid[level] = A;
        } else {
            for (int cnt = 0; cnt < pow(3, level); ++cnt) {
                int ones_count = 0;
                for (int i = 3 * cnt; i < 3 * (cnt + 1); ++i) {
                    if (A_pyramid[level + 1][i] == '1') {
                        ++ones_count;
                    }
                }
                if (ones_count >= 2) {
                    A_pyramid[level] += "1";
                } else {
                    A_pyramid[level] += "0";
                }
            }
        }
    }

    if (A_pyramid[0] == "1") {
        cout << Change_MinCnt("0", 0, 0, A_pyramid, N) << endl;
    } else {
        cout << Change_MinCnt("1", 0, 0, A_pyramid, N) << endl;
    }

    return 0;
}
