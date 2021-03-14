// Problem
// There are N houses for sale. The i-th house costs Ai dollars to buy. You have a budget of B dollars to spend.
// What is the maximum number of houses you can buy?
// ---------------
// Input
// The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a single line containing the two integers N and B. The second line contains N integers. The i-th integer is Ai, the cost of the i-th house.
// ---------------
// Output
// For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum number of houses you can buy.
// ---------------

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T, N, B, temp;
    vector<int> cost;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int count = 0;
        cost.clear();
        cin >> N >> B;
        for (int j = 0; j < N; j++)
        {
            cin >> temp;
            cost.push_back(temp);
        }
        sort(cost.begin(), cost.end());
        for (int k = 0; k < cost.size(); k++)
        {
            if (cost[k] <= B)
            {
                ++count;
                B -= cost[k];
            }
            else
                break;
        }
        cout << "Case #" << i + 1 << ": " << count << "\n";
    }
    return 0;
}