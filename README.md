# Instructions to run the code

This is the repository for the CBCBR related experiments described in the IJCAI paper (https://www.ijcai.org/proceedings/2022/709). 

-To run the code, MSSQL 2019 Server (or later versions) needs to be installed and a database named IJCAI2022 should be in place. It is also neccesary to import Flogard et al.'s dataset into a table named dbo.BayesianDynamicChecklistLocalDb within the IJCAI2022 database. The dataset is located at https://ieee-dataport.org/open-access/labour-inspection-checklist-content

-The mycbr rest api should be downloaded and installed before running the code (see https://github.com/ntnu-ai-lab/mycbr-rest). 

-After that, this repository should be downloaded. Then the file named mycbr-3.3-SNAPSHOT needs to be copied from this repository and pasted in to the folder named \lib\no\ntnu\mycbr\mycbr-sdk\myCBR\myCBR\3.3-SNAPSHOT in the folder where the newly installed mycbr rest api is located. It may be neccesary to re-run mvn clean install. 

-Then the filed named KPValideringBayesianFylkeTheme.prj should be copied and pasted into the base folder of the mycbr rest api. 

-The application can then be run according to the instructions in https://github.com/ntnu-ai-lab/mycbr-rest, by  running the command: java -DMYCBR.PROJECT.FILE="./KPValideringBayesianFylkeTheme.prj" -jar ./target/mycbr-rest-2.0.jar

-The code should be opened with Jupyter Notebook. 
