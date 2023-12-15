# Hold On to Data

**Authors:** Patrick Brophy, Michael Roytman, Prabvir Kukreja  
**Date of submission:** 12/14/2023  

## Abstract

This paper presents an in-depth investigation into the efficacy of data augmentation techniques in improving rock climbing hold detection, utilizing the YOLOv8 architecture. Given the unique challenges posed by the variability in rock climbing hold shapes, sizes, and colors, coupled with diverse lighting conditions and backgrounds, conventional object detection models often struggle to achieve high accuracy.

To address these challenges, we implement various data augmentation strategies, such as rotation, scaling, and color adjustment, to enrich our dataset. The YOLOv8 model, known for its speed and accuracy in object detection, is then trained on this augmented dataset. Our results demonstrate a significant improvement in the model's ability to detect climbing holds under varying conditions, compared to training with non-augmented data. This advancement not only enhances the safety and planning aspects of rock climbing but also contributes to the broader field of object detection in dynamic and unstructured environments.


## How to Run the Code

To run the code, follow these steps:

1. Clone the project repository by executing the following command in your terminal or command prompt:

   ```bash
   git clone https://github.com/mroytman83/CS539_Final_Project
   cd CS539_Final_Project
   cd notebooks
2. WARNING: running the notebook locally will incur very slow performance, unless there is CUDA support.
   It is highly suggested that the base/augmented models are run in a cloud environment such as Google Colab.
   Once the kernel is trsuted, run all, to finetune the model and test it on the out of sample dataset!

