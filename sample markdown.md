# Compare two images to see how similar they are to each other

This `image-similarity` API enables you to compare two images and determine how visually similar they’re to each other using Amazon Mechanical Turk (MTurk). This is useful in the field of computer vision, for example when building visual search that returns similar looking products. The API takes as input URL of the two images to be analyzed and returns a score between 0 and 1 indicating how similar the images are to each other where 1 being the most similar.

Here’s an example of the Input object and the Result object:

### Example request:

```python
{
  "input": {
    "image1": {"url":"https://s3-us-west-2.amazonaws.com...a1.jpg"},
    "image2": {"url":"https://s3-us-west-2.amazonaws.com...g1.jpg"}
   }
}
```

### Example Result:

```python
{
  "result": {
    "similarityScore": 0.5
  }
}
```

Here’s how the images might be presented to Workers on MTurk.

![Worker Preview of HIT](https://cdn-images-1.medium.com/max/800/1*S268GrGji75KrQmfW62LNA.png "Worker Preview of HIT")

The API implements an adjudication strategy based on Worker agreement and returns results only when it reaches confidence.

---
