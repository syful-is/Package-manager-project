# Package-manager-project:

### Step1: Prepare `All question dataset with meta information`....

Sub-step1:  Prepare dataset with all meta information
script:[RQ3_all_metadata.py](F:\1_NAIST_Research_SE\SE_code\RQ3_all_metadata.py)
Output: [RQ2_lda_15_topics_with_all_metadata_06_04_2020.csv](F:/1_NAIST_Research_SE/SE_meeting/PM_Stackoverflow/RQ2_answer/LDA_15_topics/RQ2_lda_15_topics_with_all_metadata_06_04_2020.csv)

Sub-step2:  Seperate samples for three package manager (`maven`, `npm`, `Nuget`)
Script: [Seperate_Dataset_for_three_PM.py](RQ3_scripts/Seperate_Dataset_for_three_PM.py)
Output1: [PM_Maven_all_questions.csv](RQ3/PM_Maven_all_questions.csv)
Output2: [PM_npm_all_questions.csv](RQ3/PM_npm_all_questions.csv)
Output3: [PM_nuget_all_questions.csv](RQ3/PM_nuget_all_questions.csv)


Sub-step3: Prepare `Samples` for all three cases  (`maven`, `npm`, `Nuget`)


Survey sample calculator: 
[sscalc.htm](https://www.surveysystem.com/sscalc.htm)
For `maven` sample size= 382
For `npm` sample size= 379
For `Nuget` sample size= 370


Script: to prepare samples
[prepare_samples.py](F:\1_NAIST_Research_SE\SE_code\prepare_samples.py)
Sample Dataset: 
output1: [PM_Maven_all_sample.csv](RQ3/PM_Maven_all_sample.csv)
output2: [PM_npm_all_sample.csv](RQ3/PM_npm_all_sample.csv)
output3: [PM_nuget_all_sample.csv](RQ3/PM_nuget_all_sample.csv)


Sub-step4: Here we performed manual analysis for RQ3,4,5, & 6

Results: You can find the offline version of the result in:
[PM_undelyning_cause_question_coding.xlsx](Replication_package\Results\RQ3_4_5_6\Results\PM_undelyning_cause_question_coding.xlsx)
[PM_Attribute_coding.xlsx](Replication_package\Results\RQ3_4_5_6\Results\PM_Attribute_coding.xlsx)


Result: Link of google sheet for manual analysis [Online]:
[Underlyning_cause_and_question_coding](https://docs.google.com/spreadsheets/d/1Dtc4i5Ex88EPjFCBrTP8efKr5RC1yeW6LwgT0YPMGBw/edit?usp=sharing)
[Attribute coding](https://docs.google.com/spreadsheets/d/1iWf_rnPx8KdisGgjVJuajTQgGtRUjfXaVtb7DTYSs34/edit?usp=sharing)

step2:  `RQ6` (Qualitative)

Script: [Association_rule_mining.py](RQ3_scrips/Association_rule_mining.py)

Results: Association rule mining results:
Directory: Replication_package\Results\RQ3_4_5_6\Results

Manual analysis of image link
Result: [Image_link_analysis.xlsx](Replication_package\Results\RQ3_4_5_6\Results\Image_link_analysis.xlsx)

Google sheet results [Online]
[Image link analysis](https://docs.google.com/spreadsheets/d/1Zff8Z8Ujsd5W_XFYWFQV80fPrU_u_PCiWC29CPSO4Ws/edit?usp=sharing)


