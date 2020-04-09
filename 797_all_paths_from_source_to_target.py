class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # choice - to continue down path
        # constraint - must go to one of nodes as directed
        # goal - reach None or node N-1
        # acyclic means no backtracking cause no cycles
        def _traverse_path(node: int, all_paths=None, current_path=None):
            if not current_path:
                all_paths = []
                current_path = []
            current_path.append(node)
            if node == len(graph) - 1:
            # if destination reached, then add to answer
                all_paths.append(current_path.copy())
            for next_node in graph[node]:
            # dfs because function called recursively before "sibling" node called
                _traverse_path(next_node, all_paths, current_path)
            # to adjust current path back to what it previously was
            current_path.pop()
            if node == 0:
                return all_paths
            
        return _traverse_path(0)
