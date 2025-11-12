{\rtf1\ansi\ansicpg1252\cocoartf2865
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import math\
\
def calculate_volume_of_sphere(radius: float) -> float:\
    """Return volume of a sphere with given radius."""\
    if radius < 0:\
        raise ValueError("radius must be non-negative")\
    return (4.0/3.0) * math.pi * (radius ** 3)\
\
if __name__ == "__main__":\
    # quick check\
    print(round(calculate_volume_of_sphere(3), 4))  # 113.0973\
}