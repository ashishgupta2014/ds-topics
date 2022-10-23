class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:

            # collision
            while stack and a < 0 and stack[-1] > 0:

                dif = a + stack[-1]

                # a is stronger
                if dif < 0:
                    stack.pop()

                # stack[-1] is stronger
                elif dif > 0:
                    break

                # equal
                else:
                    stack.pop()
                    break

            # no collision
            else:
                stack.append(a)

        return stack


solve = Solution()
# asteroids = [5, 5, 2, -5, 10, 2, -5]
# asteroids = [5, 10, -5]
# asteroids = [8, -8]
# asteroids = [10, 2, -5]
# asteroids = [-5, -5, 2, 5, 10, 2, 5]
# asteroids = [-5, -5, 2, 5, 0, -2, -5]
asteroids = [-2, -2, 1, -2]
print(solve.asteroidCollision(asteroids))
