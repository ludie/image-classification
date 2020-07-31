# Image Classification
![https://www.dreamstime.com/illustration/classify.html](https://thumbs.dreamstime.com/b/big-data-data-science-communication-concept-large-flow-filter-gear-to-separate-analyize-classify-information-78132890.jpg)
#### From: https://www.dreamstime.com/ 
Image classification is a supervised learning problem: define a set of target classes (objects to identify in images), and train a model to recognize them using labeled example photos.

## Background
At Shopee, we always strive to ensure the correct listing and categorization of products. For example due to the recent pandemic situation, face masks become extremely popular for both buyers and sellers, everyday we need to categorize and update a huge number of masks items. A robust product detection system will significantly improve the listing and categorization efficiency. But in the industrial field the data is always much more complicated and there exists mis-labelled images, complex background images and low resolution images, etc. The noisy and imbalanced data and multiple categories make this problem still challenging in the modern computer vision field.
## Datasets
In Shopee Product Detection Dataset, there are more than 100k images directly from E-commercial industry field. You will be able to explore the real-world images which is noisy and long-tailed, and let your model predict the correct categories for the images. There contains 42 most popular categories product at Shopee.

<img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F5198646%2F8983b696df39ecb3bbd2fb5dcf7303be%2F5d04dd453bbe5b71c00236f9383751e5.jpg?generation=1591669667767485&alt=media" width="200" height="200"><img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F5198646%2F56456e8a500366e15d468ccd8d5f13c2%2F3b1519ee1932c8ed960649be4ff35dec.jpg?generation=1591670501765344&alt=media" width="200" height="200"><img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F5198646%2F24c4289a420487e7ea3117492a03b29a%2F3d52392446452e4eb7e26e4d762467b3.jpg?generation=1591670956360484&alt=media" width="200" height="200"><img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F5198646%2Ff4d283fc00b5f2055893fbca2e62a3b3%2F0dbeed1585ee580bf3d9670e8b23ecc8.jpg?generation=1591671179189986&alt=media" width="200" height="200"><img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F5198646%2F31f1700efb459542f6d5ad5964f61c39%2F2b346cae0305ece2a7e819b833dfd635.jpg?generation=1591671472191358&alt=media" width="200" height="200"><img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F5198646%2F4ca0ca158d7b79f20d3bc2d16abf97e3%2F1cf0391bad6debae1a9cff35153e8962.jpg?generation=1591671513570675&alt=media" width="200" height="200"><img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F5198646%2F74c7ee5182be4902d42f845f3889a433%2F0ad3826c91d647b659794160adb70f92.jpg?generation=1591672539773817&alt=media" width="200" height="200"><img src="https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F5198646%2Fec184aadda0d10cb1b09fa58deb98fc6%2F00ba143008cf454fa24c5f1e1c60c8e5.jpg?generation=1591672611376483&alt=media" width="200" height="200"> 


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
