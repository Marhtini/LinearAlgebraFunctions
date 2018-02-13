#!/usr/bin/env python

# Basic Functions for working with Vectors in Linear Algebra
# John Martinez (@marhtini) - February 2018

import sys
import math


def vector_add(av1, av2):

    vector_result = []
    vector_result.append((float(av1[0]) + float(av2[0])))
    vector_result.append((float(av1[1]) + float(av2[1])))
    print("Vector Addition: " + str(vector_result))


def vector_subtract(sv1, sv2):

    vector_result = []
    vector_result.append((float(sv1[0]) - float(sv2[0])))
    vector_result.append((float(sv1[1]) - float(sv2[1])))
    print("Vector Subtract: " + str(vector_result))


def vector_multiply(scalar, mvector):

    # Scalar Multiplication

    vector_result = []
    for i in mvector:
        vector_result.append(eval(scalar) * float(i))
    print("Scalar Multiplication: " + str(vector_result))
    return vector_result


def vector_magnitude(mv1):

    vector_result = []
    for i in mv1:
        i_float = float(i)
        squared_i = i_float**2  # Exponent in Python is ** not ^
        vector_result.append(squared_i)
    magsum = math.sqrt(sum(vector_result))
    print("Magnitude: " + str(magsum))
    return magsum


def vector_normalize(nv1):

    mag = vector_magnitude(nv1)
    nmultiply = (1.0/mag)
    vector_multiply(str(nmultiply), nv1)  # STR because of Eval statement in Multiply


def vector_dotproduct(dpv1,dpv2):

    dot_product_list = []
    n = 0
    for i in dpv1:
        dot_product_list.append(float(i) * float(dpv2[n]))
        n += 1

    dot_product = sum(dot_product_list)
    print("Dot Product: " + str(dot_product))
    return dot_product


def vector_innerproduct(ipv1, ipv2):

    dot_product = vector_dotproduct(ipv1, ipv2)
    magnitude_ipv1 = vector_magnitude(ipv1)
    magnitude_ipv2 = vector_magnitude(ipv2)

    if magnitude_ipv1 != 0 and magnitude_ipv2 != 0:
        multiply_arccos_by_this = dot_product/(magnitude_ipv1 * magnitude_ipv2)
        inner_product = math.acos(multiply_arccos_by_this)
    elif magnitude_ipv1 == 0 or magnitude_ipv2 == 0:
        inner_product = 0
    else:
        print("Error in vector_innerproduct function.")

    radian_to_degree_conversion = float(57.2958 * inner_product)

    print("Inner Product in Radians: " + str(inner_product))
    print("Inner Product in Degrees: " + str(radian_to_degree_conversion))

    return radian_to_degree_conversion


def vector_orthogonal(ov1, ov2):

    # toleranceInDotProduct = 1*10**-10  # 1e-10
    orthDotProduct = vector_dotproduct(ov1, ov2)
    orthInnerProduct = vector_innerproduct(ov1, ov2)

    # >= 90 <= 91 handles floats that are almost exactly 90 degree angles
    if orthDotProduct == 0 or (orthInnerProduct >= 90 and orthInnerProduct <= 91):
        print(str(ov1) + " and " + str(ov2) + " are Orthogonal!")
    elif orthDotProduct != 0 or orthInnerProduct != 90:
        print(str(ov1) + " and " + str(ov2) + " are NOT Orthogonal!")
    else:
        print("Unknown Error in vector_orthogonal function.")


def vector_parallel(pv1, pv2):

    n = 0
    for i in pv2:

        if (float(i)/float(pv1[n])).is_integer() == True: # A bit easier than Modulo with Floats
            n += 1
        elif (float(i)/float(pv1[n])).is_integer() != True:
            print(str(pv1) + " and " + str(pv2) + " are NOT Parallel.")
            return 0
        else:
            print("Error in vector_parallel function.")

    print(str(pv1) + " and " + str(pv2) + " are Parallel!")


def main():

    vector_action = sys.argv[1]

    if vector_action == 'multiply':
        scalar = sys.argv[2]
        vector = sys.argv[3].split(",")
        vector_multiply(scalar, vector)

    elif vector_action == "magnitude":
        vector1 = sys.argv[2].split(",")
        vector_magnitude(vector1)

    elif vector_action == "normalize":
        vector1 = sys.argv[2].split(",")
        vector_normalize(vector1)

    elif vector_action == "dotproduct":
        vector1 = sys.argv[2].split(",")
        vector2 = sys.argv[3].split(",")
        vector_dotproduct(vector1, vector2)

    elif vector_action == "innerproduct":
        vector1 = sys.argv[2].split(",")
        vector2 = sys.argv[3].split(",")
        vector_innerproduct(vector1, vector2)

    elif vector_action == "orthogonal":
        vector1 = sys.argv[2].split(",")
        vector2 = sys.argv[3].split(",")
        vector_orthogonal(vector1, vector2)

    elif vector_action == "parallel":
        vector1 = sys.argv[2].split(",")
        vector2 = sys.argv[3].split(",")
        vector_parallel(vector1, vector2)

    else:
        vector1 = sys.argv[2].split(",")
        vector2 = sys.argv[3].split(",")

        if vector_action == 'add':
            vector_add(vector1, vector2)
        elif vector_action == 'subtract':
            vector_subtract(vector1, vector2)
        else:
            print('Unknown Error')


if __name__ == "__main__":
