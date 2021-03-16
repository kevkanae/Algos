// Problem
//https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc7/00000000001d3f56

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