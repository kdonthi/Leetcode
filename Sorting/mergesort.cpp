#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
	void printVec(vector<int> a) {
		for (int i: a) {
			cout << i << " ";
		}
		cout << endl;
	}
	vector<int> sort_vec(vector<int> a) {
		int sizea = a.size();
		if (sizea != 1) {
			vector<int> b = sort_vec(vector<int>(a.begin(), a.begin() + sizea/2));
			vector<int> c = sort_vec(vector<int>(a.begin() + sizea/2, a.end()));
			vector<int> d;
			int bcounter = 0;
			int ccounter = 0;
			int bsize = b.size();
			int csize = c.size();
			while (bcounter < bsize || ccounter < csize) {
				if (bsize - bcounter && csize - ccounter) {
					d.push_back(b[bcounter] < c[ccounter] ? b[bcounter++] : c[ccounter++]);
				}
				else if (bsize - bcounter) {
					d.push_back(b[bcounter++]);
				}
				else {
					d.push_back(c[ccounter++]);
				}
			}
			return (d);
		}
		else {
			return (a);
		}
	}
};
int main() {
	vector<int> a = {4,3,2,1};
	Solution sol;
	sol.printVec(a);
	sol.printVec(vector<int>(a.begin(), a.begin() + 1));
	sol.printVec(vector<int>(a.begin() + 1, a.end()));
	sol.printVec(sol.sort_vec(a));
}
