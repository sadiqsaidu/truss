# Truss

A small, dependency-free Python library for 2D geometry.

## Features

- `Point`: coordinates, displacement, and distance between points.
- `Size`: width and height with tolerance-aware equality.
- `Vector`: addition, subtraction, scaling, dot and cross products, normalization, projection, angles, and rotation.
- `Line`: parallel and perpendicular lines, intersections, and parallel or perpendicular lines through a point.
- `Segment`: length, midpoint, points along a segment, closest points and distances, intersections, and bisectors.
- `Circle`: area, circumference, point containment, and polygon approximation.
- `Polygon`: centroid, sides, and point containment.
- `Rect`: bounds, area, perimeter, point containment, intersections, and polygon conversion.
- Constructors for circles, polygons, rectangles containing points, and rectangles centered on a point.

Floating point comparisons use a small tolerance, so equality checks are not thrown off by rounding errors.

## Running tests

Run the unit tests from the repository root:

```bash
python3 -m unittest discover -s geom2d -p '*_test.py'
```
