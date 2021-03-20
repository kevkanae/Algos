//Problem
//https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff43/00000000003380d2#problem

#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T, N, countdown, temp;
    vector<int> arr;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        int count = 0;

        arr.clear();
        cin >> N >> countdown;
        int a = countdown;
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
                    a = countdown;
                    count++;
                }
            }
        }
        cout << "Case #" << i + 1 << ": " << count << "\n";
    }

    return 0;
}
