
public class diameterOfBinaryTree {
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

    static int maxDiameter = 0;

    public static int diameterOfBinaryTree(TreeNode root) {
        calculateHeight(root);
        return maxDiameter;
    }
    
    public static int calculateHeight(TreeNode root) {
        if (root == null) {
            return 0;
        } else {
            int leftHeight = calculateHeight(root.left);
            int rightHeight = calculateHeight(root.right);
            maxDiameter = Math.max(maxDiameter, leftHeight + rightHeight);

            return 1 + Math.max(leftHeight, rightHeight);
        }
    }
}
