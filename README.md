# Intelligent Early Wildfire Detection

Wildfires are one of the main contributing factors to the acceleration of tree cover loss. This has a tremendous impact on the environment as the rate at which CO2 is absorbed becomes lower than the emission rate from burning fossil fuels. Such imbalance has a clear impact on the global temperature and is further aggravated by deforestation and land degradation. Ultimately, by exhausting the environment from its resources, the consequences of catastrophes -  both natural and human-caused - are likely to worsen and lead to greater losses. It is, thus, critical to develop and employ the right detection systems that can alert on active fires and help mitigate the impact on the environment.

# File Structure

## models
contains experiment files for different model approaches 

experimentN : Contains different experiments trying to solve the issue

## data_collection
Contains methods for collecting data and pre processing it to create datasets for AI models.

**contains git ignored files**
data_collection/my_nasa_api_key : can be obtained at https://api.nasa.gov/

## data (git ignored)
Folder containing downloaded material due to large file sizes is exluded from git should only contain downloaded 

**contains** 
data/FPA_FOD_20170508.sqlite : Source https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires

## datasets
Contains some processed data such as forest fire locations and other semi-ready and ready data to be used in programs and models.

## scripts
Contains python scripts that handle some kind of tasks that are not related to dataprep or ML tasks. For example getting data out of an sqlite database.

Will contain a requirements.txt file once any are required.





