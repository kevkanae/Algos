#include <bits/stdc++.h>
using namespace std;

void fib(int n)
{
    int count = 2;
    int f1 = 0, f2 = 1, f3;
    vector<int> list = {f1, f2};
    while (count < n)
    {
        f3 = f1 + f2;
        list.push_back(f3);
        f1 = f2;
        f2 = f3;
        count++;
    }
    for (int i = 0; i < list.size(); i++)
    {
        cout << list[i] << ' ';
    }
}

int main()
{
    int n;
    int check = 1;
    while (check == 1)
    {
        cout << "Enter the Sequence Length: ";
        cin >> n;
        if (n == 0)
        {
            cout << "Enter Non Zero Integer Value :)\n";
        }
        else
        {
            fib(n);
            check = 0;
        }
    }

    return 0;
}
