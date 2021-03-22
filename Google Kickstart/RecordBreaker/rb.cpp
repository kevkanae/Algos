// Problem
// https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000387171

#include <bits/stdc++.h>

int main()
{
    int T, N, V, temp;
    std::cin >> T;
    for (int i = 0; i < T; i++)
    {
        int count = 0;
        int prev = 0;
        std::cin >> N;
        int arr[N];
        for (int j = 0; j < N; j++)
        {
            std::cin >> arr[j];
        }
        if (arr[0] > arr[1])
        {
            count++;
        }
        for (int k = 1; k < N; k++)
        {
            if (k != N - 1)
            {
                if (arr[k] > arr[k - 1] && arr[k] > arr[k + 1] && arr[k] > prev)
                {
                    count++;
                    prev = arr[k];
                }
            }
            else
            {
                if (arr[k] > arr[k - 1] && arr[k] > prev)
                {
                    count++;
                }
            }
        }
        std::cout << "Case #" << i + 1 << ": " << count << "\n";
    }

    return 0;
}