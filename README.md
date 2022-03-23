# Multi-scale Template Matching using Python and OpenCV

Let’s first understand why the standard approach to template matching using `cv2.matchTemplate` is not very robust.
However, when we try to apply template matching using the `cv2.matchTemplate` function, 
we are left with a false match — this is because the size of the logo image is substantially smaller than the logo on the cover.

_So what do we do now?_

## The cv2.matchTemplate Trick

Just because the dimensions of your template do not match the dimensions of the region in the image you want to match, 
does not mean that you cannot apply template matching.

In this case, all you need to do is apply a little trick:

Loop over the input image at multiple scales (i.e. make the input image progressively smaller and smaller).
Apply template matching using `cv2.matchTemplate` and keep track of the match with the largest correlation coefficient (along with the x, y-coordinates of the region with the largest correlation coefficient).
After looping over all scales, take the region with the largest correlation coefficient and use that as your “matched” region.
As I said, this trick is dead simple — but in certain situations this approach can save you from writing a lot of extra code and dealing with more fancy techniques to matching objects in images.

_By definition template matching is translation invariant. 
The extension we are proposing now can help make it more robust to changes in scaling (i.e. size). 
But template matching is not ideal if you are trying to match rotated objects or objects that exhibit non-affine transformations. 
If you are concerned with these types of transformations you are better of jumping right to keypoint matching._

## Installation

```shell
pip install -r requirements.txt
```

## Usage 
```shell
python match.py -i image.jpg -o crop.jpg -t logo.png
```

## Help
```shell
python match.py --help
```
