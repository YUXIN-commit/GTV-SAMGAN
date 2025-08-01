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

Prepare your own dataset and refer to the samples in `GTV-SAMGAN/data_demo`  to replace them according to your specific scenario. You need to generate the	`image2label_train.json` file before running train.py.

	cd ./GTV-SAMGAN
 	python train.py

* work_dir: Specifies the working directory for the training process. Default value is workdir.
* image_size: Default value is 256.
* data_path: Dataset directory, for example: data_demo.
* resume: Pretrained weight file, ignore sam_checkpoint if present.
* sam_checkpoint: Load sam checkpoint.
* encoder_adapter: Whether to fine-tune the Adapter layer, set to False only for fine-tuning the decoder.
* use_amp: Set whether to use mixed-precision training.

#### Pretrain Weights
We fine-tuned the pretrained model from [SAM-Med2D](https://github.com/OpenGVLab/SAM-Med2D/tree/main).

The pretrained weights can be downloaded from the following link.
Baidu Cloud: https://pan.baidu.com/s/1HWo_s8O7r4iQI6irMYU8vQ?pwd=dk5x
Extraction code: dk5x

### **Test**

	cd ./GTV-SAMGAN
 	python test.py

* work_dir: Specifies the working directory for the testing process. Default value is workdir.

#### Test multiple model parameter files. 

At the end of the `test.py` file, use the following code to test multiple model parameter files.

`model_dir` specifies the folder containing the model parameter files to be tested.

	#Test multiple model parameter files.
 
	if __name__ == '__main__':
	    args = parse_args()

	    #Get all .pth files under the specified folder.
	    model_dir = r"workdir\models\GTV-SAMGAN"
	    pth_files = [os.path.join(model_dir, f) for f in os.listdir(model_dir) if f.endswith('.pth')] 
	    for pth_file in pth_files: 
	        args.sam_checkpoint = pth_file 
	        print(f"Current sam_checkpoint: {args.sam_checkpoint}")
	        main(args)
	    print('============================All tests are complete. Please check the CSV document.==========================================================')

After testing is complete, a `.csv` file will be generated to store the evaluation results for each model parameter.

#### Test single model parameter file.

At the end of the `test.py` file, use the following code to test multiple model parameter files.
`pth_file` refers to the specific model parameter file you want to test.

	#Test a single model parameter file.
	if __name__ == '__main__':
	   args = parse_args()
	   pth_file = r"workdir\GTV-SAMGAN_model"
	   args.sam_checkpoint = pth_file 
	   main(args)       

## Reference

	@misc{cheng2023sammed2d,
	      title={SAM-Med2D}, 
	      author={Junlong Cheng and Jin Ye and Zhongying Deng and Jianpin Chen and Tianbin Li and Haoyu Wang and Yanzhou Su and
	              Ziyan Huang and Jilong Chen and Lei Jiangand Hui Sun and Junjun He and Shaoting Zhang and Min Zhu and Yu Qiao},
	      year={2023},
	      eprint={2308.16184},
	      archivePrefix={arXiv},
	      primaryClass={cs.CV}
	}
 
 	@misc{Data From NSCLC-Radiomics (version 4),
	      title={Data From NSCLC-Radiomics (version 4)}, 
	      author={Aerts, H. J. W. L., Wee, L., Rios Velazquez, E., Leijenaar, R. T. H., Parmar, C., Grossmann, P., Carvalho, S., Bussink, J., Monshouwer, R., Haibe-Kains, B., Rietveld, D., Hoebers, F., Rietbergen, M. M., Leemans, C. R., Dekker, A., Quackenbush, J., Gillies, R. J., Lambin, P.},
	      year={2014},
	      eprint={https://doi.org/10.7937/K9/TCIA.2015.PF0M9REI},
              archivePrefix={The Cancer Imaging Archive},
	}



