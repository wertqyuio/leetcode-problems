from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # find minimum
        # ideas are to go through k lists every time
        # second idea is to complete binary search insertion every time
        start = ListNode(0)
        start.next = None
    
        merge_order = PriorityQueue()
        merge_list = lists
        for idx in range(len(lists)):
            current = lists[idx]
            if current:
                merge_order.put((current.val,idx))
        
        if merge_order.qsize():
            node_position = merge_order.get()
            previous_node = merge_list[node_position[1]]
            start.next = previous_node
            next_node = merge_list[node_position[1]].next
            merge_list[node_position[1]] = next_node
            if next_node:
                merge_order.put((next_node.val, node_position[1]))
        
        while merge_order.qsize():
            node_position = merge_order.get()
            current_node = merge_list[node_position[1]]
            previous_node.next = current_node
            next_node = merge_list[node_position[1]].next
            merge_list[node_position[1]] = next_node
            previous_node = current_node
            if next_node:
                merge_order.put((next_node.val,node_position[1]))
            
            
        return start.next
