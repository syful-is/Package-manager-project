# Package-manager-project:


# Steps to prepare result of RQ2:

### Step1: Perform topic modeling using LDA:
Script: [RQ2_LDA_sychra.ipynb](https://github.com/syful-is/Package-manager-project/blob/master/Scripts/RQ2_scripts/RQ2_LDA_sychra.ipynb)

### Step2: Process the output of LDA topic mdodeling:
 Scripts: 

This script is used to map the PM question posts into `Language, environment, dependency`
[1_metric_mapping.py](RQ2_scripts/1_metric_mapping.py)

This script is used to map the topics (15 into 3 theme topics)
[2_major_cat_mapping.py](RQ2_scripts/2_major_cat_mapping.py)

This script is used to map the topics (15 into 10 topics)
[3_mapped_by_major_cat_version_2.py](RQ2_scripts/3_mapped_by_major_cat_version_2.py)

This script is used to map the question posts into language support
[4_mapped_by_language.py](RQ2_scripts/4_mapped_by_language.py)

This script is used to map the question posts into PM list
[5_mapped_by_PM.py](RQ2_scripts/5_mapped_by_PM.py)

This script is used to map the question posts into environment support
[6_mapped_by_environment.py](RQ2_scripts/6_mapped_by_environment.py)

This script is used to map the question posts into dependency  tree
[7_mapped_by_dependency.py](RQ2_scripts/7_mapped_by_dependency.py)

### Script for preparing input of dendrogram visualizations:

[8_mapped_by_major_category.py](RQ2_scripts/8_mapped_by_major_category.py)

[9_dependency_mapped_by_major.py](RQ2_scripts/9_dependency_mapped_by_major.py)

[10_mapped_by_major_category.py](RQ2_scripts/10_mapped_by_major_category.py)

[11_language_mapped_by_major.py](RQ2_scripts/11_language_mapped_by_major.py)

[12_PM_mapped_major_Cat.py](RQ2_scripts/12_PM_mapped_major_Cat.py)


LDA topic summary:
[RQ2_topics_detail.xlsx](Replication_package\Results\RQ2\Results\RQ2_topics_detail.xlsx)

To see topic summary detail, you can go through the google sheet
Google sheet: [Topic Summary](https://docs.google.com/spreadsheets/d/12BC_5m2FWTlJJpat73monxQCODZk9o_t4s0ZDU900EQ/edit?usp=sharing)



