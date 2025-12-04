class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        i = 0
        while i < len(directions) and directions[i] == 'L':
            i += 1
        
        j = len(directions) - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1
        
        collisions = 0
        for k in range(i, j + 1):
            if directions[k] != 'S':
                collisions += 1
        
        return collisions