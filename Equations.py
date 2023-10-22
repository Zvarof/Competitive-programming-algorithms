''' Case : ax + by = c'''

def find_any_solution(a, b, c):
    def gcd(a, b):
        x0, x1, y0, y1 = 1, 0, 0, 1         # Initialize coefficients
        while b:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return a, x0, y0

    g, x0, y0 = gcd(abs(a), abs(b))

    if c % g:
        return False

    x0 *= c // g
    y0 *= c // g

    if a < 0:
        x0 = -x0
    if b < 0:
        y0 = -y0

    return x0, y0