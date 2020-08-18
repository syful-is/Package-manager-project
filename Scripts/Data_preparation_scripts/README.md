# Dataset Preparation:


### step1: Indetify `Package-Managers` related Tags and extract `relevant tags` 

### Step1: `Initial` post extraction using `Package-Managers` tagged post
Script: [3_PM_related_initial_posts.py](Replication_package\Scripts\Data_preparation_scripts/3_PM_related_initial_posts.py)
Output: [syc01_PM_related_initial_post_detailed_syc.csv](Dataset/syc01_PM_related_initial_post_detailed_syc.csv)

### Step2: Tag extract from `initial` posts set and `initial post count` from total: 806 posts
Local PC Script: [4_tag_count.py](Replication_package\Scripts\Data_preparation_scripts/4_tag_count.py)
Output: [syc02_filtered_tag.csv](Dataset/syc02_filtered_tag.csv)
Afterward collect the tag frequency for all post of SO using the same script. Here the data Source will be `1_all_post_details.csv`
Script:[4.1_tag_count.py](Replication_package\Scripts\Data_preparation_scripts/4.2_tag_count.py)
[syc04_All_tags_detail_information.csv](Dataset/syc04_All_tags_detail_information.csv)


### Step3: `Manual filtering` to ensure  `Package-Managers` related filtered tags
Local PC Script: [5_tag_verification.py](Replication_package\Scripts\Data_preparation_scripts/5_tag_verification.py) and `manual checking`
Output: [syc05_filtered_tag_used_for_data_extraction.csv](Dataset/syc05_filtered_tag_used_for_data_extraction.csv)
After manual verification, we obtain:
[syc05_filtered_tag_used_for_data_extraction.csv](Dataset/syc05_filtered_tag_used_for_data_extraction.csv)
More detail on the google sheet about tag processing (you may  have a look): [PM_tag_processing](https://docs.google.com/spreadsheets/d/1Mf9nqcKyvouTjQQj598uZRuzcIYUSqBB9UeIiKVy6hA/edit?usp=sharing)
step2: Extract `Package-Managers` related posts
Step1: Find the `Final question post dataset` from SO main post dataset
Script:  [6_PM_related_post_extract.py](Replication_package\Scripts\Data_preparation_scripts/6_PM_related_post_extract.py)
Ouput: [syc06_PM_all_question_post.csv](Dataset/syc06_PM_all_question_post.csv)
Script: [7_PM_related_Answer_post_extract.py](Replication_package\Scripts\Data_preparation_scripts/7_PM_related_Answer_post_extract.py)
Output:[syc07_PM_all_answer.csv](Dataset/syc07_PM_all_answer.csv)
Step3: `Number of PM posts` 
Question Post: 22270 (47.32%)
Answer Post: 248036 (52.68%)
Total: 470806 (100%)

