#### 目標：
Use saliency map to show where does model concentrate on.

#### Problem: 
Multi-channel model will create same size saliency maps even thought brain in each channel is not in same size.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/101687024/210765788-ad9d6e0d-d9f6-464f-b7c5-abeae21be54b.png">

current solution:
Trained 90 models for each level of brain, so each level has its own saliency which means they will not interfere each other level and have different size.
But it’s really time consuming.

<img width="400" alt="image" src="https://user-images.githubusercontent.com/101687024/210766647-e27bf161-7dba-499d-a5b8-443dcf5f29e0.png">


#### Next step:
Intersection of saliency map between Alzheimer and sex.
we trained the model to classified man and women, and show the intersection of saliency map between alzheimer disease and sex

<img width="400" alt="image" src="https://user-images.githubusercontent.com/101687024/210766503-82eb2abc-b270-4ebe-8a49-8ddeb943752d.png">
As the image shows saliency map between Alzheimer disease and sex has a lot interset area ,this may imply that man and women might be one feature when prediction Alzheimer disease.




