# The NWPU-Crowd Dataset
The NWPU-Crowd Dataset is constructed by Wang et al., from NWPU. It is a large-scale congested crowd counting dataset that consists of 5,109 images crawled from the Internet, elaborately annotating 2,133,238 instances. If you would like to submit your results, please register, login, and read the guideline:

## Update 2020.05.22

1. Provide the box-level labels for each head.
2. 


## Guideline
1. You have 6 submissions in a natural month. You are allowed to train your model and select the best one according to the performance on the validation set. Once cheating is found on an account or a group of accounts, we will remove the accounts and permanently ban the IP.
2. For counting tasks, the submission file should be ```*.txt``` format, which has 1,500 lines. In each line, the first item is the image id of the test set and the second item is the prediction value. For example,
```
3610 100.0000
3611 2.2456
...
5109 8976.0173
```
3. For localization tasks, the submission file should be ```*.txt``` format, which has 1,500 lines. In each line, the first item is the image id of the test set; the second item is the number of head (N); the otehrs are N*2 values, which represents the positions (```x,y```) of N points. Different from counting, all number must be ```integer```. For example,
```
3610 1 5 5
3611 0
3612 3 1 1 2 2 3 3
...
5109 10 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10 
```
4. You are allowed to select a submission to show the leaderboard.
5. Once the leaderboard changes, we will keep a copy as a record, which can be treated as evidence.

## License
This dataset is for academic and non-commercial uses (such as academic research, teaching, scientific publications, or personal experimentation), of which data are collected from the Internet. However, if you find yourself or your personal belongings in the data, please contact us, and we (NWPU) will immediately remove the respective images from our servers. The content of the data does not represent any of the authors’ views, including but not limited to the following: political positions, religious beliefs, etc. Permission is granted to use the data given that you agree to the license terms as follows:
1. The labeling process of the dataset suffers from our strict multi-stage annotation and refinement. Nevertheless, we (NWPU) do not accept any responsibility for errors or omissions.
2. You should include a reference to the NWPU-Crowd Dataset in any work that makes use of the dataset.
3. You do not distribute this dataset or modified versions.
4. You may not use the dataset or any derivative work for commercial purposes as, for example, licensing or selling the data, or using the data with a purpose to procure a commercial gain.
5. All rights not expressly granted to you are reserved by us (NWPU).

## Data Format

1. The dataset provides ```*.jpeg``` images, and two types of labels(```jsons``` and ```mats```). The points order is ```x, y```. To be specific, the contents of ```.mat``` files are consistent with the UCF-QNRF. The boxes labels is ```xmin, ymin, xmax, ymax```.
2. Each line in ```train.txt``` and ```val.txt``` has three items, image id, luminance label, and scene level. 
3. Each line in ```test.txt``` has only one item, image id.





