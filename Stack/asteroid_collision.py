def asteroidCollision(asteroids):
    stack = []
    for c in asteroids:

        while stack and c * stack[-1] < 0:
            value = stack.pop()
            if abs(c) == abs(value):
                continue
            else:
                maxi = c if abs(c) > abs(value) else value
                c = (maxi)
        else:
            stack.append(c)

    return stack

asteroids = [5,10,-5]
print(asteroidCollision(asteroids))
asteroids = [8,-8]
print(asteroidCollision(asteroids))
asteroids = [10,2,-5]
print(asteroidCollision(asteroids))