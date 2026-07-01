class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        left = 0 
        n = len(people)
        right = n-1
        boats = 0

        while left <= right:
            if left<= right and people[left] == limit:
                boats+=1
                left+=1
            elif left<= right and people[right] == limit:
                boats+=1
                right-=1
            else:
                calc = people[left]+people[right]
                if calc < limit:
                    left += 1
                    right -=1
                    boats +=1
                elif calc > limit:
                    right -= 1
                    boats += 1
                elif calc == limit:
                    boats += 1
                    right -=1
                    left += 1
        return boats

            


