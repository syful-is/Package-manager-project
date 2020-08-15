# Package-manager-project
**Paper Title: The Brokers in a Dependency Ecosystem: An Empirical Study on using Package Managers**


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

**Study design:**
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
        


**Replication package Structure**
```
📁 Replication_package/
├─ 📁 Dataset/
|
├─ 📁 Scripts/
|  ├─ 📁 Data_preparation_scripts
|  ├─ 📁 RQ1_scripts
|  ├─ 📁 RQ2_scripts
|  ├─ 📁 RQ3_4_5_6_scripts
|
├─ 📁 Results/
|  ├─ 📁 RQ1
|  ├─ 📁 RQ2
|  ├─ 📁 RQ3_4_5_6 
|
─

```
