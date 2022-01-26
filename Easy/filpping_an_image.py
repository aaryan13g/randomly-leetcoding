/* https://leetcode.com/problems/flipping-an-image/ */

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            image[i] = [abs(pixel - 1) for pixel in image[i]]
        return image
