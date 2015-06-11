class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        row = [A,C,E,G]
        col = [B,D,F,H]
        row.sort()
        col.sort()
        small = abs((row[2]-row[1])*(col[2]-col[1]))
        large = (C-A)*(D-B) + (G-E)*(H-F)
        # Judge if these two rectangle intersect or not
        # If intersect, reduce the intersection area
        if E>=C or G<=A or B>=H or D<=F:
            return large
        return large -small
