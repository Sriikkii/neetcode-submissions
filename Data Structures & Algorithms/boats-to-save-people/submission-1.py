class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        left = 0 
        n = len(people)
        right = n-1
        boats = 0

        while left<=right:
            if left <= right and people[left] == limit:
                boats += 1
                left+=1
            elif left <= right and people[right] == limit:
                boats+=1
                right -= 1
            else:
                calculated = people[left]+people[right]
                if calculated < limit:
                    boats+=1
                    right-=1
                    left +=1
                elif calculated > limit:
                    boats += 1
                    right -= 1
                elif calculated == limit:
                    boats += 1
                    left += 1
                    right -= 1

        return boats

            


