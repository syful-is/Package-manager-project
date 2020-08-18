# Dataset Preparation:


## Indetify `Package-Managers` related Tags and extract `relevant tags` 

### Initially, we seprate all the question and answer post from SO:
Script:[1_All_question_post_SO.py](https://github.com/syful-is/Package-manager-project/blob/master/Scripts/Data_preparation_scripts/1_All_question_post_SO.py)

Script:[2_All_answer_post_SO.py](https://github.com/syful-is/Package-manager-project/blob/master/Scripts/Data_preparation_scripts/2_All_answer_post_SO.py)

### Step1: `Initial` post extraction using `Package-Managers` tagged post
Script: [3_PM_related_initial_posts.py](https://github.com/syful-is/Package-manager-project/blob/master/Scripts/Data_preparation_scripts/3_PM_related_initial_posts.py)

### Step2: Tag extract from `initial` posts set and `initial post count` from total: 806 posts

Script: [4.1_tag_count.py](https://github.com/syful-is/Package-manager-project/blob/master/Scripts/Data_preparation_scripts/4.1_tag_count.py)

Afterward collect the tag frequency for all post of SO using the same script. 

Script:[4.1_tag_count.py](https://github.com/syful-is/Package-manager-project/blob/master/Scripts/Data_preparation_scripts/4.2_tag_count.py)


### Step3: `Manual filtering` to ensure  `Package-Managers` related filtered tags

Script: [5_tag_verification.py](https://github.com/syful-is/Package-manager-project/blob/master/Scripts/Data_preparation_scripts/5_tag_verification.py) and `manual checking`

After manual verification, we obtain: [syc05_filtered_tag_used_for_data_extraction.csv]


More detail on the google sheet about tag processing (you may  have a look): [PM_tag_processing](https://docs.google.com/spreadsheets/d/1Mf9nqcKyvouTjQQj598uZRuzcIYUSqBB9UeIiKVy6hA/edit?usp=sharing)


### Step4: Extract `Package-Managers` related posts

Script: [6_PM_related_post_extract.py](https://github.com/syful-is/Package-manager-project/blob/master/Scripts/Data_preparation_scripts/6_PM_related_post_extract.py)-Find the `Final question post dataset` from SO main post dataset

Script: [7_PM_related_Answer_post_extract.py](https://github.com/syful-is/Package-manager-project/blob/master/Scripts/Data_preparation_scripts/7_PM_related_Answer_post_extract.py)- Find the `Final PM answer post dataset` from SO main post dataset


### Step5: `Number of PM posts` summary

Question Post: 22270 (47.32%)

Answer Post: 248036 (52.68%)

Total: 470806 (100%)

