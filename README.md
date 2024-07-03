# **Fisheye Image Correction**

This project aims to correct fisheye distortion in images using two distinct methods: the Midpoint Circle Algorithm and the Hemi-Cylinder Unwrapping Algorithm. These methods address the radial distortion caused by fisheye lenses, which are frequently used to capture wide field-of-view images.

**Note**: If there is an error while opening the PDF report on GitHub then paste the URL of the [PDF](https://github.com/ankitk75/Fisheye-Correction/blob/main/CV_Project_Report.pdf) into [http://nbviewer.jupyter.org/](http://nbviewer.jupyter.org/).

Table of Contents
-----------------

*   [Project Overview](#project-overview)
*   [Methodologies](#methodologies)
    *   [Midpoint Circle Algorithm](#midpoint-circle-algorithm)
    *   [Hemi-Cylinder Unwrapping Algorithm](#hemi-cylinder-unwrapping-algorithm)
*   [Installation](#installation)
*   [Usage](#usage)
*   [Features](#features)
*   [Results](#results)
*   [Future Work](#future-work)

Project Overview
----------------

Fisheye lenses capture a wide field of view, resulting in significant radial distortion where straight lines appear curved. This project employs two correction techniques: the Midpoint Circle Algorithm, which is simple and suitable for real-time applications, and the Hemi-Cylinder Unwrapping Algorithm, which provides more accurate corrections by using a hemi-cylindrical projection.

Methodologies
-------------

## Midpoint Circle Algorithm

The Midpoint Circle Algorithm (MCA) is a technique traditionally used in computer graphics for circle rasterization. For fisheye image correction, MCA involves the following steps:

1.  **Identify the Distorted Region**: The distortion center is typically the image center.
2.  **Circle Fitting**: Fit a circle to the edge points of the fisheye pattern using a least squares method.
3.  **Calculate Circle Parameters**: Determine the circle's center coordinates (a, b) and radius r.
4.  **Remap Pixels**: Map distorted radial coordinates to undistorted ones, interpolating pixel values where necessary.
5.  **Output the Corrected Image**: Generate the undistorted image.

This method offers a straightforward correction process ideal for embedded systems.


## Hemi-Cylinder Unwrapping Algorithm


The Hemi-Cylinder Unwrapping Algorithm uses an equidistant projection model to correct fisheye distortion. Key steps include:

1.  **Identify Vanishing Points**: Use planar checkerboard configurations to find where 3D parallel lines converge in the distorted image.
2.  **Determine Distortion Epicenter**: Find the intersection of fitted circles to establish the epicenter.
3.  **Establish Projection Mapping**: Apply the equidistant projection model to map points between the fisheye and hemi-cylindrical planes.
4.  **Map Unwrapped Plane**: Align the unwrapped image plane with the hemi-cylindrical plane.
5.  **Construct Lookup Table**: Facilitate the mapping process with a lookup table.

This method maintains horizontal field of view and is useful for panoramic surveillance.

Installation
------------

1.  Clone the repository:
    ```bash
    git clone https://github.com/ankitk75/Fisheye-Correction.git
    cd Fisheye-Correction
    ```

Usage
-----

To use the fisheye correction scripts, follow these steps:

1.  Place your fisheye distorted image in the `Images` folder.
2.  Run the desired correction script:
    ```bash
    python midpoint_circle_correction.py
    ```
    or
    ```bash
    python hemi_cylinder_unwrapping.py
    ```
3.  The corrected image will be saved in the `Images` folder.

Features
--------

*   **Midpoint Circle Algorithm**: Fast and suitable for real-time applications.
*   **Hemi-Cylinder Unwrapping Algorithm**: Accurate and preserves image content.

Results
-------

Below are examples of fisheye image correction:

## Input Image:

<div style="display: flex;">
  <img src="https://github.com/ankitk75/Fisheye-Correction/blob/main/Images/fe1.jpg" width="59%" />
  <img src="https://github.com/ankitk75/Fisheye-Correction/blob/main/Images/fe2.jpg" width="40%" />
</div>

## Corrected Image using Midpoint Circle Algorithm:

<div style="display: flex;">
  <img src="https://github.com/ankitk75/Fisheye-Correction/blob/main/Images/fe1_output_midpoint.jpg" width="59%" />
  <img src="https://github.com/ankitk75/Fisheye-Correction/blob/main/Images/fe2_output_midpoint.jpg" width="40%" />
</div>

## Corrected Image using Hemi-Cylinder Unwrapping Algorithm:

<div style="display: flex;">
  <img src="https://github.com/ankitk75/Fisheye-Correction/blob/main/Images/fe1_output_hemi_cylinder.jpg" width="59%" />
  <img src="https://github.com/ankitk75/Fisheye-Correction/blob/main/Images/fe2_output_hemi_cylinder.jpg" width="40%" />
</div>


Future Work
-----------

*   **Algorithm Optimization**: Enhance performance and accuracy.
*   **Computational Efficiency**: Reduce processing time for high-resolution images.
*   **Adaptation to Different Camera Models**: Develop a universal algorithm for various camera models.
