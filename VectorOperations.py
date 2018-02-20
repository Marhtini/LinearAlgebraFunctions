#!/usr/bin/env python

# Basic Functions for working with Vectors in Linear Algebra
# John Martinez (@marhtini) - February 2018

# TODO: Needs some refactoring for efficiency/input and help

import sys
import math


def vector_add(av1, av2):

    vector_result = []
    count = 0
    while count < len(av1):
        vector_result.append(float(av1[count]) - float(av2[count]))
        count += 1

    print("Vector Addition: " + str(vector_result))
    return vector_result


def vector_subtract(sv1, sv2):

    vector_result = []
    count = 0
    while count < len(sv1):
        vector_result.append(float(sv1[count]) - float(sv2[count]))
        count += 1

    print("Vector Subtraction: " + str(vector_result))
    return vector_result


def vector_multiply(scalar, mvector):

    # Scalar Multiplication

    vector_result = []
    for i in mvector:
        try:
            vector_result.append(eval(scalar) * float(i))
        except:
            vector_result.append(scalar * float(i))
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
    normalized = vector_multiply(str(nmultiply), nv1)  # STR because of Eval statement in Multiply
    print("Normalization of " + str(nv1) + ": " + str(normalized))
    return normalized


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
            return False
        else:
            print("Error in vector_parallel function.")

    print(str(pv1) + " and " + str(pv2) + " are Parallel!")
    return True


def vector_projection(vVect, bVect):

    # angleAssumption <= 90  # Degrees
    parallelLength = vector_multiply(vector_dotproduct(vVect, vector_normalize(bVect)), vector_normalize(bVect))
    print("Parallel Length: " + str(parallelLength))
    return parallelLength


def vector_perpendicular(cVect, xVect):

    aVect = vector_projection(cVect, xVect)
    print("aVECT is: " + str(aVect))
    print("xVECT (origin vector) is: " + str(xVect))

    bVect = vector_subtract(cVect, aVect)
    print("bVECT (Parallel Result) is: " + str(bVect))
    return bVect


def vector_crossproducts(vVect, wVect):

    # x means CROSS in crossproduct

    if len(vVect) != 3:
        print("Error: First Vector is not three dimensional.")
        return 0
    elif len(wVect) != 3:
        print("Error: Second Vector is not three dimensional.")
        return 0

    if vector_innerproduct(vVect, wVect) == 0 \
            or vector_innerproduct(vVect, wVect) == 180\
            or vVect == "0,0"\
            or wVect == "0.0"\
            or vector_parallel(vVect, wVect) is True:
        crossProduct = [0,0,0]
        print("Cross Product is :" + str(crossProduct))
        return crossProduct # 0

    else:

        crossProduct = []

        x = 0
        y = 1
        z = 2

        row1_1 = float(vVect[y]) * float(wVect[z])
        row1_2 = float(wVect[y]) * float(vVect[z])
        row2_1 = float(vVect[x]) * float(wVect[z])
        row2_2 = float(wVect[x]) * float(vVect[z])
        row3_1 = float(vVect[x]) * float(wVect[y])
        row3_2 = float(wVect[x]) * float(vVect[y])

        finalRow1 = row1_1 - row1_2
        finalRow2 = (row2_1 - row2_2) * -1 # Must make negative!
        finalRow3 = row3_1 - row3_2


        crossProduct.append(finalRow1)
        crossProduct.append(finalRow2)
        crossProduct.append(finalRow3)

        print("The Cross Product is: " + str(crossProduct))
        vector_area_parallelogram(crossProduct)


def vector_area_parallelogram(crossproductvector):

    x = crossproductvector[0]
    y = crossproductvector[1]
    z = crossproductvector[2]

    parallelogram_vw = math.sqrt(x**2 + y**2 + z**2)

    print("Parallelogram Spanned by V & W: " + str(parallelogram_vw))

    vector_area_triangle(parallelogram_vw) # Get Triangle Spanning V & W

    return parallelogram_vw


def vector_area_triangle(parallelogram):

    triangle_vw = parallelogram / 2

    print("Triangle Spanned by V & W: " + str(triangle_vw))
    return triangle_vw


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

    elif vector_action == "projection":
        vector1 = sys.argv[2].split(",")
        vector2 = sys.argv[3].split(",")
        vector_projection(vector1, vector2)

    elif vector_action == "perpendicular":
        vector1 = sys.argv[2].split(",")
        vector2 = sys.argv[3].split(",")
        vector_perpendicular(vector1, vector2)

    elif vector_action == "crossproduct":
        vector1 = sys.argv[2].split(",")
        vector2 = sys.argv[3].split(",")
        vector_crossproducts(vector1, vector2)

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
    main()
