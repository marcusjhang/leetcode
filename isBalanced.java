public class isBalanced {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    
    public boolean isBalanced(TreeNode root) {
        if (root == null) {
            return true;
        } else if ((Math.abs(calculateHeight(root.left) - calculateHeight(root.right)) <= 1) && isBalanced(root.left) && isBalanced(root.right)) {
            return true;
        } else {
            return false;
        }
    }

    public int calculateHeight(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            int leftHeight = calculateHeight(root.left);
            int rightHeight = calculateHeight(root.right);
            return 1 + Math.max(leftHeight, rightHeight);
        }
    }
}
