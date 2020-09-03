# Package-manager-project:


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3988740.svg)](https://doi.org/10.5281/zenodo.3988740)


### Paper Title: The Brokers in a Dependency Ecosystem: An Empirical Study on using Package Managers


**Authors:** Syful Islam, Raula Gaikovina Kula, Christoph Treude, Bodin Chinthanet, Takashi Ishio, and Kenichi Matsumoto 


**Abstract:** A package manager (PM) is crucial to most technology stacks, acting as a broker to ensure that a verified dependency package is correctly installed, configured, or removed from an application.
Diversity in technology stacks has led to dozens of PMs with various features.
While recent studies have shown that developers struggle to migrate their dependencies, the common assumption is that PMs broker dependencies without any issues. 
In this paper, we would like to explore issues faced by developers when using PMs through an empirical study of content on Stack Overflow (SO).
Through a quantitative analysis of 470,806  posts related to 16 PMs, we first determine the importance of PM-related posts and extract topics contained in these posts.
We then carry out a qualitative analysis of 1,131 posts related to the Maven, npm, and NuGet dependency ecosystems to analyze questions, underlying causes and their resolutions.
Our results confirm that developers tend to struggle with PMs.
The choice of PM affects their user experience, as questions are likely to arise from lack of instructions and error messages.
We find that PM-related posts are not likely to get resolved, with only 40\% to 50\% having an accepted answer.
Our work further lays out a road-map to investigate the trade-off between design features to understand what an ideal PM would look like.

# Study design:
We divide our empirical study into three parts with six research questions:

**1. Characterizing PM-related posts and topics:**

        RQ1: How do PM-related posts compare to the rest of SO posts?
        
        RQ2: What kind of topics are present in PM-related posts?
        
        
**2. Analyzing PM-related posts in terms of their question and its underlying cause:**

        RQ3: What kinds of PM questions do developers ask?
        
        RQ4: What are the underlying causes of a PM-related post?
        
        
**3. Analyzing the information needed to resolve a PM-related post:**

        RQ5: What type of PM-related posts get resolved?
        
        RQ6: What information is needed to resolve a PM-related post?
        


# Replication package Structure:
```
📁 Package-manager-project/
├─ 📁 Dataset/
|
├─ 📁 Scripts/
|  ├─ 📁 Data_preparation_scripts/
|  ├─ 📁 RQ1_scripts/
|  ├─ 📁 RQ2_scripts/
|  ├─ 📁 RQ3_4_5_6_scripts/
|
├─ 📁 Results/
|  ├─ 📁 RQ1/
|  ├─ 📁 RQ2/
|  |  ├─ 📁 Figures/
|  |  ├─ 📁 Topic_popularity_and_difficulty_Results/
|  ├─ 📁 RQ3_4_5_6/ 
|     ├─ 📁 Manual_analysis_Results/
|     ├─ 📁 Association_rules/
|
─
```
### Contents:
  1. [Dataset](https://github.com/syful-is/Package-manager-project/tree/master/Dataset)- is a folder that contains the dataset for `Package-manager project`.
  2. [Scripts](https://github.com/syful-is/Package-manager-project/tree/master/Scripts)- is a folder that contains the all the codes. 
  3. [Results](https://github.com/syful-is/Package-manager-project/tree/master/Results)- is a folder that contains the results obtained from dataset.

# How to run:
  1. Download the dataset from: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3988740.svg)](https://doi.org/10.5281/zenodo.3988740)
  2. Extract the files.
  3. Clone this repository into your userhome folder in the system
  ```https://github.com/syful-is/Package-manager-project.git```
  3. Open `Jupyter Notebook` or `Python Spyder`.
  4. Copy any code and Set your working directory using 
                
                ```
                import os
                
                #Please specify your dataset directory. 
                os.chdir("..../Dataset/")
                ```
  
  4. Example-1: Run the **[kruskal_and_cohen_1c.ipynb](https://github.com/syful-is/Package-manager-project/blob/master/Scripts/RQ1_scripts/kruskal_and_cohen_1c.ipynb)** for testing the statistical significance of the `reputation` of developers who belong to PM posts (Part of RQ1).
  5. Example-2: Run the **[RQ2_LDA_sychra.ipynb](https://github.com/syful-is/Package-manager-project/blob/master/Scripts/RQ2_scripts/RQ2_LDA_sychra.ipynb)**  for LDA topic modeling (Part of RQ2)


# Authors:
  
  1. [Syful Islam](https://syful-is.github.io/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
  2. [Raula Gaikovina Kula](https://raux.github.io/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
  3. [Christoph Treude](http://ctreude.ca/), University of Adelaide, Adelaide, Australia.
  4. [Bodin Chinthanet](https://bchinthanet.com/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
  5. [Takashi Ishio](https://takashi-ishio.github.io/), Nara Institute of Science and Technology (NAIST), Nara, Japan.
  6. [Kenichi Matsumoto](http://isw3.naist.jp/Contents/Research/cs-05-en.html), Nara Institute of Science and Technology (NAIST), Nara, Japan.

