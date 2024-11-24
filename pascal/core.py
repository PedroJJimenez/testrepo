def generate_pascals_triangle(n):
    """
    Generate the first n rows of Pascal's Triangle.

    Pascal's Triangle is a triangular array of the binomial coefficients. 
    Each number is the sum of the two directly above it.

    :param n: Number of rows to generate
    :type n: int
    :return: A list of lists representing the first n rows of Pascal's Triangle
    :rtype: list
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

def binomial_expansion(x, y, n):
    """
    Compute the n-th power of the binomial (x + y) using Pascal's Triangle.

    :param x: The first term in the binomial
    :type x: int or float
    :param y: The second term in the binomial
    :type y: int or float
    :param n: The power to which the binomial is raised
    :type n: int
    :return: The expanded form of the binomial (x + y)^n
    :rtype: float
    """
    coefficients = generate_pascals_triangle(n + 1)[-1]
    result = sum(coefficients[i] * (x ** (n - i)) * (y ** i) for i in range(n + 1))
    return result

# # Example usage:
# binomial_expansion(2, 3, 3)

# # Example usage:
# print(generate_pascals_triangle(5))