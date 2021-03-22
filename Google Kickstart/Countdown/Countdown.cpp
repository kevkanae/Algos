//Problem
//https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2#problem

#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T, N, K, temp;
    vector<int> arr;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int count = 0;
        arr.clear();
        cin >> N >> K;
        int a = K;
        for (int j = 0; j < N; j++)
        {
            cin >> temp;
            arr.push_back(temp);
        }
        for (int k = 0; k < arr.size(); k++)
        {
            if (arr[k] == a)
            {
                a--;
                if (a == 0)
                {
                    a = K;
                    count++;
                }
            }
        }
        cout << "Case #" << i + 1 << ": " << count << "\n";
    }

    return 0;
}