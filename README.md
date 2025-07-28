# GTV-SAMGAN Integrating GTV-MFIT and Generative Adversarial Networks in SAM-med2d for Lung Cancer GTV Segmentation

We would like to thank [SAM-Med2D](https://github.com/OpenGVLab/SAM-Med2D/tree/main); our code is based on theirs with modifications.

## **Datasets**

In this study, we utilized two lung cancer datasets.

### 1. Public Dataset

   The public dataset was obtained from the[NSCLC-Radiomics Dataset](https://www.cancerimagingarchive.net/collection/nsclc-radiomics/)，which contains images from 422 patients with non-small cell lung cancer (NSCLC).
### 2. Local Dataset

    The local dataset is a clinical dataset collected from a local hospital, comprising 112 lung cancer patients who underwent radiotherapy. The median age of the patients was 64 years, with an age range of 40 to 89 years. This dataset is confidential and not publicly available.

## **Usage**

This code has been implemented in python language using Pytorch library and tested in ubuntu OS, though should be compatible with related environment.

### **Installation**

Run the following code to install the Requirements:

        pip install -r requirements.txt

### **Train**

Prepare your own dataset and refer to the samples in __GTV-SAMGAN/data_demo__  to replace them according to your specific scenario. You need to generate the	__image2label_train.json__ file before running train.py.

	cd ./GTV-SAMGAN
 	python train.py

* work_dir: Specifies the working directory for the training process. Default value is workdir.
* image_size: Default value is 256.
* data_path: Dataset directory, for example: data_demo.
* resume: Pretrained weight file, ignore sam_checkpoint if present.
* sam_checkpoint: Load sam checkpoint.

#### Pretrain Weights
We fine-tuned the pretrained model from [SAM-Med2D](https://github.com/OpenGVLab/SAM-Med2D/tree/main).

The pretrained weights can be downloaded from the following link.
Baidu Cloud: https://pan.baidu.com/s/1HWo_s8O7r4iQI6irMYU8vQ?pwd=dk5x
Extraction code: dk5x
