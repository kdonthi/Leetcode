/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        vector<TreeNode*> vect = {root};
        vector<TreeNode*> addvect;
        int depth = 1;
        bool addToDepth;
        int i; //SC 3
        if (!root) {
            return (0);
        }
        while (vect.size() > 0) {
            addToDepth = false; //TC 2 * number of nodes
            for (i = 0; i < vect.size(); i++) {
                if (vect[i]->left) {
                    //printf("%i\n", vect[i]->left->val);
                    addvect.push_back(vect[i]->left);
                }
                if (vect[i]->right) {
                    //printf("%i\n", (vect[i]->right->val));
                    addvect.push_back(vect[i]->right);
                }
                if (vect[i]->right || vect[i]->left)
                    addToDepth = true;
            }
            if (addToDepth)
                depth++;

            vect.clear();
            for (TreeNode* i: addvect) {
                //printf("%i\n", i->val);
                vect.push_back(i); //TC number of nodes
            }
            addvect.clear(); //TC number of nodes (each clear is TC of number of values)
            //printf("Vector Size: %i\n", vect.size());
        }
        return (depth);
    }
 }; //TC is linear and SC is greatest amount of values per a given level
