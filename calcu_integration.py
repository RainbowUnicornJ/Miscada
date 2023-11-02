from scipy.integrate import quad

def integrate_average(f, a, b):
    integral, error = quad(f, a, b)
    average = integral / (b - a)
    return average

