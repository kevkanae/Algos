// Problem
// https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ffc8/00000000002d82e6

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T, N, H, temp, count = 0;
    vector<int> peaks;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        cin >> N;
        for (int j = 0; j < N; j++)
        {
            cin >> temp;
            peaks.push_back(temp);
        }

        for (int k = 1; k < peaks.size() - 1; k++)
        {
            if (peaks[k] > peaks[k - 1] && peaks[k] > peaks[k + 1])
                count++;
        }
        peaks.clear();
        cout << "Case #" << i + 1 << ": " << count << "\n";
        count = 0;
    }

    return 0;
}