class Node:
    def __init__(self):
        self.max_len = 1
        self.pref_len = 1
        self.suff_len = 1
        self.pref_char = ''
        self.suff_char = ''
        self.total_len = 1

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [Node() for _ in range(4 * n)]
        
        def push_up(idx: int):
            left = idx * 2
            right = idx * 2 + 1
            
            l_node = tree[left]
            r_node = tree[right]
            curr = tree[idx]
            
            curr.total_len = l_node.total_len + r_node.total_len
            curr.pref_char = l_node.pref_char
            curr.suff_char = r_node.suff_char
            
            curr.pref_len = l_node.pref_len
            if l_node.pref_len == l_node.total_len and l_node.pref_char == r_node.pref_char:
                curr.pref_len += r_node.pref_len
                
            curr.suff_len = r_node.suff_len
            if r_node.suff_len == r_node.total_len and r_node.suff_char == l_node.suff_char:
                curr.suff_len += l_node.suff_len
                
            curr.max_len = max(l_node.max_len, r_node.max_len)
            if l_node.suff_char == r_node.pref_char:
                curr.max_len = max(curr.max_len, l_node.suff_len + r_node.pref_len)

        def build(node_idx: int, l: int, r: int):
            if l == r:
                tree[node_idx].max_len = 1
                tree[node_idx].pref_len = 1
                tree[node_idx].suff_len = 1
                tree[node_idx].pref_char = s[l]
                tree[node_idx].suff_char = s[l]
                tree[node_idx].total_len = 1
                return
            
            mid = (l + r) // 2
            build(node_idx * 2, l, mid)
            build(node_idx * 2 + 1, mid + 1, r)
            push_up(node_idx)

        def update(node_idx: int, l: int, r: int, pos: int, char: str):
            if l == r:
                tree[node_idx].pref_char = char
                tree[node_idx].suff_char = char
                return
            
            mid = (l + r) // 2
            if pos <= mid:
                update(node_idx * 2, l, mid, pos, char)
            else:
                update(node_idx * 2 + 1, mid + 1, r, pos, char)
            push_up(node_idx)

        build(1, 0, n - 1)
        
        ans = []
        for char, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, char)
            ans.append(tree[1].max_len)
            
        return ans