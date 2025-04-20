from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components import DataIngestion
from cnnClassifier import logger
import sys
print(sys.path)

STAGE_NAME = "Data Ingestion"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<<<")
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()
        logger.info(f">>>>>>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e