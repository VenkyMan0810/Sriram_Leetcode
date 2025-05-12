class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = []
        # for i in strs:
        #     add = False
        #     for g in res:
        #         if sorted(i) == sorted(g[0]):
        #             g.append(i)
        #             add = True
        #             break
        #     if not add:
        #         res.append([i])
        # return res

        g={}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in g:
                g[key] = []
            g[key].append(i)
        
        return list(g.values())