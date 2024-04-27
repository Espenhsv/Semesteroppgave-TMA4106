# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 10:07:20 2024

@author: essv0404
"""

import math

def appDer(f, x, h):
    return (f(x + h) - f(x)) / h

def samDer(f, x, h_values):
    der = math.exp(x)  # Analytisk derivert av e^x er e^x
    results = []
    for h in h_values:
        approksimert = appDer(f, x, h)
        error = abs(der - approksimert)
        results.append((h, approksimert, error))
    return results

def main():
    x = 1.5
    h_values = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001]  # Liste med forskjellige h-verdier
    results = samDer(math.exp, x, h_values)
    print("h\tApproksimert derivert\tError")
    for h, approksimert, error in results:
        print(f"{h}\t{approksimert}\t{error}")
        
if __name__ == "__main__":
      main()  
    

def sentralDiff(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def sammenlign_sentralDiff(f, x, h_values):
    der = math.exp(x)  # Analytisk derivert av e^x er e^x
    results = []
    for h in h_values:
        approksimert = sentralDiff(f, x, h)
        error = abs(der - approksimert)
        results.append((h, approksimert, error))
    return results

def main():
    x = 1.5
    h_values = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001]  # Liste med forskjellige h-verdier
    results = sammenlign_sentralDiff(math.exp, x, h_values)
    print("h\tApproksimert derivert\tError")
    for h, approksimert, error in results:
        print(f"{h}\t{approksimert}\t{error}")
        
if __name__ == "__main__":
    main()

def femPunktDiff(f, x, h):
    return (f(x - 2*h) - 8*f(x - h) + 8*f(x + h) - f(x + 2*h)) / (12 * h)

def sammenlignFemPunktDiff(f, x, h_values):
    der = math.exp(x)  # Analytisk derivert av e^x er e^x
    results = []
    for h in h_values:
        approksimert = femPunktDiff(f, x, h)
        error = abs(der - approksimert)
        results.append((h, approksimert, error))
    return results

def main():
    x = 1.5
    h_values = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001]  # Liste med forskjellige h-verdier
    results = sammenlignFemPunktDiff(math.exp, x, h_values)
    print("h\tApproksimert derivert\tError")
    for h, approksimert, error in results:
        print(f"{h}\t{approksimert}\t{error}")

if __name__ == "__main__":
    main()
