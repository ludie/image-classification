# Image Classification
![https://www.dreamstime.com/illustration/classify.html](https://thumbs.dreamstime.com/b/big-data-data-science-communication-concept-large-flow-filter-gear-to-separate-analyize-classify-information-78132890.jpg)
#### From: https://www.dreamstime.com/ 
Image classification is a supervised learning problem: define a set of target classes (objects to identify in images), and train a model to recognize them using labeled example photos.

## Background
At Shopee, we always strive to ensure the correct listing and categorization of products. For example due to the recent pandemic situation, face masks become extremely popular for both buyers and sellers, everyday we need to categorize and update a huge number of masks items. A robust product detection system will significantly improve the listing and categorization efficiency. But in the industrial field the data is always much more complicated and there exists mis-labelled images, complex background images and low resolution images, etc. The noisy and imbalanced data and multiple categories make this problem still challenging in the modern computer vision field.
## Datasets
In Shopee Product Detection Dataset, there are more than 100k images directly from E-commercial industry field. You will be able to explore the real-world images which is noisy and long-tailed, and let your model predict the correct categories for the images. There contains 42 most popular categories product at Shopee.

### File descriptions
- train.csv: training dataset.
- test.csv: test dataset.

### Data fields
- filename: image file name(str).
- category: image category(str).

### Train.csv
| filename | category  | 
| :---   | :-- |
| 45e2d0c97f7bdf8cbf3594beb6fdcda0.jpg | 3 |
| f74d1a5fc2498bbbfa045c74e3cc333e.jpg | 3 |
| f6c172096818c5fab10ecae722840798.jpg | 3 |
| 251ffd610399ac00fea7709c642676ee.jpg | 3 |
| 73c7328b8eda399199fdedec6e4badaf.jpg | 3 |
| 64235682a0457eda1bfa8afe88222480.jpg | 3 |
| ... | ... |
