import random
import scipy.integrate as spi


def f(x):
    return x**2


def monte_carlo_integration(num_samples, a, b):
    sum_values = 0

    for _ in range(num_samples):
        x = random.uniform(a, b)
        sum_values += f(x)

    average = sum_values / num_samples
    integral_approximation = (b - a) * average

    return integral_approximation


if __name__ == "__main__":
    num_samples = 100000
    lower_limit = 0
    upper_limit = 2

    result = monte_carlo_integration(num_samples, lower_limit, upper_limit)
    print(f"Approximated integral value: {result}")

    result, error = spi.quad(f, lower_limit, upper_limit)
    print(f"Analytical result: {result}")