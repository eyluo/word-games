import word_util


class Graph(object):
    def __init__(self, words):
        self.adj_list = dict()
        for parent in words:
            nodes = set()
            for child in words:
                if parent != child and parent[-1] == child[0]:
                    nodes.add(child)
            self.adj_list[parent] = nodes
        return

    def __repr__(self):
        result = ''
        for node in self.adj_list:
            result += f'{node} -> [ '
            for outgoing in self.adj_list[node]:
                result += f'{outgoing} '
            result += ']\n'
        return result.strip()

    def __eq__(self, other):
        if isinstance(other, Graph):
            return self.adj_list == other.adj_list
        return False

    def find_paths(self, sides, max_depth=3, max_results=5):
        letter_set = word_util.sides_to_letter_set(sides)

        def validate_path(path):
            path_letter_set = set()
            for word in path:
                for c in word:
                    path_letter_set.add(c)
            return path_letter_set == letter_set

        def rec_find_path(node, path=[], depth=0):
            if validate_path(path):
                return path
            if depth == max_depth:
                return None

            path.append(node)
            for outgoing in self.adj_list[node]:
                result = rec_find_path(outgoing, path, depth+1)
                if result != None:
                    return result
            path.pop()

            return None

        results = list()
        for node in self.adj_list:
            result = rec_find_path(node, path=[])
            if result != None:
                results.append(result)
                if len(results) == max_results:
                    return results
        return results
