from sqlalchemy import Column, Integer, String, ARRAY, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Creator(Base):
    """Creator _summary_

    Args:
        Base (_type_): _description_
    """    
    __tablename__ = "creators"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    model_count = Column(Integer)
    link = Column(String)

class Model(Base):
    """Model _summary_

    Args:
        Base (_type_): _description_
    """    
    __tablename__ = "models"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    type = Column(String)#	enum (Checkpoint, TextualInversion, Hypernetwork, AestheticGradient)
    nsfw = Column(Boolean)
    tags = Column(ARRAY(String))
    creator_username = Column(String)
    creator_image = Column(String) #TODO: figure out key to creator table
    model_versions_id = Column(Integer)
    model_versions_name = Column(String)
    model_versions_created_at = Column(DateTime)
    model_versions_download_url = Column(String)
    model_versions_trained_words = Column(ARRAY(String))
    model_versions_files_size_kb = Column(Integer)
    model_versions_files_format = Column(String)
    model_versions_files_pickle_scan_result = Column(String)
    model_versions_files_virus_scan_result = Column(String)
    model_versions_files_scanned_at = Column(DateTime)
    model_versions_images_url = Column(String)
    model_versions_images_nsfw = Column(String)
    model_versions_images_width = Column(Integer)
    model_versions_images_height = Column(Integer)
    model_versions_images_hash = Column(String)
    model_versions_images_meta = Column(String)#generation params of image (object | null)

class ModelVersion(Base):
    """ModelVersion _summary_

    Args:
        Base (_type_): _description_
    """    
    __tablename__ = "model_versions"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    model_name = Column(String)
    model_type = Column(String)
    model_nsfw = Column(Boolean)
    model_poi = Column(Boolean)
    model_id = Column(Integer)
    created_at = Column(DateTime)
    download_url = Column(String)
    trained_words = Column(ARRAY(String))
    files_size_kb = Column(Integer)
    files_format = Column(String)
    files_pickle_scan_result = Column(String)
    files_virus_scan_result = Column(String)
    files_scanned_at = Column(DateTime)
    images_url = Column(String)
    images_nsfw = Column(String)
    images_width = Column(Integer)
    images_height = Column(Integer)
    images_hash = Column(String)
    images_meta = Column(String)

class Tag(Base):
    """Tag _summary_

    Args:
        Base (_type_): _description_
    """    
    __tablename__ = "tags"
    name = Column(String, primary_key=True)
    model_count = Column(Integer)
    link = Column(String)
    metadata_total_items = Column(String)
    metadata_current_page = Column(String)
    metadata_page_size = Column(String)
    metadata_total_pages = Column(String)
    metadata_next_page = Column(String)
    metadata_prev_page = Column(String)
